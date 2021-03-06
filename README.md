# PathFinder

![](http://i.imgur.com/DVoBZfC.png)

## Overview

PathFinder is an open-source application which I (Matthew Egan) have developed for the sole purpose of curiosity. The application is powered by [Kivy](https://kivy.org/), a Python GUI framework. The PathFinder Agent implements the [A* search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm) which, using a heuristic, will find the optimal path through some state space (in our case, a maze of 2 dimensional co-ordinates) from some starting state to a goal state.

## Heuristics
The heuristic I have decided to use by default is the [diagonal distance heuristic](http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html#heuristics-for-grid-maps) which will estimate the minimum amount of steps to the goal when allowed 8 directions of movement.

## Running Pathfinder
To run PathFinder, simply clone the repository:

	clone https://github.com/mattjegan/PathFinder

[Install Kivy](https://kivy.org/docs/installation/installation.html), and then run:

	kivy PathFinder.py

## Contribution
If you would like to contribute to PathFinder please make a pull request.

## Customization
### Permanent Customization
To customize PathFinder colours and value permanently, simply edit values in Settings.py.

### Temporary Customization
It is possible to customize PathFinder from the command line. This is primarily for the case when a user wants to run multiple simulations of the PathFinder Agent with different constraints. Due to Kivy already parsing command line arguments we must interact with PathFinder through piped arguments:

	echo '5 2000 300 50' | kivy PathFinder.py
    
The string is of the form `CELL_SIZE NUM_OBSTACLES GRID_WIDTH GRID_HEIGHT`