"""
Iterator related helper functions.

"""

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

