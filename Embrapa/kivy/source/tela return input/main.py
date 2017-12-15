#conding: utf-8

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

def click():
    print(ed.text)



def build():
    layout = FloatLayout()
    ed = TextInput()
    global ed
    ed.text = "Entrada"
    layout.add_widget(ed)
    ed.size_hint = None,None
    ed.height = 300
    ed.width = 300
    ed.x = 50
    ed.y = 250

    bt = Button()
    bt.text = "Click aqui"
    layout.add_widget(bt)
    bt.size_hint = None,None
    bt.x = 400/2 -50
    bt.y = 100
    bt.on_press = click

    return layout

if __name__ == '__main__':
    Window.size = 400,600
    janela = App()
    janela.title = "aplicativo porreta"
    janela.build = build
    janela.run()