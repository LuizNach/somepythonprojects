# programa: 148 widget kvlang
# coding: utf-8

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window

class HelloApp(App):
    pass


if __name__ == "__main__":
    Window.size = 600,800
    HelloApp().run()