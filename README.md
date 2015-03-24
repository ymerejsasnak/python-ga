# python-ga
first python project: simple genetic algorithm


###next todo:

* apply evolution using fitness ratings: each new robot has 2 parents (pick 15 random ones and choose the 1 with highest rating, then do again)...pick a random point (0 - 162) in the gene list to 'crossover' each parent's genes (first x from one, with rest from the other)...make 2 children from these parents (using SAME resultant genes or do crossover twice?  probably latter...)  each child's genes are subject to random mutation (set action replaced by a random action) but I will have to figure out the randomness of this...  ...Keep going until there is a new generation of 200 child robots

* repeat this for 1000 generations and compare original ratings (say avg and max?) with 1000th decendents ratings


###and then, eventually.... (in future...have to move on from this for now to learn more practical things, sadly...)

* add way to interact with the program to make own adjustments (number of generations, number of actions per robot, etc)

* add lots of optional (so as not to overwhelm) statistics/info printouts

* add graphics capability eventually?  play 1 random original vs 1 random 1000th child for animated comparison 

* maybe after learning more python web stuff make it more of a web app and give it a simple html/css/js UI