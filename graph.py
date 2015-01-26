"""
Generalized graph functions.

A graph data structure is a list of (edge, cost) tuples, where edge is a
start-end string of nodes, e.g. ('AB', 5).

"""
import random

import my_math

def find_total_cost(graph):
    """ Returns the sum of all edge costs. """
    return sum(cost for _, cost in graph)

def all_edges(graph):
    """ Return a list of all edges in the graph. """
    return [edge for edge, _ in graph]

def find_possible_paths(node, graph):
    """ Return a list of valid next moves if we are at a given node. """
    return [edge for edge, _ in graph if node in edge]

def all_nodes(graph):
    """ Return a set of all nodes in a given graph. """
    return set([node for edge, _ in graph for node in edge])

def find_odd_nodes(graph):
    """ Return a list of nodes of odd order. """
    return [node for node, order in find_orders(graph).items() if \
            not my_math.is_even(order)]

def end_node(node, edge):
    """ Returns the other end of an edge. """
    return edge.strip(node)

def find_orders(graph):
    """ Return a dictionary of node orders. """
    nodes = all_nodes(graph)
    return {node: len(find_possible_paths(node, graph)) for node in nodes}

def edge_cost(edge, graph):
    """
    Find the edge cost in the graph, or return None if edge not found.

    Checks both 'AB' and 'BA' (undirected) edge names.

    """
    for e, cost in graph:
        if e in (edge, edge[::-1]):
            return cost
    return None

def is_bridge(edge, graph, segments=None):
    """
    Return True if an edge is a bridge.

    Given a graph and (optional) unvisited segments.

    """
    print(edge, graph, segments)
    start = random.choice(edge)

    stack = []
    visited = []
    while True:
        stack.append(start)
        visited.append(start)
        edge_options = [x for x in find_possible_paths(start, graph) if x in segments]
        adjacent_nodes = sorted([end_node(start, edge) for edge in options])
        node_options = [x for x in adjacent_nodes if x not in visited]
        if node_options:
            print(next_nodes)
            start = next_nodes[0]  # Alphabetical, for now
        else:
            try:
                start = stack.pop()
            except IndexError:
                break
    # TODO: This is wrong...
    if len(visited) == len(gr.all_nodes(graph)):
        return False
    else:
        return True

    # choose one node on the edge
    # from that node, explore every connected edge, minus
    # removed segments
    # if we visit every edge node in the graph, we
    # are not a bridge
    return False

def main():
    """ Run a test on a known Eularian graph. """
    graph = [  # Eularian
        ('AB', 4),
        ('AC', 3),
        ('AD', 5),
        ('BC', 3),
        ('CD', 5),
    ]
    print('Graph: {}'.format(graph))
    print('Total cost: {}'.format(find_total_cost(graph)))
    print('All nodes: {}'.format(all_nodes(graph)))
    print('Odd nodes: {}'.format(find_odd_nodes(graph)))
    print('All orders: {}'.format(find_orders(graph)))
    print('Possible paths for C: {}'.format(find_possible_paths('C', graph)))
    print('Cost for AB: {}'.format(edge_cost('AB', graph)))

if __name__ == '__main__':
    main()

