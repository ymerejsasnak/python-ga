import random


class Robot:

    def __init__(self):
        '''initialize each robot with randomized list of instructions
        (162 but some are not actually possible)
         0-north, 1-south, 2-east,3-west,4-stay,5-pick up,6-random move'''

        self.genes = []
        for x in range(162):
            self.genes.append(random.randrange(7))

    def __str__(self):
            return ''.join(map(str, self.genes))


class Situation_Table:

    def __init__(self):
        '''just initialize with *randomized* actions rather than
        entering 162 potential situations by hand and see how it goes...
        encoding: each current or adjacent space has 3 possible states:
        is empty, has item, or is a wall....make each possible combination
        a tuple of five numbers (0 empty, 1 item, 2 wall) in n/e/w/s/c order
        (ie north, east, west, south, and current) -- and use as key in dict
        to lookup action to take (0-6) see above'''

        self.table = {}

        for n in range(3):
            for e in range(3):
                for w in range(3):
                    for s in range(3):
                        for c in range(2):  #can't BE on a wall
                            self.table[(n, e, w, s, c)] = random.randrange(7)

    def __str__(self):
        output = []
        for k in self.table.keys():
            output.append('situation: ' + str(k) + '  action: ' + str(self.table[k]))
        return '\n'.join(output)


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


















def main():

    #below isn't quite right yet...getting ahead of myself...need to make it all work for 1 robot before I go further

    #create grid
    g = Grid()
    print (g)

    #create 200 randomized robots to start with
    robots = []
    for x in range(200):
        robots.append(Robot())

    for x in range(5):  #just print first five original robots as a test/example
        print ("Robot " + str(x) + ": " + str(robots[x]))

    table = Situation_Table()
    print (table)


main()
