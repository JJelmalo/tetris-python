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
seccion_bn = [pix_bn for _ in list(range(10))]

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
            "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔳", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔳", "🔲", "🔲", "🔳", "🔲", "🔲", "🔳", "🔳")

screen_2 = ("🔲", "🔲", "🔲", "🔲", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲",
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
            "🔲", "🔲", "🔲", "🔳", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔳", "🔲", "🔲", "🔳", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔳", "🔲", "🔲", "🔳", "🔳", "🔲", "🔲", "🔲", "🔳", "🔲",
            "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳")



# Creamos una matriz con los indices de la screen.
matriz = []
fila = []

for row in range(0, 20):
    for elem in range(0, 10):
        n = row * 10
        fila.append(elem + n)
    if len(fila) == 10:
        matriz.append(fila)
        fila = []

matriz.reverse()




import threading
from random import randint, choice, choices
import time

import main, recursos


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

    # Relativo a la alteracion de la lista de colision
    print(lista_colision)
    lista_colision = list(filter(lambda x: lista_colision.remove(x) if x in list(range(191, 201)) else None, lista_colision))
    print(lista_colision)

    return tuple(seccion), lista_colision



def filas_mejorada(screen:tuple):

    # Creamos una matriz con los indices de la screen.
    matriz = []
    fila = []

    for row in range(0, 20):
        for elem in range(0, 10):
            n = row * 10
            fila.append(elem + n)
        if len(fila) == 10:
            matriz.append(fila)
            fila = []

    matriz.reverse()
    #print(matriz)

    # Comprobamos fila por fila, comenzando por la ultima, si estan completas
    row = []
    for ind, fila in enumerate(matriz):
        for elem in fila:
            if screen[elem] == pix_ng:
                row.append(True)
            else:
                row.append(False)
        if all(row):
            return True, ind
        else:
            row = []

    return False


# Elimina y contabiliza las filas completas
def come_filas_mejorado(screen:tuple, indice:int, lista_colision:int)->tuple:
    #print("Inicio")
    #print("screen original")
    #main.pantalla_prueba([], screen)
    screen = list(screen)
    #screen.reverse()
    #print("screen al reves")
    #main.pantalla_prueba([], screen)

    # Creamos una matriz a partir de screen
    screen_x_filas = []
    fila = []

    for elem in screen:
        fila.append(elem)
        if len(fila) == 10:
            screen_x_filas.append(fila)
            fila = []
    #print("\nscreen_x_filas recien creada", screen_x_filas)
    screen_x_filas.reverse()
    #print("screen_x_filas al reves", screen_x_filas)


    # Borramos la fila respectiva en la matriz gemela de screen. Y añadimos una fila en blanco por arriba
    screen_x_filas.pop(indice)
    screen_x_filas.reverse()
    #print("\nscreen_x_filas despues de eliminar las filas completas", screen_x_filas)
    screen_x_filas.insert(0, seccion_bn)
    #print("\nscreen_x_filas despues de insertar las filas en blanco", screen_x_filas)

    # Volvemos a convertir la matriz en una tupla. 
    screen = []
    for fila in screen_x_filas:
        for elem in fila:
            screen.append(elem)
    main.pantalla_prueba([], screen)

    # Actualizamos la lista de colision, apartir de la matriz de valores. El indice parte de una matriz al reves, por lo que hay que tenerlo en cuenta
    indices_colision = matriz[indice]
    print(indices_colision)
    print(lista_colision)
    for x in indices_colision:
        lista_colision.remove(x)
    # indices a actualizar en lista de colision:
    n = min(matriz[indice])
    nueva_lista_colision = list(map(lambda x: x+10 if x < n else None, lista_colision))
 
    print(lista_colision)

    #print(len(screen), screen)
    return tuple(screen), nueva_lista_colision


