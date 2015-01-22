import graph as gr

def find_shortest_path(end, previous_nodes):
    """ Summarize results of Dijkstras, return shortest path. """
    route = []
    prev = end
    while prev:
        route.insert(0, prev)  # At beginning
        prev = previous_nodes[prev]
    return route

def find_cost(path, graph):
    """ Return minimum cost from start to end nodes, using Dijkstra's. """
    start, end = path

    all_nodes = gr.find_nodes(graph)
    unvisited = set(all_nodes)
    # Initialize all nodes to total graph cost (at least)
    node_costs = {node: gr.find_total_cost(graph) for node in all_nodes}
    node_costs[start] = 0  # Start has zero cost

    previous_nodes = {node: None for node in all_nodes}

    node = start
    while unvisited:  # While we still have unvisited nodes
        for option in gr.find_possible_paths(node, graph):
            next_node = option.strip(node)
            if next_node not in unvisited:
                continue  # Don't go backwards
            cost = gr.edge_cost(option, graph)
            if node_costs[next_node] > node_costs[node] + cost:
                node_costs[next_node] = node_costs[node] + cost
                previous_nodes[next_node] = node
        unvisited.remove(node)
        # Next node must be closest unvisited node:
        options = {k:v for k, v in node_costs.items() if k in unvisited}
        try:
            # Find key of minimum value in a dictionary
            node = min(options, key=options.get)
        except ValueError:  # arg is empty sequence, aka dead ended
            break
        if node == end:  # Since we're pathfinding, we can exit early
            break

    print('node_costs: {}'.format(node_costs))
    print('previous_nodes: {}'.format(previous_nodes))

    shortest_path = find_shortest_path(end, previous_nodes)
    cost = node_costs[end]
    print('shortest_path: {}'.format(shortest_path))
    print('node_cost to {}: {}'.format(end, node_costs[end]))

    return cost, shortest_path
