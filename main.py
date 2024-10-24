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


# C:Pruebas/PROGRAMACION/Repositorios/Tetris





from getpass import getpass
from random import randint

import recursos, mov_teclado, pruebas
#import mov_auto

import time
import threading
from enum import Enum, IntEnum
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
limite_h_de = [x for x in range(1, ancho*largo+1) if x%10 == 0]
limite_h_iz = [x+1 for x in limite_h_de if x<200]
limite_h_de_esp = [9, 19, 29, 39, 49, 59, 69, 79, 89, 99, 109, 119, 129, 139, 149, 159, 169, 179, 189, 199]

evento_1 = threading.Event()


#=======================================#


# BLOQUE PARA LA REPRESENTACION


# Fija las figuras terminadas a la pantalla
def pantalla_pix(coordenadas:list, screen:tuple)->tuple:
    
    screen = list(screen)
    imagen = ""
    #print("Coordendas de patalla_pix: ", coordenadas)

    # Comprobacion limite superior
    if list(filter(lambda x: x<=0, coordenadas)):
        coordenadas = list(filter(lambda x: x>0, coordenadas))
        final = True
    else:
        final = False

    # Comprobacion de reinicio de la pantalla
    if reinicio:
        screen = [pix_bn for _ in range(1, 201)]

    # Trasfiriendo las coordenadas de la figura a la pantalla (lista)
    else:
        for elemento in coordenadas:
            screen.pop(elemento-1)
            screen.insert(elemento-1, pix_ng)
    #print(screen)

    # Codigo de representacion: ¿initil aqui?
    # count = 1
    # for caracter in screen:
    #     if count == 10:
    #         imagen = imagen + caracter + "\n"
    #         count = 0
    #     else:
    #         imagen = imagen + caracter
    #     count += 1

    return tuple(screen), final

    

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

    # Marcador
    # ancho_marcador = len(f"|  Resultado:  {acumulado}  |")
    # print("="*ancho_marcador)
    # print("|", " "*(ancho_marcador-4), "|")
    # print(f"|  Resultado:  {acumulado}  |")
    # print("|", " "*(ancho_marcador-4), "|")
    # print("="*ancho_marcador)
    # print(f"\t+{resultado}")

    # print(f"Lineas: {lineas}")
    # print(f"Nivel: {nivel}")


#=======================================#


# BLOQUE PARA LA GESTION DE LAS FIGURAS


# Funcion para la seleccion de nuevas piezas - reseteo
def salida(figuras:dict):

    lista = list(figuras.keys())
    indice = randint(0, (len(lista))-1)
    figura = figuras[lista[indice]]
    figura["posicion"] = 0
    coordenadas = figura["1ini"]

    return figura, coordenadas
    #return figuras["recta"], figuras["recta"]["1ini"]

