#
# PathFinder.py
#
# Original Author: Matthew J Egan
#          Github: mattjegan/PathFinder
#
# This file sets up the Kivy application and instantiates
# the world that the agent runs in.

from Settings import Settings
from World import World

import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config

from sys import stdin

class PathFinder(App):

    title = 'PathFinder'

    def __init__(self):
        super().__init__()
        self.settings = Settings()

        # If there is piped input
        if not stdin.isatty():
            try:
                cli_settings = stdin.read().rstrip().split(' ')

                self.settings.CELL_SIZE = int(cli_settings[0])
                self.settings.NUM_OBSTACLES = int(cli_settings[1])
                self.settings.GRID_WIDTH = int(cli_settings[2])
                self.settings.GRID_HEIGHT = int(cli_settings[3])

                self.settings.WINDOW_WIDTH  = str(self.settings.CELL_SIZE * self.settings.GRID_WIDTH)
                self.settings.WINDOW_HEIGHT = str(self.settings.CELL_SIZE * self.settings.GRID_HEIGHT)

                Config.set('graphics', 'width', self.settings.WINDOW_WIDTH)
                Config.set('graphics', 'height', self.settings.WINDOW_HEIGHT)

            except:
                raise IOError

    def build(self):
        Config.set('graphics', 'width', self.settings.WINDOW_WIDTH)
        Config.set('graphics', 'height', self.settings.WINDOW_HEIGHT)

        game = World(self.settings)
        game.draw()
        Clock.schedule_interval(game.update, self.settings.UPDATE_SPEED)
        return game

if __name__ == "__main__":
    PathFinder().run()