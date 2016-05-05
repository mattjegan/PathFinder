#
# Settings.py
#
# Original Author: Matthew J Egan
#          Github: mattjegan/PathFinder
#
# This file contains various values that are used in 
# the PathFinder Kivy application

class Settings:
    # World Geometry
    CELL_SIZE = 5
    NUM_OBSTACLES = 2000
    GRID_WIDTH  = 100
    GRID_HEIGHT = 100
    INFINITY = 999999

    # Application Settings
    WINDOW_WIDTH  = str(CELL_SIZE * GRID_WIDTH)
    WINDOW_HEIGHT = str(CELL_SIZE * GRID_HEIGHT)
    UPDATE_SPEED = 0.5 / 60.0

    # Colors
    AGENT_COLOR = (0, 1, 0)
    GOAL_COLOR = (1, 0, 0)
    OBSTACLE_COLOR = (.4, 0, .4)
    TRAVELLED_PATH_COLOR = (.6, .6, .6)