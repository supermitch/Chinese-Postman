import my_math

class Graph(object):
    """ Abstract representation of a graph. """

    def __init__(self, data=None):
        self.edges = {}
        if data:
            self.add_edges(data)

    def __repr__(self):
        return 'Graph({})'.format(str(self.edges))

    def add_edges(self, edges):
        """ Add a list of edges. """
        for edge in edges:
            self.add_edge(*edge)

    def add_edge(self, *args):
        """ Adds an Edge to our graph. """
        self.edges[len(self.edges)] = Edge(*args)

    def remove_edges(self, edges):
        """ Removes a list of edges. """
        for edge in edges:
            self.remove_edge(*edge)

    def remove_edge(self, *args):
        """ Remove an edge, plus node if it's disconnected. """
        matches = self.find_edge(*args)
        for key in matches.keys():
            del self.edges[key]

    @property
    def nodes(self):
        return set([node for edge in self.edges.values() \
                    for node in (edge.head, edge.tail)])
    @property
    def node_keys(self):
        """ Return a list of all node keys in this graph. """
        return sorted(self.nodes)

    @property
    def node_orders(self):
        """ Return how many connections a node has. """
        return {x: len(self.edge_options(x)) for x in self.nodes}

    @property
    def odd_nodes(self):
        """ Return a list of odd nodes only. """
        return [k for k in self.nodes if not \
                my_math.is_even(self.node_orders[k])]

    def node_options(self, node):
        """ Returns a list of (node, cost) tuples connected. """
        options = []
        for edge in self.edges.values():
            if edge.head == node:
                options.append(edge.tail)
            elif edge.tail == node:
                options.append(edge.head)
        return sorted(options)

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
        return list(self.edges.values())

    def find_edge(self, head, tail, cost=None, directed=None):
        """
        Returns a dictionary of matching edges.

        Of the given parameters, `cost` and `directed` are optional.
        """
        results = {}
        for key, edge in self.edges.items():
            if not cost and not directed:
                if (head, tail) == (edge.head, edge.tail) or \
                   (tail, head) == (edge.head, edge.tail):
                    results[key] = edge
            elif not directed:
                if (head, tail, cost) == edge or \
                   (tail, head, cost) == edge:
                    results[key] = edge
            else:
                if directed and (head, tail, cost, directed) == edge:
                    results[key] = edge
                elif (tail, head, cost, directed) == edge:
                    results[key] = edge
        return results

    def edge_options(self, node):
        """ Return available edges for a given node. """
        return [x for x in self.edges.values() if node in (x.head, x.tail)]

    def edge_cost(self, *args):
        """ Search for this edge. """
        weight = min([edge.weight for edge in self.find_edge(*args).values() if edge.weight])
        return weight

    @property
    def total_cost(self):
        """ Return the total cost of this graph. """
        return sum(x.weight for x in self.edges.values() if x.weight)

    def is_bridge(self, edge):
        """ Determine if edge is a bridge. """
        return True

    def __len__(self):
        return len(self.edges)


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

    def __eq__(self, other):
        if len(other) == 3:
            other = other + (False,)  # Assume undirected
        return (self.head, self.tail, self.weight, self.directed) == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return 'Edge({}, {}, {}, {})'.format(self.head, self.tail,
                                             self.weight, self.directed)

    def __len__(self):
        """ How many attribs we have. Kinda weird... """
        return len([x for x in \
            (self.head, self.tail, self.weight, self.directed) \
            if x is not None])

    def end(self, node):
        """ Find the opposite end of this edge, given a node. """
        if node == self.head:
            return self.tail
        elif node == self.tail:
            return self.head
        else:
            raise ValueError('Node ({}) not in edge ({})'.format(node, self))

    @property
    def contents(self):
        """ A tuple containing edge contents. """
        return (self.head, self.tail, self.weight, self.directed)

if __name__ == '__main__':
    import tests.run_tests
    tests.run_tests.run(['network'])

