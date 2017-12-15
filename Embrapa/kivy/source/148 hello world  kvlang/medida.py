# programa: 148 widget kvlang
# coding: utf-8

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

class RootWidget(FloatLayout):
    pass

class medidaApp(App):

    def build(self):
        return RootWidget()


if __name__ == "__main__":
    Window.size = 600,800; # ??? Lembrar: mudar esse tamanho depois
    medidaApp().run()