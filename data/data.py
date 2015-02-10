"""
Predefined graphs for testing and experimentation.

"""

square = [  # Eularian, simple square
    (1,2,1), (2,3,1), (3,4,1), (4,1,1)
]

ice_cream = [  # Semi-Eularian, 2 triangles
    (1,2,4), (1,3,3), (1,4,5), (2,3,3), (3,4,5)
]
sailboat = [  # Non-Eularian, 3 triangles
    (1,2,4), (1,3,3), (1,5,10), (2,3,2), (2,4,3), (3,4,3), (4,5,9)
]
kite = [  # Semi-Eularian, 2 triangles w/ a tail
    (1,2,4), (2,3,3), (3,4,2), (2,4,3), (5,4,2), (4,1,3)
]

clover = [  # Eularian, square w/ parallel edges
    (1,2,1), (1,2,2), (2,3,1), (2,3,2), (3,4,1), (3,4,2), (4,1,1), (4,1,2)
]

# North of Chancellor Blvd. (to beaches) graph
north = [
    ('AB', 10), ('BC', 1), ('BD', 10), ('DF', 1), ('DP', 10), ('FE', 1),
    ('FG', 1), ('GH', 5), ('GP', 10), ('HI', 2), ('HJ', 3), ('JK', 2),
    ('IJ', 2), ('IN', 10), ('JL', 10), ('LM', 1), ('LN', 4), ('NO', 1),
    ('NP', 2), ('PQ', 1),
]

# University Blvd. to Chancellor Blvd. (University golf course)
golf = [
    ('AB', 4), ('BC', 3), ('BG', 1), ('CD', 1), ('CE', 6), ('CF', 2),
    ('EF', 7), ('FG', 2), ('FI', 2), ('GH', 9), ('GI', 2), ('IJ', 8),
    ('JK', 1), ('JN', 6), ('KL', 2), ('KM', 7),
]

# Non-Eularian w/ 6 odd nodes
big_six = [
    ('AB', 8), ('AE', 4), ('AH', 3), ('BC', 9), ('BG', 6), ('CD', 5),
    ('CF', 3), ('DE', 5), ('DF', 1), ('EF', 2), ('EG', 3), ('GH', 1),
]

# Full North of University Ave to Beaches
university = [
    ('AB', 4), ('BC', 3), ('CD', 1), ('BF', 1), ('CE', 2), ('CZ', 6),
    ('EG', 2), ('EF', 2), ('EZ', 7), ('FG', 2), ('FH', 9), ('GI', 8),
    ('IJ', 1), ('IM', 7), ('JK', 2), ('JL', 8), ('LM', 4), ('LQ', 10),
    ('MN', 2), ('MP', 10), ('NO', 1), ('NT', 10), ('NW', 10), ('PQ', 2),
    ('PS', 2), ('QR', 2), ('QS', 3), ('ST', 5), ('TU', 1), ('UV', 1),
    ('UW', 1), ('WX', 10), ('XY', 1), ('XZ', 10),
]

