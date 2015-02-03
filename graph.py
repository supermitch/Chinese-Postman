"""
Generalized graph functions.

A graph data structure is a list of (edge, cost) tuples, where edge is a
start-end string of nodes, e.g. ('AB', 5).

"""
import my_math

def total_cost(graph):
    """ Returns the sum of all edge costs. """
    return sum(cost for _, cost in graph)

def all_edges(graph):
    """ Return a list of all edges in the graph. """
    return [edge for edge, _ in graph]

def possible_paths(node, graph):
    """ Return a list of valid next moves if we are at a given node. """
    return [edge for edge, _ in graph if node in edge]

def all_nodes(graph):
    """ Return a set of all nodes in a given graph. """
    return set([node for edge, _ in graph for node in edge])

def odd_nodes(graph):
    """ Return a list of nodes of odd order. """
    return sorted([node for node, order in orders(graph).items() if \
                  not my_math.is_even(order)])

def end_node(node, edge):
    """ Returns the other end of an edge. """
    return edge.strip(node)

def orders(graph):
    """ Return a dictionary of node orders. """
    nodes = all_nodes(graph)
    return {node: len(possible_paths(node, graph)) for node in nodes}

def edge_cost(edge, graph):
    """
    Find the edge cost in the graph, or return None if edge not found.

    Checks both 'AB' and 'BA' (undirected) edge names.

    """
    for e, cost in graph:
        if e in (edge, edge[::-1]):
            return cost
    return None

def is_eularian(graph):
    """ Return True if a graph is Eularian (has zero odd nodes) """
    return not odd_nodes(graph)

def is_semi_eularian(graph):
    """ Return True if a graph is Semi-Eularian (has exactly 2 odd nodes) """
    return len(odd_nodes(graph)) == 2

def is_bridge(edge, graph, segments=None):
    """
    Return True if an edge is a bridge.

    Given a graph and (optional) unvisited segments, utilize depth-first
    search to visit all connected edges. If DFS reaches all unvisited
    segments, then the edge must not be a bridge.

    """
    if segments is None:  # Segments is "unvisited segments"
        segments = all_edges(graph)

    start = edge[1]  # Could start at either end

    stack = []
    visited = set()
    while True:
        if start not in stack:
            stack.append(start)
        visited.add(start)
        edge_options = [x for x in possible_paths(start, graph) \
                        if x in segments]
        adjacent_nodes = sorted([end_node(start, edge) for edge in edge_options])
        node_options = [x for x in adjacent_nodes if x not in visited]
        if node_options:
            start = node_options[0]  # Alphabetical, for now
        else:
            try:
                stack.pop()
                start = stack[-1]  # Go back to the last node
            except IndexError:  # We are back to the beginning
                break
    # Find all the edges that are in our graph (even if disconnected)
    remaining_graph = [edge for edge in graph if edge[0] in segments]

    # If we visited all the edges during our DFS, we must not be disconnected
    if len(visited) == len(all_nodes(remaining_graph)):
        return False
    else:
        return True  # The edge is a bridge

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