# Funcion de dibujado en patalla
def figura_giros(figura:dict, coordenadas):
    "gestiona la gestion de los giros"

 
    # Giro
    # Giran un coeficiente que se suma a los elmentos. Gira sobre un eje que es un elmeneto que no cambia su coordenada. Y giran en una 
    # direccion, que esta definida en + ó - segun el punto en el eje de ordenadas (mitad de las posiciones +, mitad negativo).
    figura = figura
    #print("Coordenadas al inicio de los calculos-giros en la funcion figura_prueba: ", coordenadas, ". La posicion de la figura: ", figura["posicion"])
    if figura["nombre"]=="recta":
        nuevas_coordenadas = []
        if figura['posicion']==1:
            # Control para los giros a un pix del margen derecho
            #print("Coordenadas figura_prueba/recta posicion 1 a posicion 0 al entrar: ", coordenadas, " ... /posicion:", figura["posicion"])
            if len(list(filter(lambda x: x in limite_h_de_esp, coordenadas))) > 1 or len(list(filter(lambda x: x in limite_h_de, coordenadas))) > 1:
                #print("ENTRO!!!!")
                for indice, x in enumerate(coordenadas):
                    if indice == 0:
                        nuevas_coordenadas.append(x+2)
                    elif indice ==1:
                        x = x - (10*indice+1)
                        nuevas_coordenadas.append(x+2)
                    elif indice ==2:
                        x = (x+1) - (10*indice+1)
                        nuevas_coordenadas.append(x+2)
                    elif indice ==3:
                        x = (x+2) - (10*indice+1)
                        nuevas_coordenadas.append(x+2)    
            else:
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
            #print("Coordenadas figura_prueba/recta posicion 1 a posicion 0: ", nuevas_coordenadas, " ... /posicion:", figura["posicion"])
            return nuevas_coordenadas
            
        elif figura['posicion']==0:
            #print("Coordenadas figura_prueba/recta posicion 0 a posicion 1 al entrar: ", coordenadas, " ... /posicion:", figura["posicion"])
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
            #print("Coordenadas figura_prueba/recta posicion 0 a posicion 1: ", nuevas_coordenadas, " ... /posicion:", figura["posicion"])
            return nuevas_coordenadas
    
    elif figura["nombre"]=="L":
        nuevas_coordenadas = []
        if figura['posicion']==0:
            #print("Coordenadas figura_prueba/L posicion 0 a posicion 1: ", nuevas_coordenadas, " ... /posicion:", figura["posicion"])
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
            #print("Coordenadas figura_prueba/L posicion 1 a posicion 2: ", nuevas_coordenadas, " ... /posicion:", figura["posicion"])
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
            #print("Coordenadas figura_prueba/L posicion 2 a posicion 3: ", nuevas_coordenadas, " ... /posicion:", figura["posicion"])
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
            #print("Coordenadas figura_prueba/L posicion 3 a posicion 0: ", nuevas_coordenadas, " ... /posicion:", figura["posicion"])
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
        
    elif figura["nombre"]=="L_inv":
        nuevas_coordenadas = []
        if figura['posicion']==0:
            #print("Coordenadas figura_prueba/L_inv posicion 0 a posicion 1: ", nuevas_coordenadas, " ... /posicion:", figura["posicion"])
            for indice, x in enumerate(coordenadas):
                if indice==0:
                    x = x-1
                    nuevas_coordenadas.append(x)
                elif indice==1:
                    x = x-1
                    nuevas_coordenadas.append(x)
                elif indice==2:
                    x = x-10
                    nuevas_coordenadas.append(x)
                elif indice==3:
                    x = x-8
                    nuevas_coordenadas.append(x)
            figura['posicion'] = 1
            return nuevas_coordenadas
    
        elif figura["posicion"]==1:
            #print("Coordenadas figura_prueba/L_inv posicion 1 a posicion 2: ", nuevas_coordenadas, " ... /posicion:", figura["posicion"])
            for indice, x in enumerate(coordenadas):
                if indice==0:
                    x = x+1
                    nuevas_coordenadas.append(x)
                elif indice==1:
                    x = x-8
                    nuevas_coordenadas.append(x)
                elif indice==2:
                    x = x
                    nuevas_coordenadas.append(x)
                elif indice==3:
                    x = x+9
                    nuevas_coordenadas.append(x)
            figura['posicion'] = 2
            return nuevas_coordenadas
    
        elif figura["posicion"]==2:
            #print("Coordenadas figura_prueba/L_inv posicion 2 a posicion 3: ", nuevas_coordenadas, " ... /posicion:", figura["posicion"])
            for indice, x in enumerate(coordenadas):
                if indice==0:
                    x = x-1
                    nuevas_coordenadas.append(x)
                elif indice==1:
                    x = x-1
                    nuevas_coordenadas.append(x)
                elif indice==2:
                    x = x-9
                    nuevas_coordenadas.append(x)
                elif indice==3:
                    x = x-9
                    nuevas_coordenadas.append(x)
            figura['posicion'] = 3
            return nuevas_coordenadas

        elif figura["posicion"]==3:
            #print("Coordenadas figura_prueba/L_inv posicion 4 a posicion 0: ", nuevas_coordenadas, " ... /posicion:", figura["posicion"])
            for indice, x in enumerate(coordenadas):
                if indice==0:
                    x = x+1
                    nuevas_coordenadas.append(x)
                elif indice==1:
                    x = x+10
                    nuevas_coordenadas.append(x)
                elif indice==2:
                    x = x+19
                    nuevas_coordenadas.append(x)
                elif indice==3:
                    x = x+8
                    nuevas_coordenadas.append(x)
            figura['posicion'] = 0
            return nuevas_coordenadas
        
    elif figura["nombre"]=="cuadrado":
        return coordenadas
    
    elif figura["nombre"]=="cuatro":
        nuevas_coordenadas = []
        if figura['posicion']==0:
            #print("Coordenadas figura_prueba/cuatro posicion 0 a posicion 1: ", nuevas_coordenadas, " ... /posicion:", figura["posicion"])
            for indice, x in enumerate(coordenadas):
                if indice==0:
                    x = x
                    nuevas_coordenadas.append(x)
                elif indice==1:
                    x = x+9
                    nuevas_coordenadas.append(x)
                elif indice==2:
                    x = x+2
                    nuevas_coordenadas.append(x)
                elif indice==3:
                    x = x+11
                    nuevas_coordenadas.append(x)
            figura['posicion'] = 1
            return nuevas_coordenadas
        
        elif figura['posicion']==1:
            #print("Coordenadas figura_prueba/cuatro posicion 1 a posicion 0: ", nuevas_coordenadas, " ... /posicion:", figura["posicion"])
            for indice, x in enumerate(coordenadas):
                if indice==0:
                    x = x
                    nuevas_coordenadas.append(x)
                elif indice==1:
                    x = x-9
                    nuevas_coordenadas.append(x)
                elif indice==2:
                    x = x-2
                    nuevas_coordenadas.append(x)
                elif indice==3:
                    x = x-11
                    nuevas_coordenadas.append(x)
            figura['posicion'] = 0
            return nuevas_coordenadas
        
    elif figura["nombre"]=="cuatro_inv":
        nuevas_coordenadas = []
        if figura['posicion']==0:
            #print(f"Coordenadas figura_prueba/{figura['nombre']} posicion 0 a posicion 1: ", coordenadas, " ... /posicion:", figura["posicion"])
            for indice, x in enumerate(coordenadas):
                if indice==0:
                    x = x+1
                    nuevas_coordenadas.append(x)
                elif indice==1:
                    x = x+9
                    nuevas_coordenadas.append(x)
                elif indice==2:
                    x = x+0
                    nuevas_coordenadas.append(x)
                elif indice==3:
                    x = x+8
                    nuevas_coordenadas.append(x)
            figura['posicion'] = 1
            #print("Coordenadas figura_prueba/cuatro_inv posicion 0 a posicion 1: ", nuevas_coordenadas, " ... /posicion:", figura["posicion"])
            return nuevas_coordenadas
    
        elif figura["posicion"]==1:
            #print(f"Coordenadas figura_prueba/{figura['nombre']} posicion 1 a posicion 0: ", coordenadas, " ... /posicion:", figura["posicion"])
            for indice, x in enumerate(coordenadas):
                if indice==0:
                    x = x-1
                    nuevas_coordenadas.append(x)
                elif indice==1:
                    x = x-9
                    nuevas_coordenadas.append(x)
                elif indice==2:
                    x = x
                    nuevas_coordenadas.append(x)
                elif indice==3:
                    x = x-8
                    nuevas_coordenadas.append(x)
            figura['posicion'] = 0
            #print("Coordenadas figura_prueba/cuatro_inv posicion 0 a posicion 1: ", nuevas_coordenadas, " ... /posicion:", figura["posicion"])
            return nuevas_coordenadas
        
    elif figura["nombre"]=="__|__":
        nuevas_coordenadas = []
        if figura['posicion']==0:
            #print("Coordenadas figura_prueba/__|__ posicion 0 a posicion 1: ", nuevas_coordenadas, " ... /posicion:", figura["posicion"])
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
            figura['posicion'] = 1
            return nuevas_coordenadas
    
        elif figura["posicion"]==1:
            #print("Coordenadas figura_prueba/__|__ posicion 1 a posicion 2: ", nuevas_coordenadas, " ... /posicion:", figura["posicion"])
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
            figura['posicion'] = 2
            return nuevas_coordenadas
        
        elif figura["posicion"]==2:
            #print("Coordenadas figura_prueba/__|__ posicion 1 a posicion 2: ", nuevas_coordenadas, " ... /posicion:", figura["posicion"])
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
            figura['posicion'] = 3
            return nuevas_coordenadas
        
        elif figura["posicion"]==3:
            #print("Coordenadas figura_prueba/__|__ posicion 1 a posicion 2: ", nuevas_coordenadas, " ... /posicion:", figura["posicion"])
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
            figura['posicion'] = 0
            return nuevas_coordenadas
            

