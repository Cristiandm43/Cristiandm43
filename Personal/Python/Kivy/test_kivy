
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Mensaje:"))
        self.mensaje = TextInput(multiline=False)
        self.add_widget(self.mensaje)

        self.add_widget(Label(text="Desplazamiento:"))
        self.desplazamiento = TextInput(multiline=False)
        self.add_widget(self.desplazamiento)

        self.encriptar = Button(text="Encriptar")
        self.encriptar.bind(on_press=self.encriptar_mensaje)
        self.add_widget(self.encriptar)

        self.add_widget(Label(text="Mensaje encriptado:"))
        self.mensaje_encriptado = TextInput(multiline=False)
        self.add_widget(self.mensaje_encriptado)

    def encriptar_mensaje(self, instance):
        mensaje = self.mensaje.text
        desplazamiento = int(self.desplazamiento.text)
        mensaje_encriptado = ""

        for caracter in mensaje:
            if caracter.isalpha():
                num = ord(caracter)
                num += desplazamiento

                if caracter.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                elif caracter.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26

                mensaje_encriptado += chr(num)
            else:
                mensaje_encriptado += caracter

        self.mensaje_encriptado.text = mensaje_encriptado

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()