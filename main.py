#!/usr/bin/env python3
"""
Solve the Chinese-Postman problem.

For a given graph, determine the minimum amount of backtracking
required to complete an Eularian circuit.

"""
import argparse

import data.data
import eularian
import graph as gr

def setup_args():
    """ Setup argparse to take graph name argument. """
    parser = argparse.ArgumentParser(description='Find an Eularian Cicruit.')
    parser.add_argument('graph', nargs='?', help='Name of graph to load')
    args = parser.parse_args()
    return args.graph

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
        ('AB', 4),
        ('BC', 3),
        ('CD', 2),
        ('BD', 3),
        ('ED', 2),
        ('DA', 3),
    ]
    graph_name = setup_args()
    try:
        graph = getattr(data.data, graph_name)
    except AttributeError:
        print('\tInvalid graph name, using default.')
    except TypeError:
        pass  # None is ok, use default

    if not gr.is_eularian(graph):
        print('Converting to Eularian path...')
        graph, min_cost = eularian.make_eularian(graph)
        print('\tAdded cost is {}'.format(min_cost))
        print('\tTotal cost is {}'.format(gr.total_cost(graph)))

    print('Attempting to solve Eularian Circuit...')
    route, attempts = eularian.eularian_path(graph, start='A')
    if not route:
        print('\tGave up after {} attempts.'.format(attempts))
    else:
        print('\tSolved in {} attempts:\n{}'.format(attempts, route))

if __name__ == '__main__':
    main()

