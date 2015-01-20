import itertools
import random


import eularian
import graph
import my_math


def flatten_tuples(iterable):
    """
    Flatten an iterable containing several tuples.

    Sum all tuples, which "extends" them, with empty tuple as start value.

    """
    return sum(iterable, ())

def all_unique(iterable):
    """ Returns True if all items in an iterable are unique. """
    seen = set()
    return not any (i in seen or seen.add(i) for i in iterable)

def find_set_cost(path_set, graph):
    """ Find the total cost of a set of path options. """
    return sum(find_cost(path, graph) for path in path_set)

def find_cost(path, graph):
    """ Return minimum cost from start to end nodes, using Dijkstra's. """
    start, end = path
    print('path: {}{}'.format(start, end))

    all_nodes = eularian.find_nodes(graph)
    # Initialize all nodes to total graph cost
    node_costs = {node: find_total_cost(graph) for node in all_nodes}

    current_node = start
    visited = set(current_node)
    node_costs[current_node] = 0

    for node in all_nodes:
        for option in find_possible_paths(node, graph):
            next_node = option.strip(node)
            if next_node in visited:
                continue  # Don't go backwards
            cost = gr.edge_cost(edge, graph)
            if node_costs[next_node] > node_costs[node] + cost:
                node_costs[next_node] = node_costs[node] + cost
        visited.add(node)



        

    
    return 1

def make_eularian(graph):
    """ Add necessary paths to the graph such that it becomes Eularian. """

    odd_nodes = eularian.find_odd_nodes(graph)
    combos = list(itertools.combinations(sorted(odd_nodes), 2))
    print('Combos: {}'.format(list(combos)))
    # TODO: This doesn't really work for sets of more than 2! Fix it.
    # It sucks anyway.
    no_of_sets = len(odd_nodes) / 2

    path_sets = [path_set for path_set in \
                 itertools.combinations(combos, no_of_sets) \
                 if all_unique(flatten_tuples(path_set))]
    print('Possible pairs B: {}'.format(path_sets))

    # Now find the shortest distances from node to node for each pair
    costs = [find_set_cost(path_set, graph) for path_set in path_sets]
    print('Costs: {}'.format(list(costs)))

    min_cost = min(costs)
    print('Minimum cost: {}'.format(min_cost))
    optimum_set = path_sets[costs.index(min(costs))]
    print('Optimum path set: {}'.format(optimum_set))

    new_graph = graph
    return new_graph

def main():
    graph = {  # Eularian
        'AB': 4,
        'AC': 3,
        'AD': 5,
        'BC': 3,
        'CD': 5,
    }
    graph = {  # Non-Eularian
        'AB': 4,
        'AC': 3,
        'AE': 10,
        'BC': 2,
        'BD': 3,
        'CD': 3,
        'DE': 9,
    }
    graph = {
        'AB': 8,
        'AE': 4,
        'AH': 3,
        'BC': 9,
        'BG': 6,
        'CD': 5,
        'CF': 3,
        'DE': 5,
        'DF': 1,
        'EF': 2,
        'EG': 3,
        'GH': 1,
    }

    if not eularian.is_eularian(graph):
        graph = make_eularian(graph)

    route, attempts = eularian.eularian_path(graph)
    if not route:
        print('{} attempts: No solution found'.format(attempts))
    else:
        print('{} attempts: Solution: {}'.format(attempts, route))

if __name__ == '__main__':
    main()

