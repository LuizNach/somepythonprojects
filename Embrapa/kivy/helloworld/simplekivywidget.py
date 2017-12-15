from kivy.app import App
# kivy.require("1.8.0")
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder

class myWidgets(Widget):
    pass

Builder.load_string('''

<MyBoxLayout>:
    BoxLayout:
        Button:
            text: "test"
        Button:
            text: "test"
        Button:
            text: "test"
    BoxLayout:
        Button:
            text: "test"
        Button:
            text: "test"
        Button:
            text: "test"

''')


class SimpleKivy2App(App):
    def build(self):
        return myWidgets()


if __name__ == "__main__":
    SimpleKivy2App().run()