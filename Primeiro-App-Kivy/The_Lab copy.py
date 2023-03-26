from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class WidgetsExample(GridLayout, Screen):
    count = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("1")
    text_input_str = StringProperty("foo")
    # slider_start = 75
    # slider_value_txt = StringProperty(str(slider_start))

    def on_button_click(self):
        if self.count_enabled == True:
            self.count += 1
            self.my_text = str(self.count)    
    def on_toggle_button_state(self, widget):
        print("toggle state: " + widget.state)
        if widget.state == "normal":
            widget.text = "Off"
            self.count_enabled = False
        if widget.state == "down":
            widget.text = "On"
            self.count_enabled = True
    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    def on_slider_value(self, widget):
        print("Slider: " + str(int(widget.value)))
        # self.slider_value_txt = str(int(widget.value))
    def on_text_validate(self, widget):
        self.text_input_str = widget.text

class StackLayoutExample(StackLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = (20, 20, 20, 20)
        self.spacing = (20, 20)
        for i in range(40):
            b = Button(text= str(i+1), size_hint=(None,None), size=(dp(100), dp(100)))
            self.add_widget(b)

# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout, Screen):
    pass

class BoxLayoutExample(BoxLayout, Screen):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="a")
    #     b2 = Button(text="b")
    #     b3 = Button(text="c")
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)

class MainWidget(Widget):
    pass


class TheLabCopyApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(WidgetsExample(name="tela3"))
        sm.add_widget(StackLayoutExample(name="tela1"))
        sm.add_widget(BoxLayoutExample(name="tela2"))
        return sm

haha = TheLabCopyApp()
haha.run()