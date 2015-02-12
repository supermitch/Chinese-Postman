import my_math

class Graph(object):
    """ Abstract representation of a graph. """

    def __init__(self, data=None):
        self.nodes = set()
        self.edges = {}
        if data:
            self.add_edges(data)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return 'Graph({})'.format(str(self.all_edges))

    def add_edges(self, edges):
        """ Add a list of edges. """
        for edge in edges:
            self.add_edge(*edge)

    def add_edge(self, *args):
        """ Adds an Edge to our graph. """
        self.edges[len(self.edges)] = Edge(*args)
        try:
            self.nodes.add(args[0])
        except IndexError:
            pass
        try:
            self.nodes.add(args[1])
        except IndexError:
            pass

    def remove_edges(self, edges):
        """ Removes a list of edges. """
        for edge in edges:
            self.remove_edge(edge)

    def remove_edge(self, edge):
        """ Remove an edge, plus node if it's disconnected. """
        start, end, cost = edge
        if start in self.nodes:
            node = self.nodes[start]
            if (end, cost) in node.connections:
                node.remove_connection(end, cost)
            if not node.connections:
                del self.nodes[start]  # Remove start node
        if end in self.nodes:
            node = self.nodes[end]
            if (start, cost) in node.connections:
                node.remove_connection(start, cost)
            if not node.connections:
                del self.nodes[end]  # Remove end node

    def add_node(self, key):
        """ Add an unconnected node. """
        self.nodes[key] = Node(key)

    @property
    def node_keys(self):
        """ Return a list of all node keys in this graph. """
        return sorted(self.nodes.keys())

    @property
    def odd_nodes(self):
        """ Return a list of odd nodes only. """
        return [k for k, v in self.nodes.items() \
                if not my_math.is_even(v.order)]

    def node_options(self, node):
        """ Returns a list of (node, cost) tuples connected. """
        return sorted(self.nodes[node].connections)

    @property
    def is_eularian(self):
        """ Return True if all nodes are of even order. """
        return len(self.odd_nodes) == 0

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

    def edge_options(self, start):
        """ Return available edges for a given node. """
        return [(start, end, cost) for end, cost in \
                self.nodes[start].connections]

    def edge_cost(self, start, end):
        """ Search for this edge. """
        # TODO: Parallel edges would have 2 costs, return minimum
        for tail, cost in self.nodes[start].connections:
            if tail == end:
                return cost
        for start, cost in self.nodes[end].connections:
            if start == end:
                return cost
        raise ValueError('Edge not found.')

    @property
    def total_cost(self):
        """ Return the total cost of this graph. """
        return sum(self.edge_cost(h, t) for h, t, _ in self.all_edges)

    def __len__(self):
        return len(self.nodes)


class Edge(object):
    """ A connection between nodes. """
    def __init__(self, *args):
        self.head = None  # Start node
        self.tail = None  # End node
        self.weight = 0  # Cost
        self.directed = False  # Undirected by default
        attrs = ('head', 'tail', 'weight', 'directed')
        for attr, value in zip(attrs, args):
            setattr(self, attr, value)

    def __repr__(self):
        return 'Edge({}, {}, {}, {})'.format(self.head, self.tail,
                                             self.weight, self.directed)

if __name__ == '__main__':
    import tests.run_tests
    tests.run_tests.run(['network'])

