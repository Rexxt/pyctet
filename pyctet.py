import lib.pycge as pycge
import random

class Game(pycge.PyConsoleGame):
    def __init__(self):
        super(Game, self).__init__()
        self.name = "PyCGE Tetra"
        self.blocktextures = [
            "..",
            "[]",
            "()",
            "▒▒",
            "☼☼"
        ]

        self.grid = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
        ]
    
    def create(self):
        pycge.clear()

    def update(self, dt):
        self.dt = dt
        y = random.randrange(0,len(self.grid))
        self.grid[y][random.randrange(0,len(self.grid[y]))] = random.randrange(0,4)

    def draw(self):
        pycge.printXY("HOLD", 10, 3)
        pycge.printXY("NEXT", 36, 3)
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                pycge.printXY(self.blocktextures[self.grid[y][x]], 15 + 2*x, 3 + y)

game = Game()
game.start()