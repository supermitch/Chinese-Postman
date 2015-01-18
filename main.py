import itertools
import random

import eularian
import my_math

def find_set_cost(path_set, graph):
    """ Find the total cost of a set of path options. """
    return sum(find_cost(path, graph) for path in path_set)

def find_cost(path, graph):
    """ Return minimum cost from start to end nodes. """
    start, end = path
    print('path: {}{}'.format(start, end))
    # Implement Dijkstra's
    return 1

def make_eularian(graph):
    odd_nodes = eularian.find_odd_nodes(graph)
    print('Odd nodes: {}'.format(odd_nodes))
    combos = list(itertools.combinations(sorted(odd_nodes), 2))
    print('Combos: {}'.format(list(combos)))
    # TODO: This doesn't really work for sets of more than 2! Fix it.
    # It sucks anyway.
    path_sets = [pair for pair in itertools.combinations(combos, 2) if \
             pair[0][0] not in pair[1] and pair[0][1] not in pair[1]]
    print('Possible pairs: {}'.format(list(path_sets)))
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

    if not eularian.is_eularian(graph):
        graph = make_eularian(graph)

    route, attempts = eularian.eularian_path(graph)
    if not route:
        print('{} attempts: No solution found'.format(attempts))
    else:
        print('{} attempts: Solution: {}'.format(attempts, route))

if __name__ == '__main__':
    main()

