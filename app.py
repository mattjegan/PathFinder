import kivy

from kivy.app import App

from kivy.clock import Clock


from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')

from World import World

class MyApp(App):

    def build(self):
        game = World()
        game.draw()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == "__main__":
    MyApp().run()