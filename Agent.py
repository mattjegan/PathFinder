from Settings import *

from kivy.graphics import *

from random import randint

class Agent:

    def __init__(self, canvas, goal, obstacles):
        self.canvas = canvas
        self.x = randint(1, GRID_WIDTH) * CELL_SIZE
        self.y = randint(1, GRID_HEIGHT) * CELL_SIZE

        self.goal = goal
        self.obstacles = obstacles

        self.path = []
        self.aStar()

        self.travelled = []

    def draw(self):
        with self.canvas:
            Color(1, 1, 0)
            for t in self.travelled:
                Rectangle(pos=t, size=(CELL_SIZE, CELL_SIZE))

            Color(1, 1, 1)
            Rectangle(pos=(self.x, self.y), size=(CELL_SIZE, CELL_SIZE))
            self.travelled.append((self.x, self.y))

    def update(self, dt):
        if len(self.path) != 0:
            nextMove = self.path.pop()
            self.x += CELL_SIZE * nextMove[0]
            self.y += CELL_SIZE * nextMove[1]

        self.draw()

    def aStar(self):
        pass