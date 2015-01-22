import itertools
import random


import eularian
import graph as gr
import my_math


def flatten_tuples(iterable):
    """
    Flatten an iterable containing several tuples.

    Sum all tuples, which "extends" them, with empty tuple as start value.

    """
    return sum(iterable, ())

def all_unique(iterable):
    """ Returns True if all items in an iterable are unique. """
    seen = set()
    return not any (i in seen or seen.add(i) for i in iterable)

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

def find_set_cost(path_set, graph):
    """ Find the cost and route for each path in a set of path options. """
    return {path: find_cost(path, graph) for path in path_set}

def make_eularian(graph):
    """ Add necessary paths to the graph such that it becomes Eularian. """

    # First build all possible additional odd node edge combos
    odd_nodes = eularian.find_odd_nodes(graph)
    combos = list(itertools.combinations(sorted(odd_nodes), 2))
    print('Combos: {}'.format(list(combos)))
    no_of_sets = len(odd_nodes) / 2

    path_sets = [path_set for path_set in \
                 itertools.combinations(combos, no_of_sets) \
                 if all_unique(flatten_tuples(path_set))]
    print('Possible pairs B: {}'.format(path_sets))

    # Now find the costs of all these sets of paths
    set_solutions = [find_set_cost(path_set, graph) for path_set in path_sets]
    print('Solutions: {}'.format(set_solutions))
    
    set_costs = [sum(v[0] for v in paths.values()) for paths in set_solutions]
    print('Set costs: {}'.format(set_costs))
    
    set_routes = [list(v[1] for v in paths.values()) for paths in set_solutions]
    print('Set routes: {}'.format(set_routes))

    # Now find the shortest distances from node to node for each pair
    min_cost = min(set_costs)
    print('Min cost: {}'.format(min_cost))
    min_set = path_sets[set_costs.index(min_cost)]
    print('Min path set: {}'.format(min_set))
    min_route = set_routes[set_costs.index(min_cost)]
    print('Min path routes: {}'.format(min_route))

    # Now we modify our graph so that it contains the new edges
    new_edges = []
    costs = []
    for path in min_route:
        for i in len(path) - 1:
            edge = path[i] + path[i + 1]
            cost = edge_cost(edge, graph))  # Look up that edge cost
            # This obviously won't work, since graph is a dictionary!
            # TODO: Turn new_graph into a list
            new_graph[edge] = cost
        
    new_graph = graph
    return new_graph

def main():
    graph = {  # Eularian
        'AB': 4,
        'AC': 3,
        'AD': 5,
        'BC': 3,
        'CD': 5,
    }
    graph = {  # Non-Eularian
        'AB': 4,
        'AC': 3,
        'AE': 10,
        'BC': 2,
        'BD': 3,
        'CD': 3,
        'DE': 9,
    }
    graph = {
        'AB': 8,
        'AE': 4,
        'AH': 3,
        'BC': 9,
        'BG': 6,
        'CD': 5,
        'CF': 3,
        'DE': 5,
        'DF': 1,
        'EF': 2,
        'EG': 3,
        'GH': 1,
    }

    if not eularian.is_eularian(graph):
        graph = make_eularian(graph)

    route, attempts = eularian.eularian_path(graph)
    if not route:
        print('{} attempts: No solution found'.format(attempts))
    else:
        print('{} attempts: Solution: {}'.format(attempts, route))

if __name__ == '__main__':
    main()

