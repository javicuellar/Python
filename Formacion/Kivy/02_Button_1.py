from kivy.app import App
from kivy.uix.button import Button
from functools import partial


#  Botón simple que ocupa toda la pantalla y con background lo ponemos en rosa

# class miButton(App):
    # def build(self): 
        # return Button(text= 'Entrar')
        # return Button(text='Entrar', background_color=(155,0,51,53))


class miButton(App):
    def disable(self, instance, *args):
        instance.disable = True
    
    def update(self, instance, *args):
        instance.text = 'Estoy deshabilitado'

    def build(self):
        mybtn = Button(text= 'Haz click para desahabilitar')

        mybtn.bind(on_press=partial(self.disable, mybtn))
        mybtn.bind(on_press=partial(self.update, mybtn))

        return mybtn



miButton().run()