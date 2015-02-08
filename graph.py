"""
Generalized graph functions.

A graph data structure is a list of (edge, cost) tuples, where edge is a
start-end string of nodes, e.g. ('AB', 5).

e.g. [('AB', 5), ('BC', 3), ('CA', 2)]

"""
import my_math

class Graph(object):
    """ Abstract representation of a graph. """

    def __init__(self, graph=None):
        self.nodes = {}
        if graph:
            for start, end, cost in graph:
                self.add_edge(start, end, cost)

    def add_edge(self, start, end, cost=0, directed=False):
        """ Adds a Node to our graph and adds node connections. """
        if start not in self.nodes:
            self.add_node(start)
            nodes[start].add_connection(end, cost)
        if end not in self.nodes:
            self.add_node(end)
            if not directed:
                nodes[end].add_connection(start, cost)

    def add_node(self, key):
        self.nodes[key] = Node(key)

    def all_nodes(self):
        """ Return a list of all nodes in this graph. """
        return [x for x in sorted(self.nodes)]

    def odd_nodes(self):
        """ Return a list of odd nodes only. """
        return [x for x in sorted(self.nodes) if my_math.is_even(x.order)]

    def is_eularian(self):
        """ Return True if all nodes are of even order. """
        return len(self.odd_nodes) == 0

    def is_eularian(self):
        """ Return True if exactly 2 nodes are odd. """
        return len(self.odd_nodes) == 2


class Node(object):
    """ A representation of a vertex in a graph. """

    def __init__(self, key):
        self.key = key
        self.connections = {}

    def add_connection(self, key, cost):
        self.connections[key] = cost

    def order(self):
        """ The number of connections this node has. """
        return len(self.connections)

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

def remove_edges(original_graph, edges):
    """
    Remove a list of edges from a graph.

    Works even for reversed edge names, e.g. 'BA' will still match 'AB'.
    Will not remove all edges, if parallel edges exist, unless they are
    listed twice.

    """
    graph = original_graph[:]
    for bad_edge in edges:
        for edge in graph[:]:  # Iterate over a copy
            if edge[0] in (bad_edge, bad_edge[::-1]):
                graph.remove(edge)
                break  # Do not remove same edge twice!
    return graph

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

if __name__ == '__main__':
    import tests.run_tests
    tests.run_tests.run(['graph'])

