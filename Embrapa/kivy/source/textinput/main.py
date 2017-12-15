#conding: utf-8

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

def build():
    return TextInput(text="primeiro texto")

if __name__ == '__main__':
    uma_var_qlqr = App()
    uma_var_qlqr.build = build
    uma_var_qlqr.run()