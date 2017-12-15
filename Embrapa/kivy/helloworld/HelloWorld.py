import kivy
from kivy.app import App
kivy.require("1.10.0")
from kivy.uix.label import Label

class SimpleKivy(App):
    def build(self):
        return Label()

if __name__ == "__main__":
    SimpleKivy().run()