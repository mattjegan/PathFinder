#
# World.py
#
# Original Author: Matthew J Egan
#          Github: mattjegan/PathFinder
#
# This file contains a widget that generates the world
# as well as communicates between the app and the agent

from Agent import Agent

from kivy.uix.widget import Widget
from kivy.graphics import *

from random import randint

class World(Widget):

    def __init__(self, settings):
        super().__init__()

        self.settings = settings

        # Generate Obstacles
        self.obstacles = []
        for i in range(self.settings.NUM_OBSTACLES):
            self.obstacles.append((randint(0, self.settings.GRID_WIDTH - 1) * self.settings.CELL_SIZE, randint(0, self.settings.GRID_HEIGHT - 1) * self.settings.CELL_SIZE))

        # Generate goal
        self.goal = (randint(0, self.settings.GRID_WIDTH - 1) * self.settings.CELL_SIZE, randint(0, self.settings.GRID_HEIGHT - 1) * self.settings.CELL_SIZE)
        while self.goal in self.obstacles:
            self.goal = (randint(0, self.settings.GRID_WIDTH - 1) * self.settings.CELL_SIZE, randint(0, self.settings.GRID_HEIGHT - 1) * self.settings.CELL_SIZE)

        # Create the agent
        self.agent = Agent(self.settings, self.canvas, self.goal, self.obstacles, self.settings.HEURISTIC)

    def draw(self):
        
        with self.canvas:
            # Draw obstactles
            Color(*self.settings.OBSTACLE_COLOR)
            for ob in self.obstacles:
                Rectangle(pos=ob, size=(self.settings.CELL_SIZE, self.settings.CELL_SIZE))

            # Draw goal
            Color(*self.settings.GOAL_COLOR)
            Rectangle(pos=self.goal, size=(self.settings.CELL_SIZE, self.settings.CELL_SIZE))

    def update(self, dt):
        with self.canvas:
            self.agent.update(dt)