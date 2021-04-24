import kivy
from kivy.app import App
from kivy.uix.widget import Widget

kivy.require('2.0.0')

class TouchInput(Widget):
    def on_touch_down(self, touch):
        print(touch)
    def on_touch_move(self, touch):
        print(touch)
    def on_touch_up(self, touch):
        print(touch)

class SimpleKivy(App):
    def build(self):
        return TouchInput()

if __name__=='__main__':
    SimpleKivy().run()