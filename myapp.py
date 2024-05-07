from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.button import Button

GUI = Builder.load_file("my.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI

MeuAplicativo().run()  