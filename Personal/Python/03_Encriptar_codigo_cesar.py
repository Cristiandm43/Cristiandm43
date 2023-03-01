# Definimos la funcion de encriptacion
def cifradoCesar(palabra):
    # La palabra a encriptar se guarda en una lista de caracteres
    caracteres = list(palabra)
    # Solicitamos el desplazamiento para la encriptacion
    desplazamiento = int(input("Ingresa el desplazamiento para la encriptacion: "))
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

# Solicitamos la palabra a encriptar
palabra = input("Ingresa la palabra a encriptar: ")

# Mostramos la palabra encriptada
print("Palabra encriptada:", cifradoCesar(palabra))