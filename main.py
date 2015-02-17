#!/usr/bin/env python3
"""
Solve the Chinese-Postman problem.

For a given graph, determine the minimum amount of backtracking
required to complete an Eularian circuit.

"""
import argparse
import sys

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
    """ Make it so. """

    edges = None
    graph_name = setup_args()
    try:
        edges = getattr(data.data, graph_name)
    except AttributeError:
        print('\nInvalid graph name. Available graphs:\n\t{}\n'.format(
            '\n\t'.join([x for x in dir(data.data)
            if not x.startswith('__')])))
        sys.exit()

    original_graph = network.Graph(edges)

    print('Original:\n')
    print(original_graph)
    print('Original graph has {} edges'.format(len(original_graph)))
    if not original_graph.is_eularian:
        print('Converting to Eularian path...')
        graph, min_cost = eularian.make_eularian(original_graph)
        print('\tAdded {} edges'.format(len(graph) - len(original_graph)))
        print('\tAdded cost is {}'.format(min_cost))
        print('\tTotal cost is {}'.format(graph.total_cost))
    else:
        graph = original_graph
    print('\nEularian:')
    print(graph)
    print('Attempting to solve Eularian Circuit...')
    route, attempts = eularian.eularian_path(graph, start=1)
    if not route:
        print('\tGave up after {} attempts.'.format(attempts))
    else:
        print('\tSolved in {} attempts:\n{}'.format(attempts, route))
        print('\t({} edges)'.format(len(route) - 1))

if __name__ == '__main__':
    main()