#=======================================#


# BLOQUE DE COLISION Y LIMITES


def limites_figura_horizontal(coordenadas:list, movimiento:int, giro:bool):
    
    limite_h_de = [x for x in range(1, ancho*largo+1) if x%10 == 0]  # ¿filter?
    limite_h_iz = [x+1 for x in limite_h_de if x<200]             # ¿map?
    limite_h_de_esp = [9, 19, 29, 39, 49, 59, 69, 79, 89, 99, 109, 119, 129, 139, 149, 159, 169, 179, 189, 199]
    lado = None
    limite = None

    
    #print(f"Limite_figura_horizontal: {coordenadas}, {movimiento}, {giro},", figura['posicion'])
    #print("Limite horizontal izquierdo: ", limite_h_iz)
    #print("Limite horizontal derecho: ", limite_h_de)

    # Comprobacion de los limites en los movimientos. El lado izquierdo es definido como Falso
    if giro is False:
        for coordenada in coordenadas:
            if coordenada in limite_h_de and movimiento == 1:
                limite, lado = True, True
                return limite, lado
            elif coordenada in limite_h_iz and movimiento == -1:
                limite, lado = True, False
                return limite, lado
        limite = False
        lado = None
        return limite, lado
    
    # Comprobacion en los giros pegados al limite horizontal:
    # Especial para las rectas
    elif giro is True and figura["nombre"]=="recta":
        for coordenada in coordenadas:
            if coordenada in limite_h_iz and movimiento == 5:
                #print("Confirmado giro pegado al limite izquierdo")
                limite, lado = True, False
                return limite, lado
            elif coordenada in limite_h_de and movimiento ==5:
                limite, lado = True, True
                return limite, lado
            elif coordenada in limite_h_de_esp and movimiento ==5:
                limite, lado = True, True
                return limite, lado
        limite = False
        lado = None
        return limite, lado
    
    elif giro:
        for coordenada in coordenadas:
            if coordenada in limite_h_iz and movimiento == 5:
                #print("Confirmado giro pegado al limite izquierdo")
                limite, lado = True, False
                return limite, lado
            elif coordenada in limite_h_de and movimiento ==5:
                limite, lado = True, True
                return limite, lado
        limite = False
        lado = None
        return limite, lado
        
    
