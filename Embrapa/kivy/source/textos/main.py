#conding: utf-8

from kivy.app import App
from kivy.uix.label import Label

def build():
    lb = Label()
    lb.text = "Hello Kivy World"
    lb.italic=True
    lb.font_size = 50; #size em tamanho de pixels
    return lb

if __name__ == '__main__':
    uma_var_qlqr = App()
    uma_var_qlqr.build = build
    uma_var_qlqr.run()