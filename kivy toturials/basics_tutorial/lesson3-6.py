import kivy
from kivy.app import App
# from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

kivy.require('2.0.0')

# class Widgets(Widget):
#     pass

class SimpleKivy(App):
    def build(self):
        # return Widgets()
        return FloatLayout()

if __name__=='__main__':
    SimpleKivy().run()