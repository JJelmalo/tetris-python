"""
                                                                PRUEBAS

                                                                

                                                                
            I. Secuencia de los hilos interelacionados entre si

    - Lo he logrado de dos modos:
        . Usando una variable global, en la funcion que controla uno de los hilos. Cambiando su valor de True a False, podemos controlar el 
        bucle de la funcion que gestiona el funcionamiento del segundo hilo dandolo por terminado cuando quiero.
        . Usando el metodo join() en el primer hilo. Cuando éste acaba, el fulo principal se vuelve a poner en marcha en el momento que yo 
        quiero, e invocando una funcion creada a proposito pongo fin al segundo hilo sin usan variables globales, tan solo externas.

                                                                
"""



import threading
from random import randint
import time


# Esta funcion va a ser el hilo, controlada por la variable externa "controlador"
def funcion():

    while controlador:
        n = randint(0, 100)
        time.sleep(1)
        print(n)
        print(controlador)
    
    return print("Se acabo")


# Funcion de control. INNECESARIA.
def control(controlador):

    if controlador:
        print(f"Este es el cambio del controlador = {controlador}")
        controlador = False
        print(f"Este es el cambio del controlador = {controlador}")

    return controlador


# Funcion del segundo hilo. Gestiona controlador (como variable global), y por lo tanto la secuencia del bucle del otro hilo.
def temporizador():
    
    t = round(time.time() + 10)
    print(t)
    count = 0

    while True:
        t2 = round(time.time())
        if t2 >= t:
            print("ES CORRECTO")
            #global controlador
            #controlador = False
            break

# Este sera el codigo principal.
def programa():

    hilo1 = threading.Thread(target=temporizador)
    hilo2 = threading.Thread(target=funcion)
    hilo1.start()
    hilo2.start()
    print("Ha Comenzado\n")
    hilo1.join()
    

# funcion temporal para comprobar el movimiento en main.py.
def ordenes():
    print("""
\nPresione la letra 'a' para moverse a la izquierda.
Presione la letra 'd' para moverse a la derecha.
Presione la letra 's' para avanzar hacia abajo.
Presione la letra 'p' para girar la figura.
Presione cualquier otra tecka para salir del juego.
        """)
    
    x = input()

    if x == "a":
        movimiento = -1
        return movimiento
    elif x == "d":
        movimiento = 1
        return movimiento
    elif x == "s":
        movimiento = 0
        return movimiento
    elif x == "p":
        movimiento = 2
        return movimiento
    elif x == "g":
        movimiento = 5
        return movimiento
    else:
        print("Adios.")
        exit()




if __name__ == "__main__":

    controlador = True
    #programa()
    #print("BOOMMMMM!!!!!!!!!!!!!!!")
    #controlador = control(controlador)
    pass


