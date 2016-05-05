#
# PathFinder.py
#
# Original Author: Matthew J Egan
#          Github: mattjegan/PathFinder
#
# This file sets up the Kivy application and instantiates
# the world that the agent runs in.

from Settings import *

import kivy

from kivy.app import App

from kivy.clock import Clock


from kivy.config import Config
Config.set('graphics', 'width', WINDOW_WIDTH)
Config.set('graphics', 'height', WINDOW_HEIGHT)

from World import World

class PathFinder(App):

    title = 'PathFinder'

    def build(self):
        game = World()
        game.draw()
        Clock.schedule_interval(game.update, UPDATE_SPEED)
        return game

if __name__ == "__main__":
    PathFinder().run()