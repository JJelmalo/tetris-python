# Recursos


from enum import Enum, IntEnum



# Pantalla
pix_bn = "🔲"
pix_ng = "🔳"

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


# Figuras
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
    }



# Clase enum para controlar el movimiento
class Movimiento(IntEnum):
    
    IZQUIERDA = -1
    DERECHA = 1
    ABAJO = 0
    GIRO = 5
    SALIDA = 6


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
