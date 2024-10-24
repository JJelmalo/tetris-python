# Recursos


from enum import Enum, IntEnum



# PANTALLA
pix_bn = "🔲"
pix_ng = "🔳"
seccion_bn = [pix_bn for _ in list(range(10))]

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


# FIGURAS
figuras = {"recta" : {"nombre" : "recta",
           
                     "1" :       [["🔳"],
                                  ["🔳"],
                                  ["🔳"],
                                  ["🔳"]],

                     "2" : ["🔳", "🔳", "🔳", "🔳"],

                     "1ini" : (5, 15, 25, 35),

                     "2ini" : (4, 5, 6, 7),

                     "coef_giro" : 10,

                     "eje_giro" : 0,

                     "posicion" : 0,

                     "posiciones" : 2,

                     "coordenadas" : [int, int, int, int]
                    },

            "L" :   {"nombre" : "L",
            
					"1" :  [["🔳"],
                            ["🔳"],
                            ["🔳","🔳"]],

                    "2" :  [["🔳", "🔳", "🔳"],
                            ["🔳"]],

                    "3" :  [["🔳", "🔳"],
                                  ["🔳"],
                                  ["🔳"]],

                    "4" : [             ["🔳"],
                          ["🔳", "🔳", "🔳"]],

                    "1ini" : (5, 15, 25, 26),

                    "2ini" : (4, 5, 6, 14),

                    "3ini" : (5, 6, 16, 26),

                    "4ini" : (6, 14, 15, 16),
                    
                    "coef_giro" : 10,

                    "eje_giro" : 2,

                    "posicion" : 0,

                    "posiciones" : 4,

                    "coordenadas" : [int, int, int, int]
                    },

            "L_inv" :   {"nombre" : "L_inv",
            
					"1" :        [["🔳"],
                                  ["🔳"],
                            ["🔳","🔳"]],

                    "2" :  [["🔳"],
                           ["🔳", "🔳", "🔳"]],

                    "3" :  [["🔳", "🔳"],
                            ["🔳"],
                            ["🔳"]],

                    "4" : [["🔳", "🔳", "🔳"],
                                        ["🔳"]],

                    "1ini" : (6, 16, 26, 25),

                    "2ini" : (5, 15, 16, 17),

                    "3ini" : (6, 7, 16, 26),

                    "4ini" : (5, 6, 7, 17),
                    
                    "coef_giro" : 10,

                    "eje_giro" : 2,

                    "posicion" : 0,

                    "posiciones" : 4,

                    "coordenadas" : [int, int, int, int]
                    },

            "cuatro" :   {"nombre" : "cuatro",
            
					"1" :        [["🔳","🔳"],
                            ["🔳","🔳"]],

                    "2" :  [["🔳"], 
                            ["🔳", "🔳"],
                                   ["🔳"]],

                    "1ini" : (5, 6, 14, 15),

                    "2ini" : (5, 15, 16, 26),
                    
                    "coef_giro" : 10,

                    "eje_giro" : 2,

                    "posicion" : 0,

                    "posiciones" : 2,

                    "coordenadas" : [int, int, int, int]
                    },

            "cuatro_inv" :   {"nombre" : "cuatro_inv",
            
					"1" :   [["🔳","🔳"],
                                   ["🔳","🔳"]],

                    "2" :         [["🔳"], 
                            ["🔳", "🔳"],
                            ["🔳"]],

                    "1ini" : (5, 6, 16, 17),

                    "2ini" : (6, 15, 16, 25),
                    
                    "coef_giro" : 10,

                    "eje_giro" : 2,

                    "posicion" : 0,

                    "posiciones" : 2,

                    "coordenadas" : [int, int, int, int]
                    },

            "cuadrado" : {"nombre" : "cuadrado",
                    
                    "1" :       [["🔳","🔳"],
                                 ["🔳","🔳"]],

                    "1ini" : (5, 6, 15, 16),

                    "coef_giro" : 10,

                    "eje_giro" : 0,

                    "posicion" : 0,

                    "posiciones" : 1,

                    "coordenadas" : [int, int, int, int]
                    },
    }



# Clase enum para controlar el movimiento
class Movimiento(IntEnum):
    
    IZQUIERDA = -1
    DERECHA = 1
    ABAJO = 0
    GIRO = 5
    SALIDA = 6


# Clase enum para los niveles:
class Niveles(IntEnum):

    UNO = 1
    DOS = 2
    TRES = 3
    CUATRO = 4
    CINCO = 5
    SEIS = 6
    SIETE = 7
    OCHO = 8
    NUEVE = 9
    DIEZ = 10


# Clase enum para controlar las filas completas
# class Filas(IntEnum):

#     PRIMERA = 0
#     SEGUNDA = 1
#     TERCERA = 2
#     CUARTA = 3
#     QUINTA = 4
#     SEXTA = 5
#     SEPTIMA = 6
#     OCTAVA = 7
#     NOVENA = 8
#     DECIMA = 9
#     UNDECIMA = 10
#     DUODECIMA = 11
#     DECIMOTERCERA = 12
#     DECIMOCUARTA = 13
#     DECIMOQUINTA = 14
#     DECIMOSEXTA = 15
#     DECIMOSEPTIMA = 16
#     DECIMOOCTAVA = 17
#     DECIMONOVENA =18
#     VIGESIMA = 19

# funcion temporal para comprobar el movimiento en main.py.
def ordenes() -> Movimiento :
    print("""
\nPresione la letra 'a' para moverse a la izquierda.
Presione la letra 'd' para moverse a la derecha.
Presione la letra 's' para avanzar hacia abajo.
Presione la letra 'p' para girar la figura.
Presione cualquier otra tecka para salir del juego.
        """)
    
    x = input()

    if x == "a":
        return Movimiento.IZQUIERDA
    elif x == "d":
        return Movimiento.DERECHA
    elif x == "s":
        return Movimiento.ABAJO
    elif x == "p":
        return Movimiento.GIRO
    else:
        print("Adios.")
        exit()
