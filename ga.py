import random
from operator import attrgetter


class Robot:

    def __init__(self, parent1=[], parent2=[]):
        #initialize each robot with position and randomized instructions
        #(162 but some are not actually possible)
        #0-north, 1-south, 2-east,3-west,4-pick up,5-do nothing, 6-random move
        #encoding: each current or adjacent space has 3 possible states:
        #is empty, has item, or is a wall....make each possible combination
        #a tuple of five numbers (0 empty, 1 item, 2 wall) in n/e/w/s/c order
        #(ie north, east, west, south, and current) -- and use as key in dict
        #to lookup action to take (0-6)

        #start robot in top left corner (does it matter where really?)
        self.x = 0
        self.y = 0
        self.session_score = 0
        self.all_scores = None
        self.fitness = None  # overall fitness based on averaged scores

        if parent1 == [] and parent2 == []:
            #ie, has no parents...is an original (totally random) robot
            self.genes = []
            for g in range(162):
                self.genes.append(random.randrange(7))
        else:
            split = random.randrange(162)
            self.genes = parent1[:split] + parent2[split:]
            #and add mutations:
            #1 in 10 chance 1 item in genes will be randomized
            #(number is just guess at what may or may not be effective)
            if random.randrange(5) == 0:
                self.genes[random.randrange(162)] = random.randrange(7)

    def __str__(self):
        return ' '.join(map(str, self.genes)) + '\n'

    def move(self, grid, table):
        #use situation variable to lookup action,
        #then take action (checking for wall collisions)
        #hit wall -5 points, pick up item +10 points,
        #try to pick up but nothing there -1 points

        situation = grid.get_situation(self.x, self.y)
        action = self.genes[table.lookup[situation]]

        #check for random action first to reassign action number
        if action == 6:
            action == random.randrange(6)

        #moves
        if action == 0:
            if self.y > 0:
                self.y -= 1
            else:
                self.session_score -= 5
        elif action == 1:
            if self.y < 9:
                self.y += 1
            else:
                self.session_score -= 5
        elif action == 2:
            if self.x < 9:
                self.x += 1
            else:
                self.session_score -= 5
        elif action == 3:
            if self.x > 0:
                self.x -= 1
            else:
                self.session_score -= 5
        #pickup
        elif action == 4:
            if situation[4]:
                self.session_score += 10
                #and remove item from spot:
                grid.grid[(self.x, self.y)] = False
            else:
                self.session_score -= 1

        return action


class Situation_Table:

    #give each unique situation its own numeric value which
    #corresponds to the an index in the robot's action list (genes)
    #c (current) is only 1 or 2 since robot can't BE on a wall

    def __init__(self):
        self.lookup = {}
        index = 0
        for n in range(3):
            for e in range(3):
                for w in range(3):
                    for s in range(3):
                        for c in range(2):
                            self.lookup[(n, e, w, s, c)] = index
                            index += 1


class Grid:

    def __init__(self):
        #create 10x10 grid with 50 percent chance of any
        #cell containing an item for the robot to pick up'''

        self.grid = {}
        for y in range(10):
            for x in range(10):
                if random.randrange(2) == 1:
                    self.grid[(x, y)] = True
                else:
                    self.grid[(x, y)] = False

    def __str__(self):
        msgs = []
        for y in range(10):
            msg = ''
            for x in range(10):
                msg += str(int(self.grid[(x, y)])) + ' '
                msgs.append(msg)

        return '\n'.join(msgs) + '\n'

    def get_situation(self, x, y):
        #remember: 0 empty, 1 item, 2 wall  in n/e/w/s/c order
        situation = []
        if y == 0:
            situation.append(2)
        else:
            situation.append(self.grid[(x, y - 1)])

        if x == 9:
            situation.append(2)
        else:
            situation.append(self.grid[(x + 1, y)])

        if x == 0:
            situation.append(2)
        else:
            situation.append(self.grid[(x - 1, y)])

        if y == 9:
            situation.append(2)
        else:
            situation.append(self.grid[(x, y + 1)])

        situation.append(self.grid[(x, y)])

        return tuple(situation)


class GA_Control:

    def __init__(self):
        #'constants' for how many of each to do
        #note: in book pop is 200, generations is 1000, sessions 100, moves 200
        #but I cut it down because the code (at least as written)
        #would take about four hours (I think??) to run otherwise
        #**but note: based on graph in book,
        #significant improvements seen in population
        #after only about 200 - 300 generations
        #**and of course the question remains:
        #how might I optimize this if at all?
        self.POPULATION = 200
        self.GENERATIONS = 1000
        self.SESSIONS = 100
        self.MOVES = 200

        #create lookup table
        self.table = Situation_Table()
        #create 200 randomized robots to start with
        self.robots = []
        for x in range(self.POPULATION):
            self.robots.append(Robot())

    def run_sessions(self):

        #--each robot...
        for r in self.robots:
            r.all_scores = []

            #--performs 100 sessions...
            for s in range(self.SESSIONS):
                self.grid = Grid()   # new layout each time
                r.session_score = 0

                #--making 200 moves each time...
                for m in range(self.MOVES):
                    r.move(self.grid, self.table)

                r.all_scores.append(r.session_score)

            #average those 100 scores to get fitness rating
            r.fitness = sum(r.all_scores) / self.SESSIONS

    def next_generation(self):
        new_robots = []
        for r in range(self.POPULATION):
            #for each parent randomly pick 15 robots,
            #then use the one of those with max fitness value
            parent1 = max(random.sample(self.robots, 15),
                          key=attrgetter('fitness'))
            parent2 = max(random.sample(self.robots, 15),
                          key=attrgetter('fitness'))
            #then use them twice (to make 2 children)
            new_robots.append(Robot(parent1.genes, parent2.genes))
            new_robots.append(Robot(parent1.genes, parent2.genes))
        self.robots = new_robots


ga = GA_Control()

for i in range(ga.GENERATIONS):
    ga.run_sessions()
    print ("Generation " + str(i) + " best fitness rating: " +
           str(max(ga.robots, key=attrgetter('fitness')).fitness))
    #print average fitness per gen here too?
    ga.next_generation()