# Funcion para obtener las coordenadas de las piezas colocadas.
def indices_colision(coordenadas:list, indices:list) -> list:

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
    #print("lista de colision", lista_colision)

    return lista_colision
        

# Comprueba si las coordenadas de la figura estan pegadas (a 10 indices/pixeles) de las figuras estacionadas
def colision(coordenadas:list, lista_colision:list)->bool:

    rango_colision = list(map(lambda x: x-10, lista_colision))
    
    #print("Rango de colision", rango_colision)
    #print("Coordenadas", coordenadas)
    #print("BOLEANO", any(coordenadas == list(rango_colision)))
    #print(list(filter(lambda x: x in rango_colision, coordenadas)))

    if list(filter(lambda x: x in rango_colision, coordenadas)):
        #print("COLISION Is True")
        return True
    
    else:
        return False
    

# Funcion para evitar que la figura en juego se monte sobre las piezas ya colocadas. Compara las coordenadas de la piezs en juego con las 
# estacionadas (lista de colision)
def control_invasion(coordenadas:list, indices:list) -> list:
    #print("Coordenadas invasion: ", coordenadas)
    #print("lista de colision: ", indices)
    invasion = list(filter(lambda x: True if x in indices else False, coordenadas))

    while any(invasion):
        coordenadas = list(map(lambda x: x - 10, coordenadas))
        invasion = list(filter(lambda x: True if x in indices else False, coordenadas))
        if any(invasion):
            continue
        else:
            #print("Coordenadas invasion purgada: ", coordenadas)
            return coordenadas
    #print("Coordenadas salidas invasion sin ¿necesidad? de purgar", coordenadas)    
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



