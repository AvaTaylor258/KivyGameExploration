# Ava Taylor

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock

from pipe import Pipe

class Background(Widget):
    cloud_texture = ObjectProperty(None)
    floor_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # create textures
        self.cloud_texture = Image(source="cloud.png").texture
        self.cloud_texture.wrap = "repeat"
        self.cloud_texture.uvsize = (Window.width / self.cloud_texture.width, -1)

        self.floor_texture = Image(source="floor.png").texture
        self.floor_texture.wrap = "repeat"
        self.floor_texture.uvsize = (Window.width / self.floor_texture.width, -1)

    def scroll_textures(self, time_passed):
        # update the uvpos of the texture
        self.cloud_texture.uvpos = ((self.cloud_texture.uvpos[0] + time_passed/2) % Window.width, self.cloud_texture.uvpos[1])
        self.floor_texture.uvpos = ((self.floor_texture.uvpos[0] + time_passed) % Window.width, self.floor_texture.uvpos[1])

        # redraw the texture
        texture = self.property("cloud_texture")
        texture.dispatch(self)

        texture = self.property("floor_texture")
        texture.dispatch(self)

class GameExplorationApp(App):
    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll_textures, 1/60)
    pass


GameExplorationApp().run()
