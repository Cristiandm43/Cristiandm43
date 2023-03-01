#importamos las librerias necesarias
import kivy 
import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Definimos la clase principal
class CifradoCesarApp(App):

    def build(self):
        # Inicializamos la interfaz de usuario
        self.layout = GridLayout(cols = 2)

        # Agregamos los elementos a la interfaz de usuario
        self.label_1 = Label(text = "Ingresa la palabra a encriptar:")
        self.input_1 = TextInput(multiline = False)
        self.label_2 = Label(text = "Ingresa el desplazamiento para la encriptacion:")
        self.input_2 = TextInput(multiline = False)
        self.boton = Button(text = "Encriptar")
        self.label_3 = Label(text = "")

        # Agregamos los elementos a la interfaz de usuario
        self.layout.add_widget(self.label_1)
        self.layout.add_widget(self.input_1)
        self.layout.add_widget(self.label_2)
        self.layout.add_widget(self.input_2)
        self.layout.add_widget(self.boton)
        self.layout.add_widget(self.label_3)

        # Definimos el evento de click en el boton
        self.boton.bind(on_press = self.encriptar)
        return self.layout

    # Definimos la funcion de encriptacion
    def cifradoCesar(self, palabra):
        # La palabra a encriptar se guarda en una lista de caracteres
        caracteres = list(palabra)
        # Obtenemos el desplazamiento para la encriptacion
        desplazamiento = int(self.input_2.text)

        # Iteramos sobre cada caracter de la palabra
        for i in range(len(caracteres)):
            # Si el caracter es una letra
            if caracteres[i].isalpha():
                # Obtenemos el codigo ASCII del caracter
                codigo = ord(caracteres[i])
                # Si es una letra mayuscula
                if codigo >= 65 and codigo <= 90:
                    codigo += desplazamiento
                    # Si el codigo ASCII supera el limite de letras mayusculas
                    if codigo > 90:
                        codigo -= 26
                # Si es una letra minuscula
                elif codigo >= 97 and codigo <= 122:
                    codigo += desplazamiento
                    # Si el codigo ASCII supera el limite de letras minusculas
                    if codigo > 122:
                        codigo -= 26
                # Se actualiza el caracter de la palabra encriptada con el nuevo codigo ASCII
                caracteres[i] = chr(codigo)
            else:
                # Si el caracter es un espacio, no se realiza ninguna modificación
                if caracteres[i] == ' ':
                    pass
                #Si el caracter se sale de los margenes del codigo ASCCI para alfabeto 
                else:
                    print('No es encriptable con estos caracteres')

        # Devolvemos la palabra encriptada
        return ''.join(caracteres)

    # Definimos la funcion que se ejecuta al presionar el boton
    def encriptar(self, objeto):
        # Obtenemos la palabra a encriptar
        palabra = self.input_1.text
        # Mostramos la palabra encriptada
        self.label_3.text = "Palabra encriptada: " + self.cifradoCesar(palabra)