from kivy.app import App
from kivy.uix.label import Label

class AnaUygulama(App):
    def build(self):
        return Label(text='Merhaba, GitHub Actions!')

AnaUygulama().run()
