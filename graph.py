"""
Generalized graph functions.

A graph data structure is a list of (edge, cost) tuples, where edge is a
start-end string of nodes, e.g. ('AB', 5).

"""
import my_math

def total_cost(graph):
    """ Returns the sum of all edge costs. """
    return sum(cost for _, cost in graph)

def edge_cost(edge, graph):
    """
    Find the edge cost in the graph, or return None if edge not found.

    Checks both 'AB' and 'BA' (undirected) edge names.

    """
    for e, cost in graph:
        if e in (edge, edge[::-1]):
            return cost
    return None

def all_edges(graph):
    """ Return a list of all edges in the graph. """
    return [edge for edge, _ in graph]

def remove_edges(graph, edges):
    """
    Remove a list of edges from a graph.

    Works even for reversed edge names, e.g. 'BA' will still match 'AB'.

    """
    removed  = [e for edge in edges for e in [edge, edge[::-1]]]
    return [(edge, cost) for edge, cost in graph if edge not in removed]

def edge_options(node, graph):
    """ Return a list of valid next moves if we are at a given node. """
    return [edge for edge, _ in graph if node in edge]

def all_nodes(graph):
    """ Return a set of all nodes in a given graph. """
    return set([node for edge, _ in graph for node in edge])

def odd_nodes(graph):
    """ Return a list of nodes of odd order. """
    return sorted([node for node, order in orders(graph).items() if \
                  not my_math.is_even(order)])

def node_options(node, graph):
    """ Return options for nodes from a given node. """
    return sorted([end_node(node, edge) \
                  for edge in edge_options(node, graph)])

def end_node(node, edge):
    """ Returns the other end of an edge. """
    return edge.strip(node)

def orders(graph):
    """ Return a dictionary of node orders. """
    nodes = all_nodes(graph)
    return {node: len(edge_options(node, graph)) for node in nodes}

def is_eularian(graph):
    """ Return True if a graph is Eularian (has zero odd nodes) """
    return not odd_nodes(graph)

def is_semi_eularian(graph):
    """ Return True if a graph is Semi-Eularian (has exactly 2 odd nodes) """
    return len(odd_nodes(graph)) == 2

def is_bridge(edge, original_graph):
    """
    Return True if an edge is a bridge.

    Given a graph and edge, utilize depth-first search to visit all connected
    edges (minus the given edge). If DFS reaches all unvisited edges, then
    the given edge must not be a bridge.

    """
    graph = remove_edges(original_graph, [edge])  # Don't include given edge

    start = edge[1]  # Start node. Could start at either end.

    stack = []
    visited = set()  # Visited nodes
    while True:
        if start not in stack:
            stack.append(start)
        visited.add(start)
        nodes = [x for x in node_options(start, graph) if x not in visited]
        if nodes:
            start = nodes[0]  # Alphabetical, for now
        else:
            try:
                stack.pop()
                start = stack[-1]  # Go back to the last node
            except IndexError:  # We are back to the beginning
                break

    # If we visited all the nodes during our DFS, we must not be disconnected
    if len(visited) == len(all_nodes(original_graph)):
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
    print('Possible paths for C: {}'.format(find_edge_options('C', graph)))
    print('Cost for AB: {}'.format(edge_cost('AB', graph)))

if __name__ == '__main__':
    main()