# Funcion correctora en los giros pegados al limites horizontal izquierdo.
# Hay una malfuncion en algunos giros. Habra que cribar por giros.
# Hemos añadido un marcador del lado, porque empezo a dar problemas en derecho tambien Pero ha dejado de darlos. Si reaparecen desarrollo 
# la correcion en el lado derecho
def funcion_correctora(figura:dict, coordenadas_temporales:list, lado:bool)->list:

    # Datos
    #print()
    #print(figura)
    #print("Nombre:", figura["nombre"], " / ", "Posicion:", figura["posicion"], " / ", "lado:", lado, " / ", "coordenadas de entrada:", coordenadas_temporales )

    if figura["nombre"] == "L":
    # Margen izquierdo
        if lado is False:
            if figura['posicion'] == 1  or figura['posicion'] == 3:
                coordenadas_nuevas = map(lambda x: x+1, coordenadas_temporales)
                coordenadas_nuevas = list(coordenadas_nuevas)
                #print("coordenadas nuevas retornadas: ", coordenadas_nuevas)
                return coordenadas_nuevas
            
    elif figura["nombre"] == "L_inv":
    # Margen derecho
        if lado:
            #print("Lado derecho")
            if figura['posicion'] == 1:
                coordenadas_nuevas = map(lambda x: x-1, coordenadas_temporales)
                coordenadas_nuevas = list(coordenadas_nuevas)
                #print("coordenadas nuevas retornadas: ", coordenadas_nuevas)
                return coordenadas_nuevas
    # Margen izquierdo
        elif lado is False:
            #print("Lado izquierdo")
            if figura["posicion"] == 3:
                coordenadas_nuevas = list(map(lambda x: x+1, coordenadas_temporales))
                #print("coordenadas nuevas retornadas: ", coordenadas_nuevas)
                return coordenadas_nuevas
            
    elif figura["nombre"] == "recta":
        #print("Figura recta")
    # Margen izquierdo
        if lado is False:
            #print("Lado izquierdo")
            if figura['posicion'] == 1:
                #print("Figura posicion 1")
                coordenadas_nuevas = map(lambda x: x+1, coordenadas_temporales)
                #print("coordenadas nuevas retornadas: ", coordenadas_nuevas)
                return list(coordenadas_nuevas)
    # Margen derecho
        elif lado and figura['posicion'] == 1:
            #print("Lado derecho")
            coordenadas_nuevas = list(map(lambda x: x-1, coordenadas_temporales))
            #print("Casi Pegada", coordenadas_nuevas)
            if filter(lambda x: x in limite_h_de, coordenadas_nuevas):
                coordenadas_nuevas = list(map(lambda x: x-1, coordenadas_nuevas))
                #print("Pegada", coordenadas_nuevas)
                return coordenadas_nuevas
            
    elif figura["nombre"] == "cuatro":
    # Margen izquierdo
        if lado is False:
            if figura['posicion'] == 0:
                coordenadas_nuevas = list(map(lambda x: x+1, coordenadas_temporales))
                #print("coordenadas nuevas retornadas: ", coordenadas_nuevas)
                return coordenadas_nuevas
            
    elif figura["nombre"] == "cuatro_inv":
    # Margen derecho
        if lado:
            if figura['posicion'] == 0:
                coordenadas_nuevas = list(map(lambda x: x-1, coordenadas_temporales))
                #print("coordenadas nuevas retornadas: ", coordenadas_nuevas)
                return coordenadas_nuevas
            
    elif figura["nombre"] == "__|__":
    # Margen derecho
        if lado:
            if figura['posicion'] == 0:
                coordenadas_nuevas = list(map(lambda x: x-1, coordenadas_temporales))
                #print("coordenadas nuevas retornadas: ", coordenadas_nuevas)
                return coordenadas_nuevas
        elif lado is False:
            if figura['posicion'] == 2:
                coordenadas_nuevas = list(map(lambda x: x+1, coordenadas_temporales))
                #print("coordenadas nuevas retornadas: ", coordenadas_nuevas)
                return coordenadas_nuevas
        
    #print("Ninguno de los supuestos")
    return coordenadas_temporales


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
        #print("CONTROL AUTO", coordenadas_nuevas)
        return list(coordenadas_nuevas)
    
    return coordenadas_nuevas


