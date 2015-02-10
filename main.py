#!/usr/bin/env python3
"""
Solve the Chinese-Postman problem.

For a given graph, determine the minimum amount of backtracking
required to complete an Eularian circuit.

"""
import argparse

import data.data
import eularian
import network

def setup_args():
    """ Setup argparse to take graph name argument. """
    parser = argparse.ArgumentParser(description='Find an Eularian Cicruit.')
    parser.add_argument('graph', nargs='?', help='Name of graph to load')
    args = parser.parse_args()
    return args.graph

def main():
    data = [  # Eularian
        (1, 2, 4),
        (1, 3, 3),
        (1, 4, 5),
        (2, 3, 3),
        (3, 4, 5),
    ]
    data = [  # Non-Eularian
        (1, 2, 4),
        (1, 3, 3),
        (1, 5, 10),
        (2, 3, 2),
        (2, 4, 3),
        (3, 4, 3),
        (4, 5, 9),
    ]
    data = [
        (1, 2, 4),
        (2, 3, 3),
        (3, 4, 2),
        (2, 4, 3),
        (5, 4, 2),
        (4, 1, 3),
    ]
    graph_name = setup_args()
    try:
        data = getattr(data.data, data_name)
    except AttributeError:
        print('\tInvalid graph name, using default.')
    except TypeError:
        pass  # None is ok, use default

    graph = network.Graph(data)
    if not graph.is_eularian:
        print('Converting to Eularian path...')
        graph, min_cost = eularian.make_eularian(graph)
        print('\tAdded cost is {}'.format(min_cost))
        print('\tTotal cost is {}'.format(graph.total_cost))

    print('Attempting to solve Eularian Circuit...')
    route, attempts = eularian.eularian_path(graph, start=1)
    if not route:
        print('\tGave up after {} attempts.'.format(attempts))
    else:
        print('\tSolved in {} attempts:\n{}'.format(attempts, route))

if __name__ == '__main__':
    main()

