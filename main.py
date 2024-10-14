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



"""
Resolucion:
    Vamos a hacerlo con funciones
    1. Necesitamos los dos tipo de pixeles. Para conseguirlos los hemos copìado de imagen que viene en el link de arriba.
    2. Los pixeles son strings, son signos, no son imagenes. Y la matriz es una lista de listas
    3. La pantalla sera representada como una matriz bidimensional.
    4. Tiene que "turnos", cada turno repesenta un lapso de tiempo, en el cual la pieza avanza.
    5. Tiene que haber una zona de salida, a ser posible en la zona central de la pantalla.
    6. Cada moviemiento de pieza tiene un dibujo diferente.
    7. En el caso de hacer un desarrollo completo, con caida y teclado, habria que ejecutar un hilo adiccional que controlara el teclado. 
    O un hilo adicional que controlara la caída de la pieza. Uno de los dos seria la secuencia principal de codigo y el otro un hilo 
    complementario que se ejecutara en paralelo.
    8. Tratamiento integral: git + github + apifast, todo para recordar y ensayar.

    
NOTA:
    EL SISTEMA DE COORDENADAS NO FUNCIONA BIEN. HAY UN ERROR DE BASE, QUE LO TRASTOCA TODO. SOLO FUNCIONA CON EL CUADRADO A BASE DE PRUEBA 
    ERROR PERO NO HAY UN DISEÑO COHERENTE DEL FUNCIONAMIENTO DE COORDENADAS. 

    LO DEJO AQUI PORQUE REHACERLO IMPLICA CASI EMPEZAR DE NUEVO Y ME LLEVARIA HORAS

    ES LA CONSECUENCIA DE NO PLANIFICAR LO QUE VOY A HACER Y DE LA FALTA DE EXPERIENCIA EN GENERAL. PESE A TODO EL SISTEMA ES MUY CURIOSO E 
    INGENIOSO, PARTICULARMENTE TENIENDO EN CUENTA QUE LO HICE A BOTE PRONTO.

"""

from getpass import getpass
from random import randint


# INTENTO PROPIO

# Instrcciones por pantalla
# print()

screen = (("🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"),
    ("🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"),
    ("🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"),
    ("🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"),
    ("🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"),
    ("🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"),
    ("🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"),
    ("🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"),
    ("🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"),
    ("🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"))

screen_l = ("🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲",
            "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲")



#=============================================================================================#

# SECUENCIA
    
#   1. Comprobacion de lanzamiento nueva figura si procede. ¿Marcador? ---> Dibujado
#   2. Ordenes
#   3. Calculos de las ordenes + movimiento automatico
#   4. Dibujado. Tal y como lo hacia antes. Primero lo llevamos a la lista y despues al string.
#   5. Consecuencias si procede: nueva figura. ¿Lineas?

# Perdurancia del lienzo. Tupla y lista

# Las figuras. Cada posicion una clave/valor. Otro para la posicion en uso siendo el valor la clave de la posicion. Las coordenadas en 
#   indices de la tupla de la pantalla.
#   . En realidad no necesito la representacion grafica que por otro lado es solo eso, una representacion visual para mi, en el fondo, 
#   con las coordenadas de cada elemento no necesito nada mas para dibujarlo
#   . La represnetacion en indices de las figuras seguira la secuencia logica de su traslacion a una lista. Ciertas figuras requeriran mas 
#   agudeza
#   . Los giros seran especialmente complicados, ya que primero giraran sobre su eje, y despues se le aplcara el movimiento automatico



# RESUMEN: Vamos calculando las coordenadas de la figura, pasandolas por parametro para sufrir las oportunas modificaciones hasta su 
# representacion final, que termina con el turno


import recursos

def pantalla_prueba(figura:list):
    'Dibuja la figura en la pantalla'

    pix_bn = "🔲"
    pix_ng = "🔳"
    # Creamos la pantalla en blanco-scream y asi nos evitamos pasarla por parametro. Usamos el guion bajo.
    screen = []
    for i in range(1, 101):
        if i//10 == int:
            screen.append("🔲\n")
        else:
            screen.append("🔲")

    # Adaptaciones de los parametros
    #screen = list(screen)
    imagen = ""

    # Creando la imagen en la pantalla (lista)
    for elemento in figura:
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




def figuras_prueba(figuras:dict, reinicio=False, coordenadas=[]):
    "gestiona la selecion de figuras y sus coordenadas al principio del turno, incluyendo la gestion de los giros"

    # Seleccion de figura - Nueva figura
    if reinicio:
        print("reniciuo")
        figuras = figuras
        lista = list(figuras.keys())
        indice = randint(0, (len(lista))-1)
        figura = figuras[lista[indice]]
        figura["posicion"] = 1
        return list(figura["1ini"])

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
    figura = figuras['recta']
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



def movimiento(coordenadas):
    "Incluye el movimiento ordenado y el automatico"

    dimensiones_pantalla = [10, 10]
    largo = dimensiones_pantalla[0]
    ancho = dimensiones_pantalla[1]

    # Indices para calculo del movimiento vertical y horizontal.
    n = 1 # o -1. Es la direccion del movimiento
    movimiento_verticax1 = [x + largo*n for x in coordenadas]
    movimiento_horizonxl = [x + n for x in coordenadas]
    movimiento_final = []

    # Retorna las coordenadas de la figura una vez aplicado el movimiento
    return movimiento_final


def logica():
    "coordina todo, enviando los parametros al resto de funciones"
    pass


if __name__ == "__main__":
    reinicio = True
    if reinicio:
        coordenadas = figuras_prueba(recursos.figuras, reinicio=reinicio)

    else:    
        figura = figuras_prueba(recursos.figuras, coordenadas=[4, 5, 6, 7])
        pantalla_prueba(screen_l, figura)

    pantalla_prueba(coordenadas)

# (5, 15, 25, 26)
# (4, 5, 6, 14)
# (5, 6, 16, 26)
# (6, 14, 15, 16)

# (5, 15, 25, 35)
# (4, 5, 6, 7)
# -1, -10, -19, -28