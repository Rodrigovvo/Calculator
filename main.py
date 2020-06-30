#coding: utf-8
#author: Rodrigo Vinicius
from kivy.app import App
from kivy.uix.gridlayout import GridLayout



class CalcGridLayout(GridLayout):
    padding = (20, 20, 20, 20)
    spacing: (5, 5)
    def Calculo(self, calcular):
        if calcular:
            try:
                self.display.text = str(eval(calcular))
            except Exception:
                self.display.text = "Error"

class CalculadoraApp(App):
    title = "Calculadora - Python_Kivy"
    def build(self):
        return CalcGridLayout()

CalculadoraApp().run()