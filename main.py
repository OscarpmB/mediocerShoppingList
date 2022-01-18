from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

items = {}

class MainApp(App):
    global items
    
    def build(self):
        self.counter = 0 # dummy index for testing item adding and removing

        startPage = GridLayout(cols=1) # size for base grid

        self.toplable = Label(text = "Welcome!")
        startPage.add_widget(self.toplable)
        
        # listSegment holds item list in middle of screen
        self.listSegment = GridLayout(cols=1)
        startPage.add_widget(self.listSegment)

        # button to add items to list segment
        addBtn = Button(text="Add item")
        addBtn.bind(on_release = self.addItem)
        startPage.add_widget(addBtn)

        return startPage


    def addItem(self, instance):
        i = 'carrot' + str(self.counter)
        q = self.counter
        self.counter = self.counter + 1

        row = BoxLayout()
        items[i] = q
        item = Label(text=i)
        quantity = Label(text=str(q))
        row.add_widget(item)
        row.add_widget(quantity)
        
        # Delete button
        remove = Button(text = "remove")
        #remove.bind(on_release = deleteItem())
        row.add_widget(remove)


        self.listSegment.add_widget(row)

        print(items)
        return

    def deleteItem(self, instance):
        self.listSegment.remove_widget(self)
        

if __name__ == '__main__':
    MainApp().run()