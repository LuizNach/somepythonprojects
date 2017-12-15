#conding: utf-8

from kivy.app import App
from kivy.uix.button import Button

def clique():
    print("O botao foi clicado")


def build():
    bt = Button()
    bt.text = "Clique aqui"
    bt.on_press = clique
    return bt

if __name__ == '__main__':
    uma_var_qlqr = App()
    uma_var_qlqr.build = build
    uma_var_qlqr.run()