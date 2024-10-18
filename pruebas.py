"""
                                                                PRUEBAS

                                                                

                                                                
            I. Secuencia de los hilos interelacionados entre si

    - Lo he logrado de dos modos:
        . Usando una variable global, en la funcion que controla uno de los hilos. Cambiando su valor de True a False, podemos controlar el 
        bucle de la funcion que gestiona el funcionamiento del segundo hilo dandolo por terminado cuando quiero.
        . Usando el metodo join() en el primer hilo. Cuando éste acaba, el fulo principal se vuelve a poner en marcha en el momento que yo 
        quiero, e invocando una funcion creada a proposito pongo fin al segundo hilo sin usan variables globales, tan solo externas.

                                                                
"""

# RECURSOS TEMPORALES

# Pantalla
pix_bn = "🔲"
pix_ng = "🔳"

screen_1 = ("🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔳", "🔲", "🔲", "🔳", "🔲", "🔲", "🔳", "🔳")

screen_2 = ("🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳")






import threading
from random import randint
import time

import main


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



#==========================================#



# Borrar pantalla terminal:
import os
import platform

def borrado():

    print("iooooooooooooooooooooooooooooooooohaodhoa\n")
    print("iooooooooooooooooooooooooooooooooohaodhoa\n")
    print("iooooooooooooooooooooooooooooooooohaodhoa\n")
    print("iooooooooooooooooooooooooooooooooohaodhoa\n")
    print("iooooooooooooooooooooooooooooooooohaodhoa\n")
    print("iooooooooooooooooooooooooooooooooohaodhoa\n")
    print("iooooooooooooooooooooooooooooooooohaodhoa\n")
    print("iooooooooooooooooooooooooooooooooohaodhoa\n")
    print("iooooooooooooooooooooooooooooooooohaodhoa\n")
    print("iooooooooooooooooooooooooooooooooohaodhoa\n")
    print("iooooooooooooooooooooooooooooooooohaodhoa\n")
    print("iooooooooooooooooooooooooooooooooohaodhoa\n")
    print("iooooooooooooooooooooooooooooooooohaodhoa\n")
    print("iooooooooooooooooooooooooooooooooohaodhoa\n")

    if platform.system() == "Windows":
        os.system("cls")
        print("windows")
    else:
        print("Otros")
        os.system("clear")
        print("Otros")


#========================================

# Borrado de las lineas completas
#   Contabilizar. Puntuacion - llevar la cuenta - comunicarlo - eliminarlas - representar visualmente la eliminacion.
#   Tiene que verse como se hace
#   un condicional de filas, en en caso positivo un bucle que vaya contabilizando filas y eliminadolas.


# Esta funcion aisla la ultima fila y la valora. Devuelve un True/False (seria lo ideal), regulado por un bucle que contenga el codigo
# para ir 'comiendose' las filas y puntuandloas. Pero esto quizas cree problemas con los hilos y la gestion de la variable "coordenadas".
# Por lo que voy a intentar hacerlo todo o casi todo en la misma funcion.
def filas(screen:tuple)->bool:

    """
    b = []
    for ind,char in enumerate(screen):
        if ind in list(range(191, 201)):
            b.append(char)
    print(b)    
    """

    a = screen[190:199]
    c = map(lambda x: True if x == main.pix_ng else False, a)

    if all(c):
        return True
    else:
        return False
    

    # Quizas habria que parar ambos movimientos, quizas con una variable de control (True/False). Gestionada por filas().

    # Codigo para gestionar las filas completas
        # Habria que llamar a otra funcion que lleve el marcador
        # A otra que elimine las lineas completas y rehaga ecreen. Cada linea eliminada una a una para que se vea.
    while all(c):
        # Llamar a funcion marcador. Implemantar lo ultimo
        # Llamar a funcion que elimine las filas
        break


def come_filas(screen:tuple)->list:
    
    screen = list(screen)

    seccion = [pix_bn for _ in list(range(10))]
    #print(len(screen))

    for _ in list(range(10)):
        screen.pop()

    #print(len(screen))
    #print(screen)

    seccion.extend(screen)
    #print(len(seccion))
    #print(seccion)

    return tuple(seccion)

        
#========================================

# Bugfix para las coordenadas que se pasan al darle repetidamente a la tecla abajo
def prueba():
        
    coordenadas_nuevas = [175, 185, 195, 205]

    a = filter(lambda x: x if x > 200 else None, coordenadas_nuevas)
    if list(a):
        coordenadas_nuevas = map(lambda x: x-10, coordenadas_nuevas)
        print("CONTROL")
        return list(coordenadas_nuevas)

    else:
        return coordenadas_nuevas

#========================================

# Hay que elaborar un control para los movimientos auto y voluntario para que no se superpongan en las piezas estacionadas, ya que si 
# se pulsa repetidamente las teclas parece que sobre pasan el control diseñado para el movimiento por turnos.

# Es un control pasivo que fijaba la pieza despues de evaluar un movimiento por turnos, basandase en la posicion de la figuara en juego 
# y de la pieza colocada. Si la primera estaba en los margenes de la segunda, ésta tambien pasaba a estar colocada, filtrada por un condicional 


# Me puedo basar en el control pasivo existente en la funcion colision y en los que he diseñado para reconducir el exceso en los valores 
# de las coordenadas en la funcion claculo_movimiento_hilo.

# Introducido por un condicional referenciado a la funcion colision.
def control_invasion(coordenadas:list, indices:list) -> list:

    invasion = list(filter(lambda x: True if x in indices else False, coordenadas))

    while any(invasion):
        coordenadas = list(map(lambda x: x - 10, coordenadas))
        invasion = list(filter(lambda x: True if x in indices else False, coordenadas))
        if any(invasion):
            continue
        else:
            return coordenadas
        
    return coordenadas




#===============================================================================================================================================#




if __name__ == "__main__":

    controlador = True
    #programa()
    #print("BOOMMMMM!!!!!!!!!!!!!!!")
    #controlador = control(controlador)
    pass
    #print(prueba())
    print("\n"*2)
    #print(control_invasion([95, 105, 115, 125], [165, 175, 185, 195]))
    #print(filas(main.screen))
    print(type(come_filas(screen_2)))
