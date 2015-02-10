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
        self.nodes[start].add_connection(end, cost)
        if end not in self.nodes:
            self.add_node(end)
        if not directed:
            self.nodes[end].add_connection(start, cost)

    def add_node(self, key):
        """ Add an unconnected node. """
        self.nodes[key] = Node(key)

    def all_nodes(self):
        """ Return a list of all node keys in this graph. """
        #return [x for x in sorted(self.nodes)]
        return sorted(self.nodes.keys())

    def odd_nodes(self):
        """ Return a list of odd nodes only. """
        return [x for x in self.nodes.values() if my_math.is_even(x.order)]

    def node_options(self, node):
        """ Returns a list of (node, cost) tuples connected. """
        return sorted(self.nodes[node].connections)

    @property
    def is_eularian(self):
        """ Return True if all nodes are of even order. """
        return len(self.odd_nodes()) == 0

    @property
    def is_semi_eularian(self):
        """ Return True if exactly 2 nodes are odd. """
        return len(self.odd_nodes) == 2

    @property
    def all_edges(self):
        """ Returns a list of all edges in this graph. """
        edges = []
        for start, node in self.nodes.items():
            for end, cost in node.connections:
                if (start, end, cost) not in edges and \
                    (end, start, cost) not in edges:
                    edges.append((start, end, cost))
        return edges

    def edge_cost(self, start, end):
        """ Search for this edge. """
        for tail, cost in self.nodes[start].connections:
            if tail == end:
                return cost
        for start, cost in self.nodes[end].connections:
            if start == end:
                return cost
        raise ValueError('Edge not found.')

    def __len__(self):
        return len(self.nodes)


class Node(object):
    """ A representation of a vertex in a graph. """

    def __init__(self, key):
        self.key = key
        self.connections = []  # List of (node, cost) tuples

    def add_connection(self, node, cost):
        self.connections.append((node, cost))

    @property
    def order(self):
        """ The number of connections this node has. """
        return len(self.connections)


if __name__ == '__main__':
    import tests.run_tests
    tests.run_tests.run(['network'])

