"""
Solve the Chinese-Postman problem.

For a given graph, determine the minimum amount of backtracking
required to complete an Eularian circuit.

"""
import copy
import itertools
import random

import dijkstra
import eularian
import graph as gr
import my_math
import my_iter


def build_path_sets(graph):
    """ Builds all possible sets of odd node pairs. """
    odd_nodes = gr.find_odd_nodes(graph)
    combos = list(itertools.combinations(sorted(odd_nodes), 2))
    no_of_pairs = len(odd_nodes) / 2

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
    return sets

def find_set_cost(path_set, graph):
    """ Find the cost and route for each path in a set of path options. """
    return {path: dijkstra.find_cost(path, graph) for path in path_set}

def find_set_solutions(path_sets, graph):
    """ Return path and cost for all paths in the path sets. """
    set_solutions = [find_set_cost(path_set, graph) for path_set in path_sets]

    set_costs = [sum(v[0] for v in paths.values()) for paths in set_solutions]

    set_routes = [list(v[1] for v in paths.values()) for paths in set_solutions]

    return set_routes, set_costs

def find_minimum_path_set(path_sets, set_routes, set_costs):
    """ Find the cheapest of all the path set solutions. """
    min_cost = min(set_costs)
    min_set = path_sets[set_costs.index(min_cost)]
    min_route = set_routes[set_costs.index(min_cost)]
    return min_route

def add_new_edges(graph, min_route):
    """ Return new graph w/ new edges extracted from minimum route. """
    new_edges = []
    for node in min_route:
        for i in range(len(node) - 1):
            edge = node[i] + node[i + 1]
            cost = gr.edge_cost(edge, graph)  # Look up existing edge cost
            new_edges.append((edge, cost))  # Append new edges
    return graph + new_edges

def make_eularian(graph):
    """ Add necessary paths to the graph such that it becomes Eularian. """

    path_sets = build_path_sets(graph)  # Get all possible added path sets

    set_routes, set_costs = find_set_solutions(path_sets, graph)

    min_route = find_minimum_path_set(path_sets, set_routes, set_costs)

    new_graph = add_new_edges(graph, min_route)  # Add our new edges

    return new_graph

def main():
    graph = [  # Eularian
        ('AB', 4),
        ('AC', 3),
        ('AD', 5),
        ('BC', 3),
        ('CD', 5),
    ]
    graph = [  # Non-Eularian
        ('AB', 4),
        ('AC', 3),
        ('AE', 10),
        ('BC', 2),
        ('BD', 3),
        ('CD', 3),
        ('DE', 9),
    ]
    graph = [
        ('AB', 8),
        ('AE', 4),
        ('AH', 3),
        ('BC', 9),
        ('BG', 6),
        ('CD', 5),
        ('CF', 3),
        ('DE', 5),
        ('DF', 1),
        ('EF', 2),
        ('EG', 3),
        ('GH', 1),
    ]
    graph = [
        ('AB', 4),
        ('BC', 3),
        ('CD', 2),
        ('BD', 3),
        ('ED', 2),
        ('DA', 3),
    ]

    from data import golf, north
    graph = golf
    graph = north

    if not gr.is_eularian(graph):
        print('Converting to Eularian path...')
        graph = make_eularian(graph)
        print('\t... done')

    print('Attempting to solve Eularian Circuit...')
    route, attempts = eularian.eularian_path(graph, start='A')
    print('\t... done')
    if not route:
        print('\nGave up after {} attempts.'.format(attempts))
    else:
        print('\nSolved in {} attempts:\n{}'.format(attempts, route))

if __name__ == '__main__':
    main()

