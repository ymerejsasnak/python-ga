import random


class Robot:

    def __init__(self):
        '''initialize each robot with position and randomized instructions
        (162 but some are not actually possible)
        0-north, 1-south, 2-east,3-west,4-pick up,5-random move
        encoding: each current or adjacent space has 3 possible states:
        is empty, has item, or is a wall....make each possible combination
        a tuple of five numbers (0 empty, 1 item, 2 wall) in n/e/w/s/c order
        (ie north, east, west, south, and current) -- and use as key in dict
        to lookup action to take (0-5) '''
        #will need to adjust this for children robots eventually
        self.x = 0
        self.y = 0
        self.score = 0
        
        self.genes = {}
        for n in range(3):
            for e in range(3):
                for w in range(3):
                    for s in range(3):
                        for c in range(2):  #can't BE on a wall
                            self.genes[(n, e, w, s, c)] = random.randrange(6)

    def __str__(self):
        output = []
        for k in self.genes.keys():
            output.append('situation: ' + str(k) + '  action: ' + str(self.genes[k]))
        return '\n'.join(output)

    
    def move(self, grid):
        #use situation variable to lookup action, then take action (checking for wall collisions)
        #hit wall -5 points, pick up item +10 points, try to pick up but nothing there -1 points
        situation = grid.get_situation(self.x, self.y)
        action = self.genes[situation]
        #moves
        if action == 0:
            if self.y > 0:
                self.y -= 1
            else:
                self.score -= 10
        if action == 1:
            if self.y < 9:
                self.y += 1
            else:
                self.score -= 10
        if action == 2:
            if self.x < 9:
                self.x += 1
            else:
                self.score -= 10
        if action == 3:
            if self.x > 0:
                self.x -= 1
            else:
                self.score -= 10
        #pickup
        if action == 4:
            if situation[4] == True:
                self.score += 10 #just 1 point for each for now until i figure something better
                grid.grid[(self.x, self.y)] = False #no more item in this spot
            else:
                self.score -= 1

        #final random action (rewrite it better when clearer headed...not quite random as is)
        if action == 5: 
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


class Grid:

    def __init__(self):
        '''create 10x10 grid with 50 percent chance of any
        cell containing an item for the robot to pick up'''

        self.grid = {}
        for y in range(10):
            for x in range(10):
                if random.randrange(2) == 1:
                    self.grid[(x, y)] = True
                else:
                    self.grid[(x, y)] = False

    def __str__(self):
        msgs = []
        msg = ''
        for k in self.grid.keys():
            if self.grid[k]:
                msg = ' has an item'
            else:
                msg = ' is empty'
            msgs.append("cell " + str(k) + msg)
        return '\n'.join(msgs)

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

    #below is a mess for now...testing stuff, etc

    #create grid
    grid = Grid()
    print (grid)

    #create 200 randomized robots to start with
    robots = []
    for x in range(200):
        robots.append(Robot())




    #for x in range(5):  #just print first five original robots as a test/example
    #    print ("Robot " + str(x) + ": " + str(robots[x]))

    #each robot
    for r in robots:
        #moves 200 times
        for i in range(200):
            r.move(grid)
        #then prints score
        print (r.score)





main()
