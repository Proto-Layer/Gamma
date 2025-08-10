from kivy.app import App
from kivy.uix.label import Label

class Gamma(App):
    def build(self):
        return Label(text = "Hello there", font_size = '24dp')
    

if __name__ == "__main__":
    Gamma().run()