def mov_auto():

    # Control:
    while not cerrojo:
        evento_1.wait()

    # Los niveles. La variable t controla la velocidad de caida. Dentro del bucle
    def tiempo():
        match nivel:
            case 1:
                t = 2
                return t
            case 2:
                t = 1.8
                return t
            case 3:
                t = 1.6
                return t
            case 4:
                t = 1.4
                return t
            case 5:
                t = 1.2
                return t
            case 6:
                t = 1
                return t
            case 7:
                t = 0.8
                return t
            case 9:
                t = 0.6
                return t
            case 10:
                t = 0.4
                return t

    global coordenadas
    global control
    
    while True:
        t = tiempo()
        time.sleep(t)
        coordenadas = cod_mov_auto(coordenadas, ancho)
        #pantalla_prueba(coordenadas, screen)
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

    #print("Coordenadas en calculo de movimiento: ", coordenadas)

    # Variable de control para salir
    global control

    # Comprobacion de los limites horizontales
    limite, lado = limites_figura_horizontal(coordenadas, movimiento, giro=False)
    if limite:
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
            limite, lado = limites_figura_horizontal(coordenadas, movimiento, giro=True)
            if limite:
            # giro de la figura
                coordenadas_temporales = figura_giros(figura, coordenadas)
                print("Giro sin corregir:", coordenadas_temporales, f"figura posicion: {figura["posicion"]}")
                coordenadas_nuevas = funcion_correctora(figura, coordenadas_temporales, lado)

                #coordenadas_nuevas = list(map(lambda x: x+1, coordenadas_temporales))
                #print(f"Giro corregido: {coordenadas_temporales}   ....   Giro corregido: {coordenadas_nuevas}")
            else:
                coordenadas_nuevas = figura_giros(figura, coordenadas)
                #print("Giro limpio:", coordenadas_nuevas)
        case recursos.Movimiento.SALIDA:
            print("\nADIOS - SALIDA")
            control = True
            exit()

    # Hay que poner AQUI, un control a las coordenas en su limite vertical. Si se pulsa repetidamente "abajo", se pueden llegar a enviar 
    # coordenadas que superen el len de screen.
    a = filter(lambda x: x if x > 200 else None, coordenadas_nuevas)
    if list(a):
        coordenadas_nuevas = map(lambda x: x-10, coordenadas_nuevas)
        #print("CONTROL VOLUNTARIO")
        return list(coordenadas_nuevas)

    # Retorna las coordenadas de la figura una vez aplicado el movimiento
    return coordenadas_nuevas


# Funcion gestion llamada del teclado
def teclado():
    #print("TECLADO")
    # Control:
    while not cerrojo:
        evento_1.wait()
    #print("TECLADO 2")
    global coordenadas

    while True:
        evento = keyboard.read_event()
        if evento.event_type == keyboard.KEY_DOWN:
            #print(evento.name)
            if evento.name.lower() == "a":
                coordenadas = calculo_movimiento_hilo(coordenadas, recursos.Movimiento.IZQUIERDA) 
            elif evento.name.lower() == "d":
                coordenadas = calculo_movimiento_hilo(coordenadas, recursos.Movimiento.DERECHA)
            elif evento.name.lower() == "s":
                coordenadas = calculo_movimiento_hilo(coordenadas, recursos.Movimiento.ABAJO)
            elif evento.name.lower() == "p":
                coordenadas = calculo_movimiento_hilo(coordenadas, recursos.Movimiento.GIRO)
            elif evento.name == "esc":
                coordenadas = calculo_movimiento_hilo(coordenadas, recursos.Movimiento.SALIDA)

        # Visualizacion.
        #pantalla_prueba(coordenadas, screen)


#=======================================#


# FILAS COMPLETADAS Y MARCADOR

def filas_mejorada(screen:tuple):

    # Creamos una matriz con los indices de la screen.
    matriz = []
    fila = []

    for row in range(0, 20):
        for elem in range(1, 11):
            n = row * 10
            fila.append(elem + n)
        if len(fila) == 10:
            matriz.append(fila)
            fila = []

    matriz.reverse()

    # Comprobamos fila por fila, comenzando por la ultima, si estan completas
    row = []
    print(len(screen))
    for ind, fila in enumerate(matriz):
        for elem in fila:
            if screen[elem-1] == pix_ng:
                row.append(True)
            else:
                row.append(False)
        if all(row):
            return True, ind
        else:
            row = []

    return False, None


