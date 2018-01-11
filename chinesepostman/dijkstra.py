""" Minimum Cost Path solver using Dijkstra's Algorithm. """

def summarize_path(end, previous_nodes):
    """
    Summarize a chain of previous nodes and return path.

    Chain is a dictionary linked list, e.g. {1: None, 2:1, 3:None, 4:2}
    returns [1, 2, 4] for end = 4.
    """
    route = []
    prev = end
    while prev:
        route.insert(0, prev)  # At beginning
        prev = previous_nodes[prev]
    return route


def find_cost(path, graph):
    """
    Return minimum cost and route from start to end nodes.

    Uses Dijkstra's algorithm to find shortest path.
    """
    start, end = path

    all_nodes = graph.node_keys
    unvisited = set(all_nodes)
    # Initialize all nodes to total graph cost (at least)
    total_cost = graph.total_cost
    node_costs = {node: total_cost for node in all_nodes}
    node_costs[start] = 0  # Start has zero cost

    previous_nodes = {node: None for node in all_nodes}

    node = start
    while unvisited:  # While we still have unvisited nodes
        for option in graph.edge_options(node).values():
            next_node = option.end(node)
            if next_node not in unvisited:
                continue  # Don't go backwards
            # If this path was cheaper than the prior cost, update it
            if node_costs[next_node] > node_costs[node] + option.weight:
                node_costs[next_node] = node_costs[node] + option.weight
                previous_nodes[next_node] = node
        unvisited.remove(node)
        # Next node must be closest unvisited node:
        options = {k:v for k, v in node_costs.items() if k in unvisited}
        try:
            # Find key of minimum value in a dictionary
            node = min(options, key=options.get)  # Get nearest new node
        except ValueError:  # arg is empty sequence, aka dead ended
            break
        if node == end:  # Since we're pathfinding, we can exit early
            break

    cost = node_costs[end]
    shortest_path = summarize_path(end, previous_nodes)

    return cost, shortest_path


if __name__ == '__main__':
    import tests.run_tests
    tests.run_tests.run(['dijkstra'])
