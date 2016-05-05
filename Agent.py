from kivy.graphics import *

from random import randint

class Agent:

    def __init__(self, canvas):
        self.canvas = canvas
        self.x = randint(1, 500)
        self.y = randint(1, 500)

    def draw(self):
        with self.canvas:
            Color(1, 1, 1)
            self.r = Rectangle(pos=(self.x, self.y), size=(5, 5))

    def update(self, dt):
        self.x += 1
        self.y += 1
        self.draw()