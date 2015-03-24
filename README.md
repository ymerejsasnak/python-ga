# python-ga
first python project: simple genetic algorithm


###next todo:

* NOTE: first will have to figure out a way to split up tables to they can be combined into childrens' tables (first idea that comes to mind is each situation tuple key (n,e,w,s,c) actually gets a value of an index (0 - 162 or whatever it was) and then have the actual moves for each robot be a list of 162 numbers (0 - 5 or hwatever) and then use the situation as key to lookup the index to then use to lookup the move...seems convoluted, a better way...????)

* apply evolution using fitness ratings(see book for details)

* repeat this for 1000 generations and compare original ratings (say avg and max?) with 1000th decendents ratings (avg and max)


###and then, eventually....

* add way to interact with the program to make own adjustments (number of generations, number of actions per robot, etc)

* add lots of optional (so as not to overwhelm) statistics/info printouts

* add graphics capability eventually?  play 1 random original vs 1 random 1000th child for animated comparison (at least use curses for SOME visual?)

* maybe after learning more python web stuff make it more of a web app and give it a simple html/css/js UI


###also:

* make comments more thorough and CLEAR!

