CELL_SIZE = 10
NUM_OBSTACLES = 3000

GRID_WIDTH  = 100
GRID_HEIGHT = 100
INFINITY = 999999

WINDOW_WIDTH  = str(CELL_SIZE * GRID_WIDTH)
WINDOW_HEIGHT = str(CELL_SIZE * GRID_HEIGHT)

UPDATE_SPEED = 1.0 / 60.0

UP         = ( 0,  1)
DOWN       = ( 0, -1)
LEFT       = (-1,  0)
RIGHT      = ( 1,  0)
UP_LEFT    = (-1,  1)
UP_RIGHT   = ( 1,  1)
DOWN_LEFT  = (-1, -1)
DOWN_RIGHT = ( 1, -1)

AGENT_COLOR = (0, 1, 0)
GOAL_COLOR = (1, 0, 0)
OBSTACLE_COLOR = (.4, 0, .4)
TRAVELLED_PATH_COLOR = (.6, .6, .6)