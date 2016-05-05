#
# World.py
#
# Original Author: Matthew J Egan
#          Github: mattjegan/PathFinder
#
# This file contains a widget that generates the world
# as well as communicates between the app and the agent

from Settings import *
from Agent import Agent

from kivy.uix.widget import Widget
from kivy.graphics import *

from random import randint

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
            Color(*OBSTACLE_COLOR)
            for ob in self.obstacles:
                Rectangle(pos=ob, size=(CELL_SIZE, CELL_SIZE))

            # Draw goal
            Color(*GOAL_COLOR)
            Rectangle(pos=self.goal, size=(CELL_SIZE, CELL_SIZE))

    def update(self, dt):
        with self.canvas:
            self.agent.update(dt)