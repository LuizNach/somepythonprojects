#conding: utf-8

from kivy.app import App
from kivy.uix.label import Label

def build():
    return Label(text = "Hello Kivy World", italic=True, font_size = 20)

if __name__ == '__main__':
    uma_var_qlqr = App()
    uma_var_qlqr.build = build
    uma_var_qlqr.run()