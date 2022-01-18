from audioop import add
from cgitb import text
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

items = {}

class MainApp(App):
    global items

    def build(self):
        startPage = GridLayout(cols=1)

        self.txt = Label(text = "Welcome!")
        startPage.add_widget(self.txt)

        self.listSegment = GridLayout(cols=3)

        startPage.add_widget(self.listSegment)

        # button to add items to list segment
        addBtn = Button(text="Add item")
        addBtn.bind(on_release = self.addItem)
        startPage.add_widget(addBtn)

        return startPage
    def addItem(self, instance):
        items["carrot"] = 2
        item = Label(text="carrot")
        quantity = Label(text="2")
        self.listSegment.add_widget(item)
        self.listSegment.add_widget(quantity)

        #Delete button
        remove = Button(text = "remove")
        self.listSegment.add_widget(remove)
        return
if __name__ == '__main__':
    MainApp().run()