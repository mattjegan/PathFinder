from Settings import *

from kivy.uix.widget import Widget
from kivy.graphics import *

from random import randint

from Agent import Agent

class World(Widget):

    def __init__(self):
        super().__init__()
        
        # Generate Obstacles
        self.obstacles = []
        for i in range(NUM_OBSTACLES):
            self.obstacles.append((randint(0, GRID_WIDTH - 1) * CELL_SIZE, randint(0, GRID_HEIGHT - 1) * CELL_SIZE))

        # Generate goal
        self.goal = (randint(0, GRID_WIDTH - 1) * CELL_SIZE, randint(0, GRID_HEIGHT - 1) * CELL_SIZE)
        while self.goal in self.obstacles:
            self.goal = (randint(0, GRID_WIDTH - 1) * CELL_SIZE, randint(0, GRID_HEIGHT - 1) * CELL_SIZE)

        # Create the agent
        self.agent = Agent(self.canvas, self.goal, self.obstacles)

    def draw(self):
        
        with self.canvas:
            # Draw obstactles
            Color(1, 0, 0)
            for ob in self.obstacles:
                Rectangle(pos=ob, size=(CELL_SIZE, CELL_SIZE))

            # Draw goal
            Color(0, 0, 1)
            Rectangle(pos=self.goal, size=(CELL_SIZE, CELL_SIZE))

    def update(self, dt):
        with self.canvas:
            self.canvas.clear()
            self.draw()
            self.agent.update(dt)