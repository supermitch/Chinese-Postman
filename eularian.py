"""
Functions relating to Eularian graphs.

This module contains functions relating to the identification
and solution of Eularian trails and Circuits.

"""
import copy
import random

import graph as gr
import my_math

def random_walk_graph(graph, start=None, circuit=False):
    """
    Return an attempt at walking the edges of a graph.

    Tries to walk a Circuit by making random edge choices. If the route
    dead-ends, returns the route up to that point. Does not revisit
    edges.

    If circuit is True, route must start & end at the same node.

    """
    segments = gr.all_edges(graph)
    if start:
        current_node = start
    else:  # Choose a node at random
        current_node = random.choice(tuple(gr.all_nodes(graph)))

    route = []
    while segments:
        # Fleury's algorith tells us to preferentially select non-bridges
        non_bridges = [x for x in gr.find_possible_paths(current_node, graph) \
                   if x in segments and not gr.is_bridge(x, graph, segments)]
        bridges = [x for x in gr.find_possible_paths(current_node, graph) \
                   if x in segments and gr.is_bridge(x, graph, segments)]
        if non_bridges:
            chosen_path = random.choice(non_bridges)
        elif bridges:
            chosen_path = random.choice(bridges)
        else:
            break  # Reached a dead-end
        next_node = gr.end_node(current_node, chosen_path)  # The other end
        segments.remove(chosen_path)  # Never revisit this edge
        route.append('{}{}'.format(current_node, next_node))
        current_node = next_node

    return route

def eularian_path(graph, start=None, circuit=False):
    """
    Return an Eularian Trail or Eularian Circuit through a graph, if found.

    Return the route if it visits every edge, else give up after 1000 tries.

    If `start` is set, force start at that Node.

    """
    # TODO: How do we know we checked all possible solutions?
    for i in range(1, 1001):
        route = random_walk_graph(graph, start, circuit)
        if len(route) == len(graph):  # We visited every edge
            return route, i
    return [], i

def is_eularian(graph):
    """ Return True if a graph has zero odd nodes. """
    return not gr.find_odd_nodes(graph)

def is_semi_eularian(graph):
    """ Return True if graph has exactly two odd nodes. """
    return len(gr.find_odd_nodes(graph)) == 2

def main():
    """ Run a test on a known Eularian graph. """
    graph = [  # Eularian
        ('AB', 4),
        ('AC', 3),
        ('AD', 5),
        ('BC', 3),
        ('CD', 5),
    ]
    if is_semi_eularian(graph):
        print('Graph: {}'.format(graph))
        print('Graph is semi-Eularian')
        route, attempts = eularian_path(graph, start='A')
        print('Solution in {} attempts: {}'.format(attempts, route))
    else:
        print('Non-Eularian graph, cannot solve.')

if __name__ == '__main__':
    main()

