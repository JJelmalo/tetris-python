# Hilo del movimiento por teclado



import keyboard

import main
import recursos



# I FASE:
# Sustitucion de las ordenes por consola por ordenes teclado
def teclado():

    evento = keyboard.read_event()

    if evento.event_type == keyboard.KEY_DOWN:
        if evento.name == "a":
            return recursos.Movimiento.IZQUIERDA
        elif evento.name == "d":
            return recursos.Movimiento.DERECHA
        elif evento.name == "s":
            return recursos.Movimiento.ABAJO
        elif evento.name == "p":
            return recursos.Movimiento.GIRO
        else:
            print("Adios.")
            exit()


# II FASE:
# Creacion de hilo para e movimiento por teclado y su integracion en el flujo principal.

