"""
Functions relating to Eularian graphs.

This module contains functions relating to the identification
and solution of Eularian trails and Circuits.

"""
import copy
import random

import graph as gr
import my_math

def fleury_walk(graph, start=None, circuit=False):
    """
    Return an attempt at walking the edges of a graph.

    Tries to walk a Circuit by making random edge choices. If the route
    dead-ends, returns the route up to that point. Does not revisit
    edges.

    If circuit is True, route must start & end at the same node.

    """
    unvisited = gr.all_edges(graph)

    # Begin at a random node unless start is specified
    node = start if start else random.choice(tuple(gr.all_nodes(graph)))

    route = []
    while unvisited:
        # Fleury's algorith tells us to preferentially select non-bridges
        options = [x for x in gr.find_possible_paths(node, graph) \
                   if x in unvisited]
        bridges = [x for x in options if gr.is_bridge(x, graph, unvisited)]
        non_bridges = [x for x in options if x not in bridges]
        if non_bridges:
            chosen_path = random.choice(non_bridges)
        elif bridges:
            chosen_path = random.choice(bridges)
        else:
            break  # Reached a dead-end, no path options
        next_node = gr.end_node(node, chosen_path)  # The other end
        unvisited.remove(chosen_path)  # Never revisit this edge
        route.append('{}{}'.format(node, next_node))
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
        if len(route) == len(graph):  # We visited every edge
            return route, i
    return [], i  # Never found a solution


def main():
    """ Run a test on a known Eularian graph. """
    graph = [  # Eularian
        ('AB', 4),
        ('AC', 3),
        ('AD', 5),
        ('BC', 3),
        ('CD', 5),
    ]
    if gr.is_semi_eularian(graph):
        print('Graph: {}'.format(graph))
        print('Graph is semi-Eularian')
        route, attempts = eularian_path(graph, start='A')
        print('Solution in {} attempts: {}'.format(attempts, route))
    else:
        print('Non-Eularian graph, cannot solve.')

if __name__ == '__main__':
    main()

