"""
Functions relating to Eularian graphs.

This module contains functions relating to the identification
and solution of Eularian trails and Circuits.

"""
import collections
import copy
import itertools
import random

import dijkstra
import my_math
from my_iter import all_unique, flatten_tuples

def fleury_walk(graph, start=None, circuit=False):
    """
    Return an attempt at walking the edges of a graph.

    Tries to walk a Circuit by making random edge choices. If the route
    dead-ends, returns the route up to that point. Does not revisit
    edges.

    If circuit is True, route must start & end at the same node.

    """
    visited = set()  # Edges

    # Begin at a random node unless start is specified
    node = start if start else random.choice(graph.node_keys)

    route = [node]
    while len(visited) < len(graph):
        # Fleury's algorithm tells us to preferentially select non-bridges
        reduced_graph = copy.deepcopy(graph)
        reduced_graph.remove_edges(visited)
        options = reduced_graph.edge_options(node)
        bridges = [k for k in options.keys() if reduced_graph.is_bridge(k)]
        non_bridges = [k for k in options.keys() if k not in bridges]
        if non_bridges:
            chosen_path = random.choice(non_bridges)
        elif bridges:
            chosen_path = random.choice(bridges)
        else:
            break  # Reached a dead-end, no path options
        next_node = reduced_graph.edges[chosen_path].end(node)  # Other end

        visited.add(chosen_path)  # Never revisit this edge

        route.append(next_node)
        node = next_node

    return route

def eularian_path(graph, start=None, circuit=False):
    """
    Return an Eularian Trail or Eularian Circuit through a graph, if found.

    Return the route if it visits every edge, else give up after 1000 tries.

    If `start` is set, force start at that Node.

    """
    for i in range(1, 1001):
        route = fleury_walk(graph, start, circuit)
        if len(route) == len(graph) + 1:  # We visited every edge
            return route, i
    return [], i  # Never found a solution


def find_dead_ends(graph):
    """
    Return a list of dead-ended edges.

    Find paths that are dead-ends. We know we have to double them, since
    they are all order 1, so we'll do this ahead of time to alleviate
    odd pair set finding.

    """
    single_nodes = [k for k, order in graph.node_orders.items() if order == 1]
    return [x for k in single_nodes for x in graph.edges.values() \
            if k in (x.head, x.tail)]

def build_node_pairs(graph):
    """ Builds all possible odd node pairs. """
    odd_nodes = graph.odd_nodes
    return (x for x in itertools.combinations(odd_nodes, 2))

def build_path_sets(node_pairs, set_size):
    """ Builds all possible sets of odd node pairs. """
    return (x for x in itertools.combinations(node_pairs, set_size) \
            if all_unique(flatten_tuples(x)))

def arrange_into_pairs(node_sets, node_count):
    """
    Split the set of nodes into pairs of tuples.

    e.g. (1, 2, 3, 4) --> [(1, 2), (3, 4)]

    """
    return (((x[i], x[i+1]) for i in range(0, node_count, 2)) \
        for x in node_sets)

def find_set_cost(path_set, graph):
    """ Find the cost and route for each node pairs in a set of path options. """
    return {pair: dijkstra.find_cost(pair, graph) for pair in pair_set}

def find_node_pair_solutions(node_pairs, graph):
    """ Return path and cost for all node pairs in the path sets. """
    node_pair_solutions = collections.OrderedDict()
    for node_pair in node_pairs:
        if node_pair not in node_pair_solutions:
            cost, path = dijkstra.find_cost(node_pair, graph)
            node_pair_solutions[node_pair] = (cost, path)
            # Also store the reverse pair
            node_pair_solutions[node_pair[::-1]] = (cost, path[::-1])
    return node_pair_solutions

def find_minimum_path_set(pair_sets, pair_solutions):
    """ Return cheapest cost & route for all sets of node pairs. """
    cheapest_set = None
    min_cost = float('inf')
    for pair_set in pair_sets:
        set_cost = sum(pair_solutions[pair][0] for pair in pair_set)
        if set_cost < min_cost:
            cheapest_set = pair_set
            min_cost = set_cost
            min_route = [pair_solutions[pair][1] for pair in pair_set]

    return cheapest_set, min_route

def add_new_edges(graph, min_route):
    """ Return new graph w/ new edges extracted from minimum route. """
    new_graph = copy.deepcopy(graph)
    for node in min_route:
        for i in range(len(node) - 1):
            start, end = node[i], node[i + 1]
            cost = graph.edge_cost(start, end)  # Look up existing edge cost
            new_graph.add_edge(start, end, cost, False)  # Append new edges
    return new_graph

def make_eularian(graph):
    """ Add necessary paths to the graph such that it becomes Eularian. """
    print('\tDoubling dead_ends')
    dead_end_edges = find_dead_ends(graph)
    print('\t\tFound {} dead ends'.format(len(dead_end_edges)))
    graph.add_edges([x.contents for x in dead_end_edges])  # Double our dead-ends

    print('\tBuilding odd node pairs')
    node_pairs = build_node_pairs(graph)

    print('\tFinding pair solutions')
    pair_solutions = find_node_pair_solutions(node_pairs, graph)

    print('\tBuilding path sets')
    set_size = int(len(graph.odd_nodes)/2)
    pair_sets = build_path_sets(node_pairs, set_size)
    print(list(pair_sets))

    print('\tFinding cheapest route')
    cheapest_set, min_route = find_minimum_path_set(pair_sets, pair_solutions)
    print('\tAdding new edges...')
    print(cheapest_set)
    print(min_route)
    final_graph = add_new_edges(graph, min_route)  # Add our new edges
    return final_graph


if __name__ == '__main__':
    import tests.run_tests
    tests.run_tests.run(['eularian'])

