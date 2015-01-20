import graph as gr
import my_math

def find_odd_nodes(graph):
    """ Return a list of nodes of odd order. """
    return [node for node, order in gr.find_orders(graph).items() if \
            not my_math.is_even(order)]

def attempt_eularian_path(graph):
    """
    Returns a Chinese-Postman perfect path, if one can be found.
    
    Randomly tries to solve an Eularian graph.
    
    """
    import random

    segments = set(graph)
    all_nodes = gr.find_nodes(segments)

    current_node = random.choice(list(all_nodes))
    route = []
    while segments:
        options = gr.find_possible_paths(current_node, segments)
        if not options:  # Reached a dead end
            break
        chosen_path = random.choice(options)
        next_node = chosen_path.strip(current_node)  # Get the other node
        segments.discard(chosen_path)  # Remove after traversing
        route.append('{}{}'.format(current_node, next_node))
        current_node = next_node

    return route

def eularian_path(graph):
    """
    Find a path through a Eularian graph.
    
    Function gives up after 1000 tries.
    """
    route = []
    attempts = 0
    while len(route) < len(graph):
        route = attempt_eularian_path(graph)
        attempts += 1
        if attempts == 1000:
            # todo: How do we know we checked all possible solutions?
            route = []
            break  # Can't find a solution?
    return route, attempts

def is_eularian(graph):
    """
    Return True if a graph is Eularian, else False.

    A graph is Eularian if all nodes are even, or only two nodes are odd.

    """
    orders = gr.find_orders(graph) 

    if all(my_math.is_even(x) for x in orders.values()):
        return True 
    else:
        return len(find_odd_nodes(graph)) == 2

def main():
    """ Run a test on a known Eularian graph. """
    graph = {  # Eularian
        'AB': 4,
        'AC': 3,
        'AD': 5,
        'BC': 3,
        'CD': 5,
    }
    if is_eularian(graph):
        print('Graph: {}'.format(graph))
        print('Graph is Eularian')
        route, attempts = eularian_path(graph)
        print('Solution in {} attempts: {}'.format(attempts, route))
    else:
        print('Non-Eularian graph, cannot solve.')

if __name__ == '__main__':
    main()

