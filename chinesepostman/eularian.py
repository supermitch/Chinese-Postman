"""
Functions relating to Eularian graphs.

This module contains functions relating to the identification
and solution of Eularian trails and Circuits.

"""
import copy
import itertools
import random
import sys
from time import clock

from . import dijkstra, my_math
from .my_iter import all_unique, flatten_tuples

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
    return [x for x in itertools.combinations(odd_nodes, 2)]

def build_path_sets(node_pairs, set_size):
    """ Builds all possible sets of odd node pairs. """
    return (x for x in itertools.combinations(node_pairs, set_size) \
            if all_unique(sum(x, ())))

def unique_pairs(items):
    """ Generate sets of unique pairs of odd nodes. """
    for item in items[1:]:
        pair = items[0], item
        leftovers = [a for a in items if a not in pair]
        if leftovers:
            # Python 2.7 version? Are they equivalent??
            for tail in unique_pairs(leftovers):
                yield [pair] + tail
            # Python 3 version:
            # yield from ([pair] + tail for tail in unique_pairs(leftovers))
        else:
            yield [pair]

def find_node_pair_solutions(node_pairs, graph):
    """ Return path and cost for all node pairs in the path sets. """
    node_pair_solutions = {}
    for node_pair in node_pairs:
        if node_pair not in node_pair_solutions:
            cost, path = dijkstra.find_cost(node_pair, graph)
            node_pair_solutions[node_pair] = (cost, path)
            # Also store the reverse pair
            node_pair_solutions[node_pair[::-1]] = (cost, path[::-1])
    return node_pair_solutions

def build_min_set(node_solutions):
    """ Order pairs by cheapest first and build a set by pulling
    pairs until every node is covered. """
    # Doesn't actually work... bad algorithm. What if last node
    # has insane path cost?
    odd_nodes = set([x for pair in node_solutions.keys() for x in pair])
    # Sort by node_pair cost
    sorted_solutions = sorted(node_solutions.items(), key=lambda x:x[1][0])
    path_set = []
    for node_pair, solution in sorted_solutions:
        if not all(x in odd_nodes for x in node_pair):
            continue
        path_set.append((node_pair, solution))
        for node in node_pair:
            odd_nodes.remove(node)
        if not odd_nodes:  # We've got a pair for every node
            break
    print(path_set)
    return path_set


def find_minimum_path_set(pair_sets, pair_solutions):
    """ Return cheapest cost & route for all sets of node pairs. """
    cheapest_set = None
    min_cost = float('inf')
    min_route = []
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
    graph.add_edges([x.contents for x in find_dead_ends(graph)])  # Double our dead-ends

    print('\tBuilding possible odd node pairs')
    node_pairs = list(build_node_pairs(graph))
    print('\t\t({} pairs)'.format(len(node_pairs)))

    print('\tFinding pair solutions')
    pair_solutions = find_node_pair_solutions(node_pairs, graph)
    print('\t\t({} solutions)'.format(len(pair_solutions)))

    print('\tBuilding path sets')
    pair_sets = (x for x in unique_pairs(graph.odd_nodes))

    print('\tFinding cheapest route')
    cheapest_set, min_route = find_minimum_path_set(pair_sets, pair_solutions)
    print('\tAdding new edges')
    return add_new_edges(graph, min_route)  # Add our new edges

if __name__ == '__main__':
    import tests.run_tests
    tests.run_tests.run(['eularian'])

