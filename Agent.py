from Settings import *

from kivy.graphics import *

from random import randint
from math import sqrt

class Agent:

    def __init__(self, canvas, goal, obstacles):
        self.canvas = canvas
        self.x = randint(1, GRID_WIDTH) * CELL_SIZE
        self.y = randint(1, GRID_HEIGHT) * CELL_SIZE

        self.goal = goal
        self.obstacles = obstacles

        self.travelled = []
        self.path = []

        self.calculated = False

        self.draw()

    def draw(self):
        with self.canvas:
            Color(1, 1, 0)
            for t in self.travelled:
                Rectangle(pos=t, size=(CELL_SIZE, CELL_SIZE))

            Color(1, 1, 1)
            Rectangle(pos=(self.x, self.y), size=(CELL_SIZE, CELL_SIZE))
            self.travelled.append((self.x, self.y))

    def update(self, dt):

        if self.calculated == False:
            self.draw()
            self.calculated = True
            return
        elif self.calculated == True:
            self.aStar()
            self.calculated = -1

        if len(self.path) != 0:
            nextMove = self.path.pop()
            self.x = nextMove[0]
            self.y = nextMove[1]

        self.draw()

    def aStar(self):
        
        def h(node, goal):
            # Manhattan distance
            return max([node[0] - goal[0], node[1] - goal[1]])

        def reconstruct_path(cameFrom, node):
            total_path = [node]
            while node in cameFrom.keys():
                node = cameFrom[node]
                total_path.append(node)
            return total_path

        def getNeighbours(node):
            # Only allow four directions of movement
            neighbours = [
                (node[0], node[1] + CELL_SIZE),
                (node[0], node[1] - CELL_SIZE),
                (node[0] + CELL_SIZE, node[1]),
                (node[0] - CELL_SIZE, node[1])
            ]
            return neighbours

        def dist_between(node1, node2):
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

