from kivy.uix.widget import Widget
from kivy.graphics import *

from random import randint

from Agent import Agent

class World(Widget):

    def __init__(self):
        super().__init__()
        self.agent = Agent(self.canvas)
        
        # Generate Obstacles
        self.obstacles = []
        for i in range(100):
            self.obstacles.append((randint(1, 500),randint(1, 500)))

        # Generate goal
        self.goal = (randint(1, 500),randint(1, 500))

    def draw(self):
        
        with self.canvas:
            # Draw obstactles
            Color(1, 0, 0)
            for ob in self.obstacles:
                Rectangle(pos=ob, size=(5, 5))

            # Draw goal
            Color(1, 0, 1)
            Rectangle(pos=self.goal, size=(5, 5))

            # Draw the agent
            self.agent.draw()


    def update(self, dt):
        with self.canvas:
            self.canvas.clear()
            self.draw()
            self.agent.update(dt)