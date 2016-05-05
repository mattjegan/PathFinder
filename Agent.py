from Settings import *

from kivy.graphics import *

from random import randint
from math import sqrt

class Agent:

    def __init__(self, canvas, goal, obstacles):
        self.canvas = canvas
        self.x = randint(0, GRID_WIDTH - 1) * CELL_SIZE
        self.y = randint(0, GRID_HEIGHT - 1) * CELL_SIZE

        self.goal = goal
        self.obstacles = obstacles

        self.travelled = []
        self.path = []

        self.calculated = False

        self.draw()

    def draw(self):
        with self.canvas:

            # Draw where the agent has been
            Color(*TRAVELLED_PATH_COLOR)
            for t in self.travelled:
                Rectangle(pos=t, size=(CELL_SIZE, CELL_SIZE))

            # Draw where the agent is
            Color(*AGENT_COLOR)
            Rectangle(pos=(self.x, self.y), size=(CELL_SIZE, CELL_SIZE))
            self.travelled.append((self.x, self.y))

    def update(self, dt):

        # If we haven't drawn the initial position do that now
        if self.calculated == False:
            self.draw()
            self.calculated = True
            return

        # This is be excuted after the initial world has finished
        # being rendered
        elif self.calculated == True:
            self.aStar()
            self.calculated = -1

        if len(self.path) != 0:
            nextMove = self.path.pop()
            self.x = nextMove[0]
            self.y = nextMove[1]

        self.draw()

    def aStar(self):
        # An implementation of the A* search algorithm as
        # described by wikipedia. We use the diagonal distance
        # heuristic by default as it is optimal when 8 directions
        # of movement are available.
        
        def h(node, goal):
            # Manhattan distance
            dx = abs(node[0] - goal[0])
            dy = abs(node[1] - goal[1])
            #return max([dx, dy])

            # Diagonal distance
            return (dx + dy) - min([dx, dy])

        def reconstruct_path(cameFrom, node):
            # Recontructs the path via backtracking through cameFrom
            total_path = [node]
            while node in cameFrom.keys():
                node = cameFrom[node]
                total_path.append(node)
            return total_path

        def getNeighbours(node):
            # Allow eight directions of movement
            neighbours = [
                (node[0], node[1] + CELL_SIZE), # Up
                (node[0], node[1] - CELL_SIZE), # Down
                (node[0] - CELL_SIZE, node[1]), # Left
                (node[0] + CELL_SIZE, node[1]), # Right
                (node[0] - CELL_SIZE, node[1] + CELL_SIZE), # UpLeft
                (node[0] + CELL_SIZE, node[1] + CELL_SIZE), # UpRight
                (node[0] - CELL_SIZE, node[1] - CELL_SIZE), # DownLeft
                (node[0] + CELL_SIZE, node[1] - CELL_SIZE), # DownRight
            ]

            # Remove an neighbours that are actually obstacles
            validNeighbours = []
            for n in neighbours:
                if n not in self.obstacles:
                    validNeighbours.append(n)

            return validNeighbours

        def dist_between(node1, node2):
            # Returns the distance between two nodes
            xSquared = (node2[0] - node1[0])**2
            ySquared = (node2[1] - node1[1])**2

            return sqrt(xSquared + ySquared)

        closedSet = []

        start = (self.x, self.y)

        openSet = [start]

        cameFrom = {}

        gScore = {}
        gScore[start] = 0

        fScore = {}
        fScore[start] = h(start, self.goal)

        while len(openSet) != 0:
            current = openSet[0]
            for node in openSet:
                if fScore.get(node, INFINITY) < fScore.get(current, INFINITY):
                    current = node

            if current == self.goal:
                self.path = reconstruct_path(cameFrom, current)
                return

            openSet.remove(current)
            closedSet.append(current)
            for neighbour in getNeighbours(current):
                if neighbour in closedSet:
                    continue

                tentative_gScore = gScore.get(current, INFINITY) + dist_between(current, neighbour)
                if neighbour not in openSet:
                    openSet.append(neighbour)
                elif tentative_gScore >= gScore.get(neighbour, INFINITY):
                    continue

                cameFrom[neighbour] = current
                gScore[neighbour] = tentative_gScore
                fScore[neighbour] = gScore.get(neighbour, INFINITY) + h(neighbour, self.goal)

        print("No path found")
        return

