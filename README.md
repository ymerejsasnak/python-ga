# python-ga
first python project: simple genetic algorithm


###next todo:

* next implement function/method to actually have a robot follow the strategy laid out in the table (must detect items, wall collisions, etc)  (for now have it perform 200 actions)

* will need a view object or function or something for above, to tell state of current neighborhood -- it gets passed as key to table to lookup action

* calculate fitness rating (how to score them?!?! she doesn't mention how she does this in the book(?) so I will have to figure out my own...)


###and then, moving on:

* run search for 200 originals

* apply evolution using fitness ratings(see book for details)

* repeat this for 1000 generations and compare original ratings with 1000th decendents ratings


###and then, eventually....

* add way to interact with the program to make own adjustments (number of generations, number of actions per robot, etc)

* add lots of statistics/info printouts

* add graphics capability eventually?  play 1 random original vs 1 random 1000th child for animated comparison (at least use curses for SOME visual?)

* maybe after learning more python web stuff make it more of a web app and give it a simple html/css/js UI


###also:

* make comments more thorough and CLEAR!

