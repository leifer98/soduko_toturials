import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import os

kivy.require('2.0.0')

class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        if os.path.isfile('details.txt'):
            with open('details.txt','r') as f:
                d = f.read().split(',')
                prev_ip = d[0]
                prev_port = d[1]
                prev_username = d[2]
        else:
            prev_ip = ''
            prev_port = ''
            prev_username = ''



        self.add_widget(Label(text='IP: '))
        self.ip = TextInput(text=prev_ip, multiline = False)
        self.add_widget(self.ip)

        self.add_widget(Label(text='PORT: '))
        self.port = TextInput(text=prev_port, multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text='USERNAME: '))
        self.username = TextInput(text=prev_username, multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label())

        self.join = Button(text = 'Join')
        self.join.bind(on_press=self.join_func)
        self.add_widget(self.join)
    def join_func(self, instance):
        port = self.port.text
        ip = self.ip.text
        username = self.username.text

        print(f"Attempting to join {ip}:{port} as {username}")

        with open("details.txt",'w') as f:
            f.write(f"{ip},{port},{username}")



class EpicApp(App):
    def build(self):
        return ConnectPage()

if __name__ == '__main__':
    EpicApp().run()