# Elimina y contabiliza las filas completas
def come_filas_mejorado(screen:tuple, indice:int, lista_colision:int)->tuple:
    
    screen = list(screen)

    # Creamos una matriz a partir de screen
    screen_x_filas = []
    fila = []

    for elem in screen:
        fila.append(elem)
        if len(fila) == 10:
            screen_x_filas.append(fila)
            fila = []

    screen_x_filas.reverse()

    # Borramos la fila respectiva en la matriz gemela de screen. Y añadimos una fila en blanco por arriba
    screen_x_filas.pop(indice)
    screen_x_filas.reverse()
    screen_x_filas.insert(0, recursos.seccion_bn)

    # Volvemos a convertir la matriz en una tupla
    screen = []
    for fila in screen_x_filas:
        for elem in fila:
            screen.append(elem)

    # Actualizamos la lista de colision
    indices_colision = recursos.matriz[indice]
    #print("Indices de colision en come filas", indices_colision)
    #print("Lista de colision en come_filas antes de actualizar los indices restantes", lista_colision)
    for x in indices_colision:
        print(x)
        lista_colision.remove(x)
    #print("Lista de colision en come_filas despues de actualizar los indices restantes", lista_colision)
    #print("Numero a partir del cual deberia ser sumados: ", min(recursos.matriz[indice]))
    nueva_lista_colision = []
    for x in lista_colision:
        if x < min(recursos.matriz[indice]):
            x = x + 10
            nueva_lista_colision.append(x)
        else:
            nueva_lista_colision.append(x)
    #print("Lista de colision final en come_filas", nueva_lista_colision)

    #print(len(screen), screen)
    return tuple(screen), nueva_lista_colision



#=======================================#


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


#=======================================#


# NIVELES

# Funcion que controla los niveles: la velocidad de caida y el reinicio de la pantalla
def fases():

    #niveles = list(range(1, 11))
    niveles = list(range(1,11))

    # Rango de los niveles
    # for nivel in niveles:
    #     if lineas < nivel*10:
    #         reinicio = False
    #         return nivel, reinicio
    #     elif lineas == nivel*10:
    #         reinicio = True
    #         if nivel == 10:
    #             return nivel, reinicio
    #         return nivel + 1, reinicio
    #     elif lineas > 100:
    #         nivel = 10
    #         reinicio = False
    #         return nivel, reinicio

# Para pruebas, acortando los niveles:
    for nivel in niveles:
        if lineas < nivel*2:
            reinicio = False
            return nivel, reinicio
        elif lineas == nivel*2:
            reinicio = True
            if nivel == 10:
                return nivel, reinicio
            return nivel + 1, reinicio
        elif lineas > 20:
            nivel = 10
            reinicio = False
            return nivel, reinicio


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
    control = False
    cerrojo = True
    count = 0
    acumulado = 0
    resultado = 0
    lineas = 0
    nivel = 1
    reinicio = False


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
            figura, coordenadas = salida(recursos.figuras)
            comienzo = False
            #fijacion = False
            #coordenadas = figura_prueba(figura)
            #print(F"Coordenadas: {coordenadas}, figura: {figura["nombre"]}, posicion: {figura["posicion"]}")
            pantalla_prueba(coordenadas, screen)
            if reinicio:
                time.sleep(2)
                reinicio = False
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
            hilo_auto.start()
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
            cerrojo = False                                                     # Variable de control de los eventos para los hilos
            coordenadas = control_invasion(coordenadas, lista_colision)
            screen, final = pantalla_pix(coordenadas, screen)                          # Añadir una comprobacion al limite superior
            # Comprobacion final de partida.
            if final:
                pantalla_prueba(coordenadas, screen)
                print("\n"*2 + "\t"*9 + "GAME OVER")
                break
            pantalla_prueba(coordenadas, screen)
            lista_colision = indices_colision(coordenadas, lista_colision)
            #print("Lista de colision: ", lista_colision)
            comienzo = True
            # Aqui iria el condicional para controlar la filas resueltas
            while True:
                print("ELIMINACION")
                boleano, indice = filas_mejorada(screen)
                if not boleano:
                    break
                #lista_colision = indices_colision(coordenadas, lista_colision)
                screen, lista_colision = come_filas_mejorado(screen, indice, lista_colision)
                #print("Lista de colision de come_filas: ", lista_colision)
                pantalla_prueba(coordenadas, screen)
                time.sleep(1.5)
                count += 1
            # Marcador // Niveles
            if count:
                print("MARCADOR")
                acumulado, resultado = marcador(count, acumulado)
                lineas = lineas + count
                # Comprobacion de niveles
                nivel, reinicio = fases()
                if reinicio:
                    print("REINICIO")
                    screen, final = pantalla_pix(coordenadas, screen)
                    lista_colision = []
                count = 0


        # Control
        if control:
            print("\n\n\n\t\t\t\t\t\t############# GRACIAS POR JUGAR ##############")
            break


        # seguro
        #print("VUELTA: ", count)
        #count += 1
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