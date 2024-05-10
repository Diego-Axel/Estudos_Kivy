from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


GUI = Builder.load_file("tela.kv")

class SuperMarketListApp(App):
    items = []

    def build(self):
        return GUI

    def add_item(self):
        item_name = self.root.ids.item_name_input.text
        item_quantity = self.root.ids.item_quantity_input.text
        item_description = self.root.ids.item_description_input.text

        if item_name and item_quantity:
            item_text = f"{item_name}: {item_quantity} ({item_description})"
            self.items.append(item_text)
            self.update_list()

    def update_list(self):
        self.root.ids.item_list.clear_widgets()
        for item in self.items:
            label = Label(text=item, size_hint_y=None, height=40)
            self.root.ids.item_list.add_widget(label)

    def generate_pdf(self):
        c = canvas.Canvas("supermarket_list.pdf", pagesize=letter)
        y = 750
        for item in self.items:
            c.drawString(100, y, item)
            y -= 20
        c.save()

SuperMarketListApp().run()
