from kivy.uix.button import Button
from kivy.app import App


#  Botón situado en la posición "pos" con las medidas "size"

class miButton(App):
    def build(self): 
        return Button(text= 'Bienvenidos', pos=(400, 350), size_hint=(.30, .30))



miButton().run()