import random


class Robot:

    def __init__(self):
        '''initialize each robot with randomized list of instructions (243 for now) 0-north, 1-south, 2-east,3-west,4-stay,5-pick up,6-random move'''

        self.genes = []
        for x in range(243):
            self.genes.append(random.randrange(0, 7))


class Grid:

    def __init__(self):
        '''create 10x10 grid with 50 percent chance of any cell containing an item for the robot to pick up'''

        self.grid = {}
        for y in range(10):
            for x in range(10):
                if random.randrange(0, 2) == 1:
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
            msgs.append(str(k) + msg)
        return ''.join(str(msgs))


def main():

    #create grid
    g = Grid()
    print (g)

    #create 200 randomized robots to start with
    robots = []
    for x in range(200):
        robots.append(Robot())


main()
