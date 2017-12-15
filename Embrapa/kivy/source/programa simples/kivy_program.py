#conding: utf-8

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window

def click():
    print("hellow")

class kivy_program(App):

    def build(self):
        return Label(text="simples")

if __name__ == '__main__':
    Window.size = 400,600
    janela = kivy_program()
    janela.run()