# NOTAS a eliminacion de filas:
#   . Todo funciona aparentemente correctamente excepto una cosa.
#   . Al eliminar una fila completa, si esta tiene cuadros negros por encima de dicha fila, aunque visualmente se corran uno para abajo, 
#   no lo hacen en la lista de colision, donde siguen manteniendo los indices previos.
#   . Habria que correrlos todos uno para abajo (+10). Todos los que esten por encima de esa linea.
#   . Esto hay que implementarlo en la funcion come_filas_mejorado, en el apartado de actualizacion de lista de colision.


        
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
# Hemos añadido un marcador del lado, porque empezo a dar problemas en derecho tambien Pero ha dejado de darlos. Si reaparecen desarrollo 
# la correcion en el lado derecho
def funcion_correctora(figura:dict, coordenadas_temporales:list, lado:bool)->list:

    # Datos
    #print()
    #print(figura)
    #print("Nombre:", figura["nombre"], " / ", "Posicion:", figura["posicion"])

    if figura["nombre"] == "L":
    # Margen izquierdo
        if lado is False:
            if figura['posicion'] == 1  or figura['posicion'] == 3:
                coordenadas_nuevas = map(lambda x: x+1, coordenadas_temporales)
                coordenadas_nuevas = list(coordenadas_nuevas)
                #print("coordenadas nuevas retornadas: ", coordenadas_nuevas)
                return coordenadas_nuevas
        
    elif figura["nombre"] == "recta":
    # Margen izquierdo
        if lado is False:
            if figura['posicion'] == 1:
                coordenadas_nuevas = map(lambda x: x+1, coordenadas_temporales)
                return list(coordenadas_nuevas)
    # Margen derecho
        if lado:
            if figura['posicion'] == 1:
                coordenadas_nuevas = map(lambda x: x-2, coordenadas_temporales)
                return list(coordenadas_nuevas)
        
    return coordenadas_temporales



#===============================================#

# MARCADOR

def marcador(count:int, acumulado):

    match count:
        case 1:
            multiplicador = 100
        case 2:
            multiplicador = 200
        case 3 | 4:
            multiplicador = 300
        case 5 | 6 | 7 | 8:
            multiplicador = 500


    resultado = multiplicador * count
    acumulado = acumulado + resultado

    return acumulado, resultado



#===============================================#

# GIRO 'L' INVERSA

L_inv = {"1ini" : (6, 16, 26, 25),
        "2ini" : (5, 15, 16, 17),
        "3ini" : (6, 7, 16, 26),
        "4ini" : (5, 6, 7, 17),}

# De la pos 0 a la pos 1:
(-1, -1, 10, -8)
# De la pos 1 a la pos 2:
(+1, -8, 0, +9)
# De la pos 2 a la pos 3:
(-1, -1, -9, -9)
# De la pos 3 a la pos 0:
(+1, +10, +19, +8)


# GIRO "cuatro"

cuatro = {"1ini" : (5, 6, 14, 15),
          "2ini" : (5, 15, 16, 26),}

# De la pos 0 a la pos 1:
(0, +9, +2, +11)
# De la pos 1 a la pos 0:
(0, -9, -2, -11)


# GIRO "cuatro_inv"

cuatro_inv = {"1ini" : (5, 6, 16, 17),
              "2ini" : (6, 15, 16, 25),}

# De la pos 0 a la pos 1:
(+1, +9, +0, +8)
# De la pos 1 a la pos 0:
(-1, -9, 0, -8)


# GIRO "verde"

verde = {"1ini" : (5, 14, 15, 16),
         "2ini" : (5, 15, 16, 25),
         "3ini" : (4, 5, 6, 15),
         "4ini" : (5, 14, 15, 25),}

# De la pos 0 a la pos 1:
(0, +1, +1, +9)
# De la pos 1 a la pos 2:
(-1, -10, -10, -10)
# De la pos 2 a la pos 3:
(+1, +9, +9, +10)
# De la pos 3 a la pos 0:
(0, 0, 0, -9)


