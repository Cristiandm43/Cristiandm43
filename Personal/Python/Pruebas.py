import multiprocessing 
  
def print_cube(num): 
    """ 
    Función para imprimir el cubo de un número 
    """
    print("Cube: {}".format(num * num * num)) 
  
def print_square(num): 
    """ 
    Función para imprimir el cuadrado de un número 
    """
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": 
    # Creación de procesos para los dos métodos 
    p1 = multiprocessing.Process(target=print_square, args=(1000, )) 
    p2 = multiprocessing.Process(target=print_cube, args=(200, )) 
  
    # Ejecutando los procesos 
    p1.start() 
    p2.start() 
  
    # Esperando a que los procesos se completen 
    p1.join() 
    p2.join() 
  
    # Imprimiendo un mensaje 
    print("Se completaron los procesos")
