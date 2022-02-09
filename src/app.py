from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

class listPage(Widget):
    def build(self):
        self.startLayout = GridLayout(cols=1)
        self.topLable = Label(text="Welcome")
        self.startLayout.add_widget(self.topLable)
        
        return self.startLayout

class MainApp(App):
    def build(self):
        self.startLayout = GridLayout(cols=1)
        self.topLable = Label(text="Welcome")
        self.startLayout.add_widget(self.topLable)
        return self.startLayout

if __name__ == '__main__':
    MainApp().run()