# Chinese-Postman Solver

I wrote this program to solve the
[Chinese Postman problem](http://en.wikipedia.org/wiki/Route_inspection_problem).

Described as:

> The **Chinese Postman Problem**, or "route inspection problem"
> is to find a shortest closed circuit that visits every edge of a
> (connected) undirected graph.

## Inspiration

I was inspired to learn about and solve this problem when I thought it would
be cool to follow every trail in
[Pacific Spirit Park](http://en.wikipedia.org/wiki/Pacific_Spirit_Regional_Park)
in one run.

Given that the park contains over 73 km of trail, I need to find the optimum
Eularian Path. Otherwise it's going to be a really, really long run!


## The Process

The solution is roughly a three-step process:

1. Determine if the graph has an
[Eularian Path](http://en.wikipedia.org/wiki/Eulerian_path)
    (Very easy)
2. Make the non-Eularian graph Eularian, at the minimum expense
    (Not so easy)
3. Find the fudged Eularian path
    (Pretty easy)

### Solving Minimum Expense

In order to convert a non- or semi-Eularian graph to an Eularian one,
you must eliminate odd nodes (nodes having an odd number of edges.)

To eliminate an odd node, you need to add another edge to it (essentially
retracing your steps.) However, this comes as a cost! The goal then is
to find out which edges to repeat, that eliminate all the odd nodes, with
the minimum cost.

1. Find all possible combinations of pairs of odd nodes
2. Using Dijkstra's Algorithm, find the cost of the minimum path between
those pairs
3. Find which set of paths (depending on how many odd nodes you have)
that results in the least total cost
4. Modify your graph with these new parallel edges

Now you have an Eularian graph with only even nodes, for which an Eularian
Circuit can be found.

### Solving the Eularian Circuit

Solving the Eularian Circuit (now that we have one) is relatively easy. At
first, I simply walked the edges randomly until I happened to find a route
that either dead-ended, or resulted in a circuit. Then I implemented [Fleury's
Algorithm](http://en.wikipedia.org/wiki/Eulerian_path#Fleury.27s_algorithm)
which says always choose a non-bridge over a bridge (for obvious
reasons). Now it takes very few attempts to solve most circuits.

Later I will implement an alternative circuit finding method (Hierholzer's?)

## To run

    python main.py

If you want to specify which graph to load, simply add the graph name:

    python main.py north

You can find all the graph names in the `data` folder.

This program will run in Python 2.7 and Python 3.4, at least.

There are unit tests included, in the `tests` directory. You can run these by
typing

    python tests/run_tests.py

from the root project folder.
