# Hilo del movimiento automatico.



import recursos
import main

import threading
import time



# Movimiento automatico:
#   Por ciclos: tiempo (temporizador) por avance (en pixeles)


# el codigo del movimiento automatico. Los parametros no son necesarios, pero de momento los mantengo para facilitar el trasiego de datos.
def cod_mov_auto(coordenadas:list, ancho:int):
    
    coordenadas_nuevas = [x + ancho for x in coordenadas]

    return coordenadas_nuevas


# Funcion temporal para indicar el trabajo del hilo.
"""
def mov_auto():
    
    # ciclo de tiempo en seg
    t = 1

    # un solo tipo de ciclo de pueba
    comienzo = True
    lista_colision = []
    while True:
        if comienzo:
            figura = main.salida(recursos.figuras)
            comienzo = False
            coordenadas = main.figura_prueba(figura)
        main.pantalla_prueba(coordenadas, main.screen)
        #### Esto seria lo propio del hilo de movimiento ###
        time.sleep(t)
        coordenadas = cod_mov_auto(coordenadas, main.ancho)
        ###                 ###                          ###
        if main.limites_vertical(coordenadas) or main.colision(coordenadas, lista_colision):
            screen = main.pantalla_pix(coordenadas, main.screen)
            main.screen = screen
            lista_colision = main.indices_colision(coordenadas, screen, lista_colision)
            comienzo = True
"""

def mov_auto():

    t = 1
    count = 1

    global coordenadas
    
    while True:
        time.sleep(2)
        coordenadas = cod_mov_auto(coordenadas, main.ancho)
        
        # seguro
        count += 1
        if count > 5:
            break



# Funcion temporal para controlar la inciacion del hilo
def thread():
    hilo = threading.Thread(target=mov_auto)
    t = round(time.time())
    hilo.start()
    hilo.join()
    time.sleep(10)
    exit()
    #if round(time.time) >= t + 10





if __name__ == "__main__":
    pass
    #thread()