# Funcion para probar los giros
def funcion_giros(coordenadas:tuple, posicion:int)->list:

    recursos.figuras['__|__']['posicion'] = posicion
    
    if recursos.figuras['__|__']["nombre"]=="__|__":
        nuevas_coordenadas = []
        if recursos.figuras['__|__']['posicion']==0:
            print("Coordenadas figura_prueba/__|__ posicion 0 a posicion 1: ", nuevas_coordenadas, " ... /posicion:", recursos.figuras['__|__']["posicion"])
            for indice, x in enumerate(coordenadas):
                if indice==0:
                    x = x+0
                    nuevas_coordenadas.append(x)
                elif indice==1:
                    x = x+1
                    nuevas_coordenadas.append(x)
                elif indice==2:
                    x = x+1
                    nuevas_coordenadas.append(x)
                elif indice==3:
                    x = x+9
                    nuevas_coordenadas.append(x)
            recursos.figuras['__|__']['posicion'] = 1
            return nuevas_coordenadas
    
        elif recursos.figuras['__|__']["posicion"]==1:
            print("Coordenadas figura_prueba/__|__ posicion 1 a posicion 2: ", nuevas_coordenadas, " ... /posicion:", recursos.figuras['__|__']["posicion"])
            for indice, x in enumerate(coordenadas):
                if indice==0:
                    x = x-1
                    nuevas_coordenadas.append(x)
                elif indice==1:
                    x = x-10
                    nuevas_coordenadas.append(x)
                elif indice==2:
                    x = x-10
                    nuevas_coordenadas.append(x)
                elif indice==3:
                    x = x-10
                    nuevas_coordenadas.append(x)
            recursos.figuras['__|__']['posicion'] = 2
            return nuevas_coordenadas
        
        elif recursos.figuras['__|__']["posicion"]==2:
            print("Coordenadas figura_prueba/__|__ posicion 1 a posicion 2: ", nuevas_coordenadas, " ... /posicion:", recursos.figuras['__|__']["posicion"])
            for indice, x in enumerate(coordenadas):
                if indice==0:
                    x = x+1
                    nuevas_coordenadas.append(x)
                elif indice==1:
                    x = x+9
                    nuevas_coordenadas.append(x)
                elif indice==2:
                    x = x+9
                    nuevas_coordenadas.append(x)
                elif indice==3:
                    x = x+10
                    nuevas_coordenadas.append(x)
            recursos.figuras['__|__']['posicion'] = 3
            return nuevas_coordenadas
        
        elif recursos.figuras['__|__']["posicion"]==3:
            print("Coordenadas figura_prueba/__|__ posicion 1 a posicion 2: ", nuevas_coordenadas, " ... /posicion:", recursos.figuras['__|__']["posicion"])
            for indice, x in enumerate(coordenadas):
                if indice==0:
                    x = x
                    nuevas_coordenadas.append(x)
                elif indice==1:
                    x = x
                    nuevas_coordenadas.append(x)
                elif indice==2:
                    x = x
                    nuevas_coordenadas.append(x)
                elif indice==3:
                    x = x-9
                    nuevas_coordenadas.append(x)
            recursos.figuras['__|__']['posicion'] = 0
            return nuevas_coordenadas

    
    return coordenadas



#===============================================#


# Funcion para la seleccion de nuevas piezas - reseteo
def salida():

    coordenadas = figura["1ini"]

    #return figura, coordenadas
    return coordenadas
    

# Funcion para la seleccion
def seleccion():

    figura = choice(list(recursos.figuras.items()))

    return figura[1]



#===============================================#


# Proyecto para la coreccion de la correccion de los giros de las rectas cuando estan pegadas a la izquierda

            # if len(list(filter(lambda x: x in limite_h_de_esp, coordenadas))) > 1 or len(list(filter(lambda x: x in limite_h_de, coordenadas))) > 1:
            #     for indice, x in enumerate(coordenadas):
            #         if indice == 0:
            #             nuevas_coordenadas.append(x)
            #         elif indice ==1:
            #             x = x - (10*indice+1)
            #             nuevas_coordenadas.append(x)
            #         elif indice ==2:
            #             x = (x+1) - (10*indice+1)
            #             nuevas_coordenadas.append(x)
            #         elif indice ==3:
            #             x = (x+2) - (10*indice+1)
            #             nuevas_coordenadas.append(x)


# CASO I
# Datos:
# Coordenadas figura_prueba/recta posicion 1 a posicion 0 al entrar:  [56, 57, 58, 59]  ... /posicion: 1
# Coordenadas figura_prueba/recta posicion 1 a posicion 0:  [57, 67, 77, 87]  ... /posicion: 0
#   . Punto de giro 58:                                     [58, 68, 78, 88]
# (+2, +11, +20, +29)

# Otros datos:
# Giro sin corregir: [39, 38, 39, 40] figura posicion: 1
# Nombre: recta  /  Posicion: 1  /  lado: True  /  coordenadas de entrada: [39, 38, 39, 40]
# Figura recta
# Lado derecho
# Casi Pegada [38, 37, 38, 39]
# Pegada [37, 36, 37, 38]


#===============================================#

# PROXIMA MEJORA:

#   . El giro de las rectas cuando estan en posicion 1 a un cuadro del limite derecho. Se tendria que hacer desde la funcion que devuelve 
#   las coordenadas de los giros. Con un testigo exportado de la funcion que controla los limites horizontales, o relizando el propio control 
#   previo cada vez que gira en la funcion de giro.
#   . ¿Añadir la proxima pieza en salir?
#       1. Podria dividir el codigo/funcionalidad la funcion salida en dos, una que seleccione la figura (proxima) y otra que devuelva las 
#       las coordenadas.
#       2. Se trata de seleccionar la siguiente figura antes de la fase de comienzo o al final de la misma.
#       3. Podria crear una funcion a modo de testigo para indicar el cambio y seleccion de nuevas piezas. Esta funcion introducida por un 
#       por un condicional seria sleeccionada por la funcion encargada de las selecciones y dibujada por la funcion encargada del dibujo.
#   . Mejorar visualmente el marcador

# Bugs:
#   . Posible bug con los margenes de los cuadrados al colocarlos


#===============================================#

# Otra excepcion



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
    #booleano, indice = filas_mejorada(screen_2)
    #print(booleano)
    #pantalla = come_filas_mejorado(screen_2, indice, [190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 184, 174])
    #print(type(pantalla), len(pantalla))
    #print(pantalla)

    # Representacion de los giros en pantalla
    # main.pantalla_prueba(verde["1ini"], main.screen)
    # coordenadas = funcion_giros(verde["1ini"], 0)
    # main.pantalla_prueba(coordenadas, main.screen)
    # coordenadas = funcion_giros(verde["2ini"], 1)
    # main.pantalla_prueba(coordenadas, main.screen)
    # coordenadas = funcion_giros(verde["3ini"], 2)
    # main.pantalla_prueba(coordenadas, main.screen)
    # coordenadas = funcion_giros(verde["4ini"], 3)
    # main.pantalla_prueba(coordenadas, main.screen)

    figura = seleccion()
    coordenadas = salida()
    print(coordenadas)
    print(figura)






# Ejemplo de fliter(), filtrando.
    # a = [1, 2, 3, 4]
    b = [10, 8, 6, 4]
    c = [9, 19, 29, 39]
    d = [-17, -18, 19, 20]
    lista = [10, 9, 8, 7, 6, 5, 4]
    #if b == lista:
    #    print("yes")
    #print(b==lista)
    #print(main.limite_h_de_esp)
    # if len(list(filter(lambda x: x in main.limite_h_de_esp, c))) > 1:
    #     print("YES")

    # b = list(filter(lambda x: x in lista, a))
    # print(b)

