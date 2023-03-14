#Ciclo de números
numero=0
while True:
    for i in range(5):
        print(numero)
        numero+=1
    respuesta=input('Pulsa 1 para pausar el ciclo de números y comenzar el ciclo de las letras del alfabeto, 2 para continuar el ciclo de números o 3 para salir del programa: ')
    if respuesta=='1':
        #Ciclo de letras del alfabeto
        abecedario='abcdefghijklmnñopqrstuvwxyz'
        i=abecedario.index('a')
        while True:
            print(abecedario[i])
            i+=1
            if i==27: #Modificar esta línea
                #Reanudar el ciclo de números
                respuesta=input('Pulsa 1 para reanudar el ciclo de números o 2 para salir del ciclo: ')
                if respuesta=='1':
                    break
                elif respuesta=='2':
                    break
    elif respuesta=='2':
        continue
    elif respuesta=='3':
        break
    else:
        print('Opción no válida.')
print('Fin del programa, Gracias')