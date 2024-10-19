# Prueba tacnica de python: Tetris.



# Reglas:
#   Cuadricula de 10x10
#   Cada posicion representada por un cuadrado blanco
#   Cada pieza de tetris se forma con los cuadrados en negro (por contraste)
#   Las piezas tienen que tener la funcionalidad de una pieza de tetris.
# Link instrucciones: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2333%20-%20TETRIS%20%5BDif%C3%ADcil%5D/ejercicio.md


# Recursos:
#    🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
#    🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
#    🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#    🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#    🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#    🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#    🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#    🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#    🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#    🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲


# VALORACION GENERAL: comparandolo con la resolucion del ejercicio por Mauredev, todo es muy parecido. Lo mas relevante es la coincidencia 
# en las mecanicas de rotacion.
# Hay cosas positivas que he aprendido como ha ointroducir mas las funciones superiores y trucos al usarlas. O la clase Enum, o el uso de 
# match/case, pero por lo demas todo es muy parecido.

# Nota: Mauredev usa para representar el pantalla, una lista anidada que simula una matriz 2D, como yo hice en el primer intento, pero termine 
# simplificandola porque aunque sea mas realista, es menos funcional en su traslacion a python. Quzias usando la libreria de pandas y/o numpy, 
# si seria mejor hacerlo cun matriz 2D.


# C: Pruebas/PROGRAMACION/Repositorios/Tetris





from getpass import getpass
from random import randint

import recursos, mov_teclado, pruebas
#import mov_auto

import time
import threading
import enum
import os
import keyboard

#from pruebas import ordenes



# variables externas (inmutables)
pix_bn = "🔲"
pix_ng = "🔳"

dimensiones_pantalla = [20, 10]
largo = dimensiones_pantalla[0]
ancho = dimensiones_pantalla[1]

screen = [pix_bn for _ in range(1, 201)]
seccion = [pix_bn for _ in list(range(10))]

evento_1 = threading.Event()


#=======================================#


# BLOQUE PARA LA REPRESENTACION


# Fija las figuras terminadas a la pantalla
def pantalla_pix(coordenadas:list, screen:tuple)->tuple:
    
    screen = list(screen)

    imagen = ""

    print("Coordendas de patalla_pix: ", coordenadas)

    # Creando la imagen en la pantalla (lista)
    for elemento in coordenadas:
        screen.pop(elemento-1)
        screen.insert(elemento-1, pix_ng)
    #print(screen)
    count = 1
    for caracter in screen:
        if count == 10:
            imagen = imagen + caracter + "\n"
            count = 0
        else:
            imagen = imagen + caracter
        count += 1

    return tuple(screen)

    

def pantalla_prueba(coordenadas:list, screen:tuple):
    'Dibuja la figura en la pantalla'

    # Borramos la pantalla
    #os.system("cls")

    # Creamos la pantalla en blanco-scream y asi nos evitamos pasarla por parametro. Usamos el guion bajo.
    screen = list(screen)
    #for i in range(1, 201):
    #    if i//10 == int:
    #        screen.append("🔲\n")
    #    else:
    #        screen.append("🔲")

    #print(screen)

    # Adaptaciones de los parametros
    #screen = list(screen)
    imagen = ""

    # Creando la imagen en la pantalla (lista)
    for elemento in coordenadas:
        try:
            screen.pop(elemento-1)
            screen.insert(elemento-1, pix_ng)
        except IndexError as exc:
            print(f"Elemento: {elemento}, len screen: {len(screen)}")
            print("Las coordenadas:", coordenadas)
            print(exc)
    #print(screen)
    count = 1
    for caracter in screen:
        if count == 10:
            imagen = imagen + caracter + "\n"
            count = 0
        else:
            imagen = imagen + caracter
        count += 1
    print(imagen)


#=======================================#


# BLOQUE PARA LA GESTION DE LAS FIGURAS


# Funcion para la seleccion de nuevas piezas
def salida(figuras:dict) -> dict:

    lista = list(figuras.keys())
    indice = randint(0, (len(lista))-1)
    figura = figuras[lista[indice]]

    return figura


# Funcion de dibujado en patalla
def figura_prueba(figura:dict, coordenadas=[]):
    "gestiona la selecion de figuras y sus coordenadas al principio del turno, incluyendo la gestion de los giros"

    # Seleccion de figura - Nueva figura
    #if reinicio:
    #    print("reniciuo")
    #    figuras = figuras
    #    lista = list(figuras.keys())
    #    indice = randint(0, (len(lista))-1)
    #    figura = figuras[lista[indice]]
    #    figura["posicion"] = 1
    #    return list(figura["1ini"])


    # Formulas para la automaticion del despliegue de las figuras (obtencion de los indices automaticos).
    # formula para que halle posicion absoluta de cualquier figura, definida sus elementos en indices
    #n_elem = len(figura)
    #posicion = figura["posicion"]       
    #postura = figura[posicion]              # Despliegue "actual" de la figura
    #coordenadas = list(figura['1ini'])          # Es temporal. Uso las coordenadas de salida
    #dimensiones = [len(x) for x in postura] # Las dimensiones por fila

    # Giro
    # Giran un coeficiente que se suma a los elmentos. Gira sobre un eje que es un elmeneto que no cambia su coordenada. Y giran en una 
    # direccion, que esta definida en + ó - segun el punto en el eje de ordenadas (mitad de las posiciones +, mitad negativo).
    figura = figura
    print("Coordenadas en la funcion figura_prueba: ", coordenadas)
    if coordenadas: 
        if figura["nombre"]=="recta":
            nuevas_coordenadas = []
            if figura['posicion']==1:
                for indice, x in enumerate(coordenadas):
                    if indice == 0:
                        nuevas_coordenadas.append(x+1)
                    elif indice ==1:
                        x = x + (10*indice)
                        nuevas_coordenadas.append(x)
                    elif indice ==2:
                        x = (x-1) + (10*indice)
                        nuevas_coordenadas.append(x)
                    elif indice ==3:
                        x = (x-2) + (10*indice)
                        nuevas_coordenadas.append(x)
                figura['posicion'] = 0
                print("Coordenadas figura_prueba/recta posicion 1 a posicion 0: ", nuevas_coordenadas)
                return nuevas_coordenadas
            
            elif figura['posicion']==0:
                for indice, x in enumerate(coordenadas):
                    if indice == 0:
                        nuevas_coordenadas.append(x-1)
                    elif indice ==1:
                        x = x - (10*indice)
                        nuevas_coordenadas.append(x)
                    elif indice ==2:
                        x = (x+1) - (10*indice)
                        nuevas_coordenadas.append(x)
                    elif indice ==3:
                        x = (x+2) - (10*indice)
                        nuevas_coordenadas.append(x)
                figura['posicion'] = 1
                print("Coordenadas figura_prueba/recta posicion 0 a posicion 1: ", nuevas_coordenadas)
                return nuevas_coordenadas
    
        elif figura["nombre"]=="L":
            nuevas_coordenadas = []
            if figura['posicion']==0:
                print(0)
                for indice, x in enumerate(coordenadas):
                    if indice==0:
                        x = x-1
                        nuevas_coordenadas.append(x)
                    elif indice==1:
                        x = x-10
                        nuevas_coordenadas.append(x)
                    elif indice==2:
                        x = x-19
                        nuevas_coordenadas.append(x)
                    elif indice==3:
                        x = x-12
                        nuevas_coordenadas.append(x)
                figura['posicion'] = 1
                return nuevas_coordenadas
    
            elif figura["posicion"]==1:
                print(1)
                for indice, x in enumerate(coordenadas):
                    if indice==0:
                        x = x+1
                        nuevas_coordenadas.append(x)
                    elif indice==1:
                        x = x+1
                        nuevas_coordenadas.append(x)
                    elif indice==2:
                        x = x+10
                        nuevas_coordenadas.append(x)
                    elif indice==3:
                        x = x+12
                        nuevas_coordenadas.append(x)
                figura['posicion'] = 2
                return nuevas_coordenadas
            
            elif figura["posicion"]==2:
                print(2)
                for indice, x in enumerate(coordenadas):
                    if indice==0:
                        x = x+1
                        nuevas_coordenadas.append(x)
                    elif indice==1:
                        x = x+8
                        nuevas_coordenadas.append(x)
                    elif indice==2:
                        x = x-1
                        nuevas_coordenadas.append(x)
                    elif indice==3:
                        x = x-10
                        nuevas_coordenadas.append(x)
                figura['posicion'] = 3
                return nuevas_coordenadas
            
            elif figura["posicion"]==3:
                print(2)
                for indice, x in enumerate(coordenadas):
                    if indice==0:
                        x = x-1
                        nuevas_coordenadas.append(x)
                    elif indice==1:
                        x = x+1
                        nuevas_coordenadas.append(x)
                    elif indice==2:
                        x = x+10
                        nuevas_coordenadas.append(x)
                    elif indice==3:
                        x = x+10
                        nuevas_coordenadas.append(x)
                figura['posicion'] = 0
                return nuevas_coordenadas
            
    else:
        coordenadas = figura['1ini']
        return list(coordenadas)


#=======================================#


# BLOQUE DE COLISION Y LIMITES


def limites_figura_horizontal(coordenadas:list, movimiento:int, giro:bool)->bool:
    
    limite_h_de = [x for x in range(1, ancho*largo+1) if x%10 == 0]  # ¿filter?
    limite_h_iz = [x+1 for x in limite_h_de if x<200]             # ¿map?
    print(f"Limite_figura_horizontal: {coordenadas}, {movimiento}, {giro}")
    print("Limite horizontal izquierdo: ", limite_h_iz)
    #print(limite_h_de)

    # Comprobacion de los limites en los movimientos:
    if giro is False:
        for coordenada in coordenadas:
            if coordenada in limite_h_de and movimiento == 1:
                return True
            elif coordenada in limite_h_iz and movimiento == -1:
                return True
        return False
    
    # Comprobacion en los giros pegados al limite horizontal izquierdo:
    else:
        for coordenada in coordenadas:
            if coordenada in limite_h_iz and movimiento == 5:
                print("Confirmado giro pegado al limite izquierdo")
                return True
        return False
        
    
# Funcion para obtener las coordenadas de las piezas colocadas.
def indices_colision(coordenadas:list, screen:tuple, indices:list) -> list:

    """
    if pix_ng not in screen:
        print("lista de colisiones", indices)
        return indices
    
    indices_pix_ng = []
    for indice,x in enumerate(screen):
        if x == pix_ng:
            indices_pix_ng.append(indice+1)
    """
    nuevos_indices = coordenadas.copy()
    lista_colision = indices + nuevos_indices
    #print("Indice_pix_ng", indices_pix_ng)
    print("lista de colision", lista_colision)

    return lista_colision
        

# Comprueba si las coordenadas de la figura estan pegadas (a 10 indices/pixeles) de las figuras estacionadas
def colision(coordenadas:list, lista_colision:list)->bool:

    rango_colision = list(map(lambda x: x-10, lista_colision))
    #rango_colision = list(rango_colision)
    print("Rango de colision", rango_colision)
    print("Coordenadas", coordenadas)
    #print("BOLEANO", any(coordenadas == list(rango_colision)))
    print(list(filter(lambda x: x in rango_colision, coordenadas)))

    if list(filter(lambda x: x in rango_colision, coordenadas)):
        print("Is True")
        return True
    
    else:
        return False
    

# Funcion para evitar que la figura en juego se monte sobre las piezas ya colocadas. Compara las coordenadas de la piezs en juego con las 
# estacionadas (lista de colision)
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


# Funcion para comprobar si la figura en juego ha llegado al limite del tablero. Compara las coordenadas con una lista de indices del limite 
# del tablero (limite_v)
def limites_vertical(coordenadas:list)->bool:

    limite_v = [x for x in range(191,201)]
    #print(coordenadas)
    #print(limite_v)

    # Comprovacion limites verticales
    for coordenada in coordenadas:
        if coordenada in limite_v:
            return True
        
    return False


#=======================================#


# HILO PARA EL MOVIMIENTO AUTOMATICO

# el codigo del movimiento automatico. Los parametros no son necesarios, pero de momento los mantengo para facilitar el trasiego de datos.
def cod_mov_auto(coordenadas:list, ancho:int):
    
    coordenadas_nuevas = [x + ancho for x in coordenadas]

    # Hay que poner AQUI, un control a las coordenadas en su limite vertical. Si se pulsa repetidamente "abajo", se pueden llegar a enviar 
    # coordenadas que superen el len de screen.
    a = filter(lambda x: x if x > 200 else None, coordenadas_nuevas)
    if list(a):
        coordenadas_nuevas = map(lambda x: x-10, coordenadas_nuevas)
        print("CONTROL AUTO", coordenadas_nuevas)
        return list(coordenadas_nuevas)
    
    return coordenadas_nuevas


def mov_auto():

    # Control:
    while not cerrojo:
        evento_1.wait()

    t = 1
    count = 1

    global coordenadas
    global control
    
    while True:
        time.sleep(2)
        coordenadas = cod_mov_auto(coordenadas, ancho)
        if control:
            exit()
        
        # seguro
        #count += 1
        #if count > 5:
        #    break


#=======================================#


# MOVIMIENTO VOLUNTARIO
# Incluye el calculo de los limites laterales (horizontales)


# Funcion para el calculo por turno. Estaria complementado por la funcion teclado del modulo mov_teclado.py que daria contenido 
# a las ordenes (ord).
# Calcula las coordenadas despues de cada movimiento
"""
def calculo_movimiento(coordenadas:list, movimiento:recursos.Movimiento):
    "Incluye el movimiento ordenado y el automatico"

    # Comprobacion de los limites horizontales
    if limites_figura_horizontal(coordenadas, movimiento):
        return coordenadas

    # Indices para calculo del movimiento vertical y horizontal.
    n = movimiento # o -1. Es la direccion del movimiento
    match movimiento:
        case recursos.Movimiento.DERECHA:
            # movimiento horizontal derecha
            coordenadas_nuevas = [x + n for x in coordenadas]
        case recursos.Movimiento.IZQUIERDA:
            # movimiento horizontal izquierda
            coordenadas_nuevas = [x + n for x in coordenadas]
        case recursos.Movimiento.ABAJO:
            # movimiento vertical
            coordenadas_nuevas = [x + ancho for x in coordenadas]
        case recursos.Movimiento.GIRO:
            # giro de la figura
            coordenadas_nuevas = figura_prueba(figura, coordenadas)
        #case recursos.Movimiento.SALIDA:
        #    print("\nADIOS")
        #    exit()

    # Control de colision
    #if colision(coordenadas_nuevas,screen):
        #return coordenadas, True

    # Retorna las coordenadas de la figura una vez aplicado el movimiento
    return coordenadas_nuevas
"""


# Bloque adaptada al procesamiento mediante hilos
def calculo_movimiento_hilo(coordenadas:list, movimiento:recursos.Movimiento):
    "Incluye el movimiento ordenado y el automatico"

    print("Coordenadas en calculo de movimiento: ", coordenadas)

    # Variable de control para salir
    global control

    # Comprobacion de los limites horizontales
    if limites_figura_horizontal(coordenadas, movimiento, giro=False):
        #print("Limite horizontal activado. Movimiento = ", movimiento)
        return coordenadas

    # Indices para calculo del movimiento vertical y horizontal.
    n = movimiento # o -1. Es la direccion del movimiento
    match movimiento:
        case recursos.Movimiento.DERECHA:
            # movimiento horizontal derecha
            coordenadas_nuevas = [x + n for x in coordenadas]
        case recursos.Movimiento.IZQUIERDA:
            # movimiento horizontal izquierda
            coordenadas_nuevas = [x + n for x in coordenadas]
        case recursos.Movimiento.ABAJO:
            # movimiento vertical
            coordenadas_nuevas = [x + ancho for x in coordenadas]
        case recursos.Movimiento.GIRO:
            # Comprobacion de los limites horizontales izquierdos en los giros:
            if limites_figura_horizontal(coordenadas, movimiento, giro=True):
            # giro de la figura
                coordenadas_temporales = figura_prueba(figura, coordenadas)
                print("Giro sin corregir:", coordenadas_temporales, f"figura posicion: {figura["posicion"]}")
                coordenadas_nuevas = pruebas.funcion_correctora(figura, coordenadas_temporales)

                #coordenadas_nuevas = list(map(lambda x: x+1, coordenadas_temporales))
                print(f"Giro sin corregir: {coordenadas_temporales}   ....   Giro corregido: {coordenadas_nuevas}")
            else:
                coordenadas_nuevas = figura_prueba(figura, coordenadas)
                print("Giro limpio:", coordenadas_nuevas)
        case recursos.Movimiento.SALIDA:
            print("\nADIOS")
            control = True
            exit()

    # Hay que poner AQUI, un control a las coordenas en su limite vertical. Si se pulsa repetidamente "abajo", se pueden llegar a enviar 
    # coordenadas que superen el len de screen.
    a = filter(lambda x: x if x > 200 else None, coordenadas_nuevas)
    if list(a):
        coordenadas_nuevas = map(lambda x: x-10, coordenadas_nuevas)
        print("CONTROL VOLUNTARIO")
        return list(coordenadas_nuevas)

    # Retorna las coordenadas de la figura una vez aplicado el movimiento
    return coordenadas_nuevas


# Funcion gestion llamada del teclado
def teclado():

    # Control:
    while not cerrojo:
        evento_1.wait()

    global coordenadas

    while True:
        evento = keyboard.read_event()
        if evento.event_type == keyboard.KEY_DOWN:
            if evento.name == "a":
                coordenadas = calculo_movimiento_hilo(coordenadas, recursos.Movimiento.IZQUIERDA) 
            elif evento.name == "d":
                coordenadas = calculo_movimiento_hilo(coordenadas, recursos.Movimiento.DERECHA)
            elif evento.name == "s":
                coordenadas = calculo_movimiento_hilo(coordenadas, recursos.Movimiento.ABAJO)
            elif evento.name == "p":
                coordenadas = calculo_movimiento_hilo(coordenadas, recursos.Movimiento.GIRO)
            elif evento.name == "esc":
                coordenadas = calculo_movimiento_hilo(coordenadas, recursos.Movimiento.SALIDA)


#=======================================#


def logica():
    "coordina todo, enviando los parametros al resto de funciones"
    pass







#================================================================================#



if __name__ == "__main__":

# Variables importantes:
    # coordenadas
    # figura

# Secuencia principal: voy a tratar de aislar los procesos de movimiento automatico y moviento con teclas en su minima expresion en sus 
#                      respectivos hilos, dejando la secuencia principal del bucle en main.py.
#                      Lo suyo seria arrancar los hilos desde el bucle principal. 
    
    hilos = True
    comienzo = True
    lista_colision = []
    count = 0
    control = False
    cerrojo = True


    # Cabecera
    os.system("cls")
    print("\n"*3)
    print("\t"*8 + "#"*20)
    print("\t"*8 + "##" + " "*16 + "##")
    print("\t"*8 + "##" + " "*5 + "TETRIS" + " "*5 + "##")
    print("\t"*8 + "##" + " "*16 + "##")
    print("\t"*8 + "#"*20)
    print("\n"*5)

    print("Pulse la tecla 'INTRO' para continuar")
    print("Para abandonar el juego pulse la tecla 'ESC' en cualquier momento")
    print("\n"*3)
    while True:
        empezar = keyboard.read_event()
        if empezar.name == 'enter':
            break



    while True:

        # Bloque de inicio/reinicio
        if comienzo:
            print("COMIENZO")
            figura = salida(recursos.figuras)
            comienzo = False
            #fijacion = False
            coordenadas = figura_prueba(figura)
            #print(coordenadas)

        # Bloque de pantalla: Quizas lo suyo seria que se refrescara solo haya cambios en coordenadas, en vez de un sleep().
        time.sleep(0.5)
        pantalla_prueba(coordenadas,screen)
        
        # Este es el bloque de ordenes en turno por turno:
        #print(coordenadas)
        #ord = recursos.ordenes()
        #print(coordenadas)
        #coordenadas = calculo_movimiento(coordenadas, ord)
        #==========================================#
        
        # Bloque de hilos. Solo una vez
        cerrojo = True
        if hilos:
            hilo_auto = threading.Thread(target=mov_auto)
            hilo_teclado = threading.Thread(target=teclado)
            #hilo_auto.start()
            hilo_teclado.start()
            hilos = False
            print("HILOS")

        #===========================================#

        # Bloque moviento por teclado por turnos
        #ord = mov_teclado.teclado()
        #coordenadas = calculo_movimiento(coordenadas, ord)

        # Bloque de control
        if limites_vertical(coordenadas) or colision(coordenadas, lista_colision):
            print("CONTROLES")
            cerrojo = False                                                             # Variable de control de los eventos para los hilos
            coordenadas = control_invasion(coordenadas, lista_colision)
            screen = pantalla_pix(coordenadas, screen)
            lista_colision = indices_colision(coordenadas, screen, lista_colision)
            comienzo = True
            # Aqui iria el condicional para controlar la filas resueltas
            while pruebas.filas(screen):
                screen = pruebas.come_filas(screen)
                pantalla_prueba(coordenadas, screen)
                time.sleep(1.5)
                count += 1
            if count:
                pass
                count = 0

        # Control
        if control:
            print("\n\n\n\t\t\t\t\t\t############# GRACIAS POR JUGAR ##############")
            break


        # seguro
        print("VUELTA: ", count)
        count += 1
        #if count > 5:
        #    break

        # Bloque complementario en turno por turno
        #print(coordenadas)
        #pantalla_prueba(coordenadas, screen)
        #print(coordenadas)
    
"""
figura = salida(recursos.figuras)
print(figura)
coordenadas = figura_prueba(figura)
print(coordenadas)
pantalla_prueba(coordenadas, screen)
coordenadas = figura_prueba(figura, coordenadas)
print(coordenadas)
pantalla_prueba(coordenadas, screen)
"""


# Coordenadas en rotacion de las figuras

# (5, 15, 25, 26)
# (4, 5, 6, 14)
# (5, 6, 16, 26)
# (6, 14, 15, 16)

# (5, 15, 25, 35)
# (4, 5, 6, 7)
# -1, -10, -19, -28

print(2//10)