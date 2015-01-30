"""
Solve the Chinese-Postman problem.

For a given graph, determine the minimum amount of backtracking
required to complete an Eularian circuit.

"""
import data.data
import eularian
import graph as gr

def main():
    graph = [  # Eularian
        ('AB', 4),
        ('AC', 3),
        ('AD', 5),
        ('BC', 3),
        ('CD', 5),
    ]
    graph = [  # Non-Eularian
        ('AB', 4),
        ('AC', 3),
        ('AE', 10),
        ('BC', 2),
        ('BD', 3),
        ('CD', 3),
        ('DE', 9),
    ]
    graph = [
        ('AB', 8),
        ('AE', 4),
        ('AH', 3),
        ('BC', 9),
        ('BG', 6),
        ('CD', 5),
        ('CF', 3),
        ('DE', 5),
        ('DF', 1),
        ('EF', 2),
        ('EG', 3),
        ('GH', 1),
    ]
    graph = [
        ('AB', 4),
        ('BC', 3),
        ('CD', 2),
        ('BD', 3),
        ('ED', 2),
        ('DA', 3),
    ]

    graph = data.data.golf
    #graph = data.data.north

    if not gr.is_eularian(graph):
        print('Converting to Eularian path...')
        graph = eularian.make_eularian(graph)
        print('\t... done')

    print('Attempting to solve Eularian Circuit...')
    route, attempts = eularian.eularian_path(graph, start='A')
    print('\t... done')
    if not route:
        print('\nGave up after {} attempts.'.format(attempts))
    else:
        print('\nSolved in {} attempts:\n{}'.format(attempts, route))

if __name__ == '__main__':
    main()

