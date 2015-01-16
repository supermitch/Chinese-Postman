import random

def find_possible_paths(node, graph):
    """ Return a list of valid next moves if we are at a given node. """
    return [edge for edge in graph if node in edge]

def find_nodes(graph):
    """ Return all nodes in a given set of edges. """
    return [node for edge in graph for node in edge]

def solve_eularian_path(graph):
    """ Randomly tries to solve an Eularian graph. """
    segments = set(graph)
    all_nodes = set(find_nodes(segments))

    current_node = random.choice(list(all_nodes))
    print('\nstart: {}'.format(current_node))
    route = []
    while segments:
        options = find_possible_paths(current_node, segments)
        if not options:  # Reached a dead end
            print('\t\tBad route...')
            break
        chosen_path = random.choice(options)
        print('chosen: {}'.format(chosen_path))
        next_node = chosen_path.strip(current_node)
        # We discard this edge, once traversed
        segments.discard(chosen_path)
        # e.g. if we started at 'A', and chose segment 'DA', return 'D'
        route.append('{}{}'.format(current_node, next_node))
        current_node = next_node

    print(route)
    return route

def main():
    graph = {
        'AB': 4,
        'AC': 3,
        'AD': 5,
        'BC': 3,
        'CD': 5,
    }

    route = []
    while len(route) < len(graph):
        route = solve_eularian_path(graph)

    print('\nSolution: {}'.format(route))

if __name__ == '__main__':
    main()

