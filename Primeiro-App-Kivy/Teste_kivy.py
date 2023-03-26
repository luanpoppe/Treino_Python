from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class RootWidget(GridLayout):
    root2 = GridLayout(cols = 3)
    a2 = Label(text = "oláaa")
    root2.add_widget(a2)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    

class TestApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        root = GridLayout(cols = 3)
        a = Label(text = "oláaa")
        # b = RootWidget.root2
        root.add_widget(a)
        root.add_widget(RootWidget.root2)
        # root.add_widget(root2)

        return root

if __name__ == '__main__':
    TestApp().run()