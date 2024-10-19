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


#===============================================#

# Bugfix giro de figuras
"""
Reporte de una linea cayendo tumbada:
    Rango de colision [176, 184, 185, 186]
    Coordenadas [24, 25, 26, 27]
    []
    Coordenadas en calculo de movimiento:  [24, 25, 26, 27]
    Giro: [23, 15, 7, -1]
"""
"""
Reporte de una linea cayendo recta (mas informacion) en su primer giro:
    Rango de colision [165, 175, 185, 186, 155, 156, 166, 176, 161, 171, 181, 182]
    Coordenadas [15, 25, 35, 45]
    []
    Coordenadas en calculo de movimiento:  [15, 25, 35, 45]
    Coordenadas en la funcion figura_prueba:  [15, 25, 35, 45]
    Coordenadas figura_prueba/recta posicion 0:  [14, 15, 16, 17]
    Giro: [14, 15, 16, 17]
    Coordenadas en calculo de movimiento:  [14, 15, 16, 17]
    Coordenadas en la funcion figura_prueba:  [14, 15, 16, 17]
    Coordenadas figura_prueba/recta posicion 0:  [13, 5, -3, -11]
    Giro: [13, 5, -3, -11]
    Coordenadas en calculo de movimiento:  [13, 5, -3, -11]
    Coordenadas en la funcion figura_prueba:  [13, 5, -3, -11]
    Coordenadas figura_prueba/recta posicion 0:  [12, -5, -22, -39]
    Giro: [12, -5, -22, -39]
"""

# Notas al segundo reporte:

#   - El error se produce dentro de la funcion, las coordenadas recibidas son correctas. El error esta en el propio calculo de la nuevas coord.
#   - Hay un primer giro correcto, con coordenadas entrantes (recta) [15, 25, 35, 45], y salientes [14, 15, 16, 17] (tumbada). Este giro no 
#   a ser representado, porque la presion del teclado ha sido demasiado rapida.

#   Nota: quizas habria que plantearse el cambio en la secuencia de representacion a cada cambio en las coordernas (¿llamada a funcion 
#   pantalla_prueba?). ¿Con alguno tipo de lock en el acceso a usodicha funcion?. Previo backup de toda el bucle de la secuencia, incluso quizas
#   del propio archivo main.py (o confio en el respaldo de git?)

#      coordenadas de pie[0] [15, 25, 35, 45]                                 --- de pie. Transicion correcta: [-1, -10, -21, -32]
#      coordenadas entrantes: [14, 15, 16, 17]                             --- tumbada
#      coordenadas despues de aplicar la formula giro[1]: [13, 5, -3, -11]    --- de tumbada a de pie
#      indices aplicados entre ambas coordenadas: [-1, -10, -13, -6]  


#===============================================#

# Funcion correctora en los giros pegados al limites horizontal izquierdo.
# Hay una malfuncion en algunos giros. Habra que cribar por giros.
def funcion_correctora(figura:dict, coordenadas_temporales:list)->list:

    # Datos
    print()
    print(figura)
    print("Nombre:", figura["nombre"], " / ", "Posicion:", figura["posicion"])

    if figura["nombre"] == "L":
        if figura['posicion'] == 1  or figura['posicion'] == 3:
            coordenadas_nuevas = map(lambda x: x+1, coordenadas_temporales)
            coordenadas_nuevas = list(coordenadas_nuevas)
            print("coordenadas nuevas retornadas: ", coordenadas_nuevas)
            return coordenadas_nuevas
        
    elif figura["nombre"] == "recta":
        if figura['posicion'] == 1:
            coordenadas_nuevas = map(lambda x: x+1, coordenadas_temporales)
            return list(coordenadas_nuevas)
        
    return coordenadas_temporales



#===============================================#

# Otra excepcion




# Rango de colision []
# Coordenadas [21, 22, 23, 24]
# []
# VUELTA:  47
# Coordenadas en calculo de movimiento:  [21, 22, 23, 24]
# Limite_figura_horizontal: [21, 22, 23, 24], 5, False
# Limite horizontal izquierdo:  [11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]
# Limite_figura_horizontal: [21, 22, 23, 24], 5, True
# Limite horizontal izquierdo:  [11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]
# Confirmado giro pegado al limite izquierdo
# Coordenadas en la funcion figura_prueba:  [21, 22, 23, 24]
# Coordenadas figura_prueba/recta posicion 1 a posicion 0:  [22, 32, 42, 52]
# Giro sin corregir: [22, 32, 42, 52] figura posicion: 0

# {'nombre': 'recta', '1': [['🔳'], ['🔳'], ['🔳'], ['🔳']], '2': ['🔳', '🔳', '🔳', '🔳'], '1ini': (5, 15, 25, 35), '2ini': (4, 5, 6, 7), 'coef_giro': 10, 'eje_giro': 0, 'posicion': 0, 'posiciones': 2, 'coordenadas': [<class 'int'>, <class 'int'>, <class 'int'>, <class 'int'>]}
# Nombre: recta  /  Posicion: 0
# Giro sin corregir: [22, 32, 42, 52]   ....   Giro corregido: None
# Exception in thread Thread-4 (teclado):
# Traceback (most recent call last):
#   File "C:\Users\Antonio J\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1075, in _bootstrap_inner
#     self.run()
#   File "C:\Users\Antonio J\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1012, in run
#     self._target(*self._args, **self._kwargs)
#   File "c:\Pruebas\PROGRAMACION\Repositorios\Tetris\main.py", line 576, in teclado
#     coordenadas = calculo_movimiento_hilo(coordenadas, recursos.Movimiento.GIRO)
#                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "c:\Pruebas\PROGRAMACION\Repositorios\Tetris\main.py", line 547, in calculo_movimiento_hilo
#     a = filter(lambda x: x if x > 200 else None, coordenadas_nuevas)
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: 'NoneType' object is not iterable


# Rango de colision []
# Coordenadas [1, 2, 3, 11]
# []
# VUELTA:  13
# Coordenadas en calculo de movimiento:  [1, 2, 3, 11]
# Limite_figura_horizontal: [1, 2, 3, 11], 5, False
# Limite horizontal izquierdo:  [11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]
# Limite_figura_horizontal: [1, 2, 3, 11], 5, True
# Limite horizontal izquierdo:  [11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]
# Confirmado giro pegado al limite izquierdo
# Coordenadas en la funcion figura_prueba:  [1, 2, 3, 11]
# 1
# Giro sin corregir: [2, 3, 13, 23] figura posicion: 2

# {'nombre': 'L', '1': [['🔳'], ['🔳'], ['🔳', '🔳']], '2': [['🔳', '🔳', '🔳'], ['🔳']], '3': [['🔳', '🔳'], ['🔳'], ['🔳']], '4': [['🔳'], ['🔳', '🔳', '🔳']], '1ini': (5, 15, 25, 26), '2ini': (4, 5, 6, 14), '3ini': (5, 6, 16, 26), '4ini': (6, 14, 15, 16), 'coef_giro': 10, 'eje_giro': 2, 'posicion': 2, 'posiciones': 4, 'coordenadas': [<class 'int'>, <class 'int'>, <class 'int'>, <class 'int'>]}
# Nombre: L  /  Posicion: 2
# Giro sin corregir: [2, 3, 13, 23]   ....   Giro corregido: None
# Exception in thread Thread-4 (teclado):
# Traceback (most recent call last):
#   File "C:\Users\Antonio J\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1075, in _bootstrap_inner
#     self.run()
#   File "C:\Users\Antonio J\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1012, in run
#     self._target(*self._args, **self._kwargs)
#   File "c:\Pruebas\PROGRAMACION\Repositorios\Tetris\main.py", line 576, in teclado
#     coordenadas = calculo_movimiento_hilo(coordenadas, recursos.Movimiento.GIRO)
#                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "c:\Pruebas\PROGRAMACION\Repositorios\Tetris\main.py", line 547, in calculo_movimiento_hilo
#     a = filter(lambda x: x if x > 200 else None, coordenadas_nuevas)
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: 'NoneType' object is not iterable




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



