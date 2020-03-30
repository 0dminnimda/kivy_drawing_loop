from kivy.app import App
from kivy.graphics import *#Color, Line, Rectangle
from kivy.uix.widget import Widget
from kivy.clock import Clock

import numpy as np
nar = np.array

class Touch(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) #super(Touch, self).__init__(**kwargs)

        self.naming()

        self.default_drawing()

        #self.drawing_func()
        Clock.schedule_interval(self.drawing_func, 0)

    def naming(self):
        self.pos = [0, 0]

    def default_drawing(self):
        with self.canvas:
            Line(points=(20, 30, 400, 500, 60, 500), width=10)
            Color(1, 0, 0, 0.5)#, mode="rgba")
            self.rect = Rectangle(pos=(0,0), size=(50,50))
            self.ell = Ellipse(pos=(0,0), size=(50,50), angle_end=180)

    def drawing_func(self, dt):
        #while 1:
        with self.canvas:
            Color(1, 0, 0, 0.5)
            self.ell.pos = nar(self.ell.pos) + 1

    def on_touch_down(self, touch):
        self.rect.pos = nar(touch.pos)-nar(self.rect.size)/2

    def on_touch_move(self, touch):
        self.rect.pos = nar(touch.pos)-nar(self.rect.size)/2

class MyApp(App):
    def build(self):
        return Touch()

if __name__ == "__main__":
    MyApp().run()
