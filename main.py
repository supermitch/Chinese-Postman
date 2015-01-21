import itertools
import random


import eularian
import graph as gr
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
    return sum(find_cost(path, graph)[0] for path in path_set)

def find_shortest_path(node_costs, previous_nodes):
    """ Summarize results of Dijkstras, return shortest path. """
    return 1, ['A', 'B', 'C', 'D']

def find_cost(path, graph):
    """ Return minimum cost from start to end nodes, using Dijkstra's. """
    start, end = path
    print('path: {}{}'.format(start, end))

    all_nodes = gr.find_nodes(graph)
    unvisited = set(all_nodes)
    # Initialize all nodes to total graph cost, at least
    node_costs = {node: gr.find_total_cost(graph) for node in all_nodes}
    node_costs[start] = 0

    previous_nodes = {node: None for node in all_nodes}

    node = start
    while unvisited:  # While we still have unvisited nodes
        for option in gr.find_possible_paths(node, graph):
            next_node = option.strip(node)
            if next_node not in unvisited:
                continue  # Don't go backwards
            cost = gr.edge_cost(option, graph)
            if node_costs[next_node] > node_costs[node] + cost:
                node_costs[next_node] = node_costs[node] + cost
                previous_nodes[next_node] = node
        unvisited.remove(node)
        # Next node must be closest unvisited node:
        options = {k:v for k, v in node_costs.items() if k in unvisited}
        try:
            node = min(options, key=options.get)
        except ValueError:  # arg is empty sequence
            break
        if node == end:
            break

    print('node_costs: {}'.format(node_costs))
    print('previous_nodes: {}'.format(previous_nodes))

    return find_shortest_path(node_costs, previous_nodes)

def make_eularian(graph):
    """ Add necessary paths to the graph such that it becomes Eularian. """

    odd_nodes = eularian.find_odd_nodes(graph)
    combos = list(itertools.combinations(sorted(odd_nodes), 2))
    print('Combos: {}'.format(list(combos)))
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

