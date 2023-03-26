from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class PrimeiroAppApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        #add widgets to window
        self.window.add_widget(Image(source="Logo.png"))

        self.greeting = Label(
            text = "Diz aí colé a boa", 
            font_size = 20,
            color = "#00FFCE"
            )
        self.window.add_widget(self.greeting)

        self.user = TextInput(
            padding_y = (20,20),
            size_hint = (1, 0.5)
            )
        self.window.add_widget(self.user)

        self.button = Button(
            text = "Clica aqui irmão",
            size_hint = (1,0.5), 
            bold = True, 
            
            background_color = "#00FFCE",
            background_normal = ""
            )
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)

        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x" : 0.5, "center_y" : 0.5}

        return self.window
    
    def callback(self, instance):
        self.greeting.text = f"A boa é {self.user.text}"


if __name__ == "__main__":
    PrimeiroAppApp().run()
