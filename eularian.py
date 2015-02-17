"""
Functions relating to Eularian graphs.

This module contains functions relating to the identification
and solution of Eularian trails and Circuits.

"""
import copy
import itertools
import random

import dijkstra
import my_math
import my_iter

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


def build_path_sets(graph):
    """ Builds all possible sets of odd node pairs. """
    odd_nodes = graph.odd_nodes
    combos = list(itertools.combinations(sorted(odd_nodes), 2))
    no_of_pairs = len(odd_nodes) / 2

    sets_2 = list(itertools.combinations(combos, no_of_pairs))
    #print(sets_2)
    sets_unique = [x for x in sets_2 if my_iter.all_unique(my_iter.flatten_tuples(x))]
    #print(sets_unique)
    return sets_unique

    set_no = 0
    sets = []
    while set_no < len(combos) / no_of_pairs:
        index = set_no
        pairs = []
        while True:
            pairs.append(combos[index])
            previous_nodes = my_iter.flatten_tuples(pairs)  # No repeats!
            for i, combo in enumerate(combos[index + 1:], start=index + 1):
                if all(x not in combo for x in previous_nodes):
                    index = i
                    break
            if len(pairs) == no_of_pairs:
                break
        sets.append(pairs)
        set_no += 1
    print(sets)
    return sets

def find_set_cost(path_set, graph):
    """ Find the cost and route for each path in a set of path options. """
    return {path: dijkstra.find_cost(path, graph) for path in path_set}

def find_set_solutions(path_sets, graph):
    """ Return path and cost for all paths in the path sets. """
    set_solutions = [find_set_cost(path_set, graph) for path_set in path_sets]
    set_costs = [sum(v[0] for v in paths.values()) for paths in set_solutions]
    set_routes = [list(v[1] for v in paths.values()) \
                  for paths in set_solutions]
    return set_routes, set_costs

def find_minimum_path_set(path_sets, set_routes, set_costs):
    """ Find the cheapest of all the path set solutions. """
    min_cost = min(set_costs)
    min_set = path_sets[set_costs.index(min_cost)]
    min_route = set_routes[set_costs.index(min_cost)]
    return min_route, min_cost

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
    print('\tBuilding path sets...')
    path_sets = build_path_sets(graph)  # Get all possible added path sets
    print('\tFinding set solutions...')
    set_routes, set_costs = find_set_solutions(path_sets, graph)
    print('\tFinding cheapest solution...')
    min_route, min_cost = find_minimum_path_set(path_sets, set_routes, set_costs)
    print('\tAdding new edges...')
    new_graph = add_new_edges(graph, min_route)  # Add our new edges
    return new_graph, min_cost


if __name__ == '__main__':
    import tests.run_tests
    tests.run_tests.run(['eularian'])

