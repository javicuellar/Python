from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config


class CalcGridLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = 'Error no se puede multiplicar entre 0'

#  El fichero con la información *.kv debe llamarse igual que la clase, nombre + App -> "Calculadora.kv"
class CalculadoraApp(App):
    def build(self):
        return CalcGridLayout()


calcApp = CalculadoraApp()
calcApp.run()