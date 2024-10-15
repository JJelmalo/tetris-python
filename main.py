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





from getpass import getpass
from random import randint

import recursos
import time
import threading
import enum

from pruebas import ordenes


# variables externas (inmutables)
pix_bn = "🔲"
pix_ng = "🔳"

dimensiones_pantalla = [20, 10]
largo = dimensiones_pantalla[0]
ancho = dimensiones_pantalla[1]

screen = [pix_bn for _ in range(1, 201)]


# Fija las figuras a la pantalla
def pantalla_pix(coordenadas:list, screen:tuple)->tuple:
    
    screen = list(screen)

    imagen = ""

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
    print(imagen)



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
                figura['posicion'] = 0
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


def limites_figura_horizontal(coordenadas:list, movimiento:int)->bool:
    
    limite_h_de = [x for x in range(1, ancho*largo+1) if x%10 == 0]  # ¿filter?
    limite_h_iz = [x+1 for x in limite_h_de if x<200]             # ¿map?
    #print(coordenadas, movimiento)
    #print(limite_h_iz)
    #print(limite_h_de)

    for coordenada in coordenadas:
        if coordenada in limite_h_de and movimiento == 1:
            return True
        elif coordenada in limite_h_iz and movimiento == -1:
            return True

    return False
        
    
# Funcion para comprobar las colisiones
def colision(coordenadas:list, screen:tuple):

    print(coordenadas)
    print(screen)
    for caracter in coordenadas:
        if screen.index(caracter) == pix_ng:
            True


def limites_vertical(coordenadas:list):

    limite_v = [x for x in range(191,201)]
    print(coordenadas)
    print(limite_v)

    # Comprovacion limites verticales
    for coordenada in coordenadas:
        if coordenada in limite_v:
            return True
        
    return False


# Calcula las coordenadas despues de cada movimiento 
def calculo_movimiento(coordenadas:list, movimiento:int):
    "Incluye el movimiento ordenado y el automatico"

    # Comprobacion de los limites horizontales
    if limites_figura_horizontal(coordenadas, movimiento):
        return coordenadas

    # Indices para calculo del movimiento vertical y horizontal.
    n = movimiento # o -1. Es la direccion del movimiento
    match movimiento:
        case 1:
            # movimiento horizontal derecha
            coordenadas_nuevas = [x + n for x in coordenadas]
        case -1:
            # movimiento horizontal izquierda
            coordenadas_nuevas = [x + n for x in coordenadas]
        case 0:
            # movimiento vertical
            coordenadas_nuevas = [x + ancho for x in coordenadas]
        case 5:
            print("\nADIOS")
            exit()

    # Control de colision
    #if colision(coordenadas_nuevas,screen):
        #return coordenadas, True

    # Retorna las coordenadas de la figura una vez aplicado el movimiento
    return coordenadas_nuevas


def logica():
    "coordina todo, enviando los parametros al resto de funciones"
    pass


if __name__ == "__main__":

# Variables importantes:
    # coordenadas
    # figura

# Secuencia
    comienzo = True
    while True:
        if comienzo:
            print("Yes")
            figura = salida(recursos.figuras)
            comienzo = False
            fijacion = False
            coordenadas = figura_prueba(figura)
            print(coordenadas)
        pantalla_prueba(coordenadas,screen)
        print(coordenadas)
        ord = ordenes()
        print(coordenadas)
        coordenadas = calculo_movimiento(coordenadas, ord)
        if limites_vertical(coordenadas):
            screen = pantalla_pix(coordenadas, screen)
            comienzo = True
        print(coordenadas)
        pantalla_prueba(coordenadas, screen)
        print(coordenadas)





# Coordenadas en rotacion de las figuras

# (5, 15, 25, 26)
# (4, 5, 6, 14)
# (5, 6, 16, 26)
# (6, 14, 15, 16)

# (5, 15, 25, 35)
# (4, 5, 6, 7)
# -1, -10, -19, -28

print(2//10)