# Chinese-Postman Solver

I wrote this program to solve the
[Chinese Postman problem](http://en.wikipedia.org/wiki/Route_inspection_problem).

The solution is roughly a three-step process:

1. Determine if the graph has an [Eularian Path](http://en.wikipedia.org/wiki/Eulerian_path)
    (Very easy)
2. Make the non-Eularian graph Eularian, at the minimum expense
    (Not so easy)
3. Find the fudged Eularian path
    (Pretty easy)

## To run

    python main.py

## Inspiration

I was inspired to learn about and solve this problem when I thought it would
be cool to follow every trail in
[Pacific Spirit Park](http://en.wikipedia.org/wiki/Pacific_Spirit_Regional_Park)
in one run.

Given that the park contains over 73 km of trail, I need to find the optimum
Eularian Path. Otherwise it's going to be a really, really long run!

