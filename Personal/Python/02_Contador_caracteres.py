# Pedimos al usuario que ingrese una cadena
cadena = input("Por favor ingrese una cadena de texto: ")

# Inicializamos el contador
contador = 0

# Recorremos la cadena
for caracter in cadena:
    # Por cada caracter, aumentamos el contador
    contador = contador + 1

# Mostramos el resultado
print(f"La cadena tiene {contador} caracteres")