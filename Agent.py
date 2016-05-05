from Settings import *

from kivy.graphics import *

from random import randint

class Agent:

    def __init__(self, canvas):
        self.canvas = canvas
        self.x = randint(1, GRID_WIDTH) * CELL_SIZE
        self.y = randint(1, GRID_HEIGHT) * CELL_SIZE

    def draw(self):
        with self.canvas:
            Color(1, 1, 1)
            self.r = Rectangle(pos=(self.x, self.y), size=(CELL_SIZE, CELL_SIZE))

    def update(self, dt):
        self.x += CELL_SIZE
        self.y += CELL_SIZE
        self.draw()