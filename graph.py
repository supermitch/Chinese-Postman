"""
Generalized graph functions.

"""

def find_total_cost(graph):
    """ Returns the sum of all edge costs. """
    return sum(graph.values())

def find_possible_paths(node, graph):
    """ Return a list of valid next moves if we are at a given node. """
    return [edge for edge in graph if node in edge]

def find_nodes(graph):
    """ Return a set of all nodes in a given graph. """
    return set([node for edge in graph for node in edge])

def find_orders(graph):
    """ Return a dictionary of node orders. """
    nodes = find_nodes(graph)
    return {node: len(find_possible_paths(node, graph)) for node in nodes}

def edge_cost(edge, graph):
    """
    Find the edge cost in the graph.
    
    If neither 'AB' or 'BA' is in the graph, returns None.

    """
    return graph.get(edge, graph.get(edge[::-1], None))

