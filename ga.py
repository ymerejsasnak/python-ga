import random


class Robot:

    def __init__(self, parent1=[], parent2=[]):
        #initialize each robot with position and randomized instructions
        #(162 but some are not actually possible)
        #0-north, 1-south, 2-east,3-west,4-pick up,5-random move
        #encoding: each current or adjacent space has 3 possible states:
        #is empty, has item, or is a wall....make each possible combination
        #a tuple of five numbers (0 empty, 1 item, 2 wall) in n/e/w/s/c order
        #(ie north, east, west, south, and current) -- and use as key in dict
        #to lookup action to take (0-5)

        #start robot roughly in the middle instead of 0,0 (does it matter?)
        self.x = 4
        self.y = 5
        self.score = 0  #per session scores
        self.fitness = None  #overall fitness based on averaged scores

        if parent1 == [] and parent2 == []:
            #has no parents...is an original (totally random) robot
            self.genes = []
            for g in range(162):
                self.genes.append(random.randrange(6))
        else:
            #has parents (TODO)
            pass

    def __str__(self):
        return ' '.join(map(str, self.genes)) + '\n'

    def move(self, grid, table):
        #use situation variable to lookup action,
        #then take action (checking for wall collisions)
        #hit wall -5 points, pick up item +10 points,
        #try to pick up but nothing there -1 points

        situation = grid.get_situation(self.x, self.y)
        action = self.genes[table.lookup[situation]]

        #moves
        if action == 0:
            if self.y > 0:
                self.y -= 1
            else:
                self.score -= 10
        elif action == 1:
            if self.y < 9:
                self.y += 1
            else:
                self.score -= 10
        elif action == 2:
            if self.x < 9:
                self.x += 1
            else:
                self.score -= 10
        elif action == 3:
            if self.x > 0:
                self.x -= 1
            else:
                self.score -= 10
        #pickup
        elif action == 4:
            if situation[4]:
                self.score += 10
                #and remove item from spot:
                grid.grid[(self.x, self.y)] = False
            else:
                self.score -= 1

        #final random action
        #(rewrite it better when clearer headed...not quite random as is)
        elif action == 5:
            if random.randrange(2) == 0:
                if random.randrange(2) == 0 and self.y > 0:
                    self.y -= 1
                elif self.y < 9:
                    self.y += 1
            else:
                if random.randrange(2) == 0 and self.x > 0:
                    self.x -= 0
                elif self.x < 9:
                    self.x += 0
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
        view = []
        if y == 0:
            view.append(2)
        else:
            view.append(self.grid[(x, y - 1)])
        if x == 9:
            view.append(2)
        else:
            view.append(self.grid[(x + 1, y)])
        if x == 0:
            view.append(2)
        else:
            view.append(self.grid[(x - 1, y)])
        if y == 9:
            view.append(2)
        else:
            view.append(self.grid[(x, y + 1)])
        view.append(self.grid[(x, y)])
        return tuple(view)


def main():

    #create grid
    grid = Grid()
    #create lookup table
    table = Situation_Table()
    #create 200 randomized robots to start with
    robots = []
    for x in range(200):
        robots.append(Robot())



    
    

    #each robot
    for r in robots:
        this_robot_scores = []
        
        #performs 100 sessions
        for s in range(100):
            r.score = 0
            
            #making 200 moves each time
            for m in range(200):
                r.move(grid, table)
                
            this_robot_scores.append(r.score)
        
        #average those 100 scores to get fitness rating
        r.fitness = sum(this_robot_scores) / 100
        


        
        
        


main()
