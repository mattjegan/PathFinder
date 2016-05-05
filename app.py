import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import *

from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')

from random import randint

class MyAgent:

    def __init__(self, canvas):
        self.canvas = canvas
        self.x = randint(1, 500)
        self.y = randint(1, 500)

    def draw(self):
        with self.canvas:
            Color(1, 1, 1)
            self.r = Rectangle(pos=(self.x, self.y), size=(5, 5))

    def update(self, dt):
        self.x += 1
        self.y += 1
        self.draw()


class MyWidget(Widget):

    def __init__(self):
        super().__init__()
        self.agent = MyAgent(self.canvas)
        
        # Generate Obstacles
        self.obstacles = []
        for i in range(100):
            self.obstacles.append((randint(1, 500),randint(1, 500)))

        # Generate goal
        self.goal = (randint(1, 500),randint(1, 500))

    def draw(self):
        
        with self.canvas:
            # Draw obstactles
            Color(1, 0, 0)
            for ob in self.obstacles:
                Rectangle(pos=ob, size=(5, 5))

            # Draw goal
            Color(1, 0, 1)
            Rectangle(pos=self.goal, size=(5, 5))

            # Draw the agent
            self.agent.draw()


    def update(self, dt):
        with self.canvas:
            self.canvas.clear()
            self.draw()
            self.agent.update(dt)


class MyApp(App):

    def build(self):
        game = MyWidget()
        game.draw()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == "__main__":
    MyApp().run()