from node import Nodo
import numpy as np
import random
# #__________________________________________definicion de variables globales
nodo_raiz= Nodo(puntuacionB=0,puntuacionN=0, caballoB=[], caballoN=[], puntos=[], tipo="MAX")
ganador=None
global movimientoBlanco, movimientoNegro,hijoMax
movimientoBlanco = None
hijoMax = None
movimientoNegro = []
#dificultad = "amateur" # principiante, amateur, experto


# #funcion que encuentra la posicion inicial de todos los elementos del tablero
def find_initial_positions(board):
    puntos = []
    caballoB = None
    caballoN = None
    for i in range(len(board)):
        for h in range(len(board)):
            if mapa[i][h] == 9:
                caballoB = [i,h]
                mapa[i][h]=0
            elif mapa[i][h] == 8:
                caballoN = [i,h]
                mapa[i][h]=0
            elif int(mapa[i][h]) != 0:
                puntos.append([i,h])

    #Una vez recorrido el mapa, modificamos los atributos del nodo_raiz
    nodo_raiz.caballoB=caballoB
    nodo_raiz.caballoN=caballoN
    nodo_raiz.puntos=puntos
    return puntos,caballoB,caballoN

def evitar_devolverce(nodo_aux,nodos_recorridos):
    if nodo_aux.nodo_validoB(nodos_recorridos):
        return nodo_aux

def verificar_puntuacionB(nodo, fila, columna):
    puntos = nodo.showPuntos().copy()
    puntuacionB = nodo.showPuntuacionB()
    if [fila,columna] in nodo.showPuntos():
        puntos.remove([fila,columna])
        puntuacionB = puntuacionB + int(mapa[fila,columna])
    return puntos, puntuacionB

def verificar_puntuacionN(nodo, fila, columna):
    puntos = nodo.showPuntos().copy()
    puntuacionN = nodo.showPuntuacionN()
    if [fila,columna] in nodo.showPuntos():
        puntos.remove([fila,columna])
        puntuacionN = puntuacionN + int(mapa[fila,columna])
    return puntos, puntuacionN

def puede_moverseB(nodo):
    nodos_posibles = []
    nodos_recorridos = nodo.recorrer_arbol_arriba()
    #-----------------------
    #arriba derecha superior
    fila_nueva = nodo.showCaballoB()[0] - 2
    columna_nueva = nodo.showCaballoB()[1] + 1

    if fila_nueva >= 0 and columna_nueva<mapa.shape[1]:
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="arriba derecha superior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="arriba derecha superior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)

    #-------------------------
    #arriba izquierda superior
    fila_nueva = nodo.showCaballoB()[0] - 2
    columna_nueva = nodo.showCaballoB()[1] - 1
    if fila_nueva >= 0 and columna_nueva>=0:
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="arriba izquierda superior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="arriba izquierda superior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)

    #-------------------------
    #arriba derecha inferior
    fila_nueva = nodo.showCaballoB()[0] - 1
    columna_nueva = nodo.showCaballoB()[1] + 2
    if fila_nueva >= 0 and columna_nueva<mapa.shape[1]:
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="arriba derecha inferior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="arriba derecha inferior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)

    #-------------------------
    #arriba izquierda inferior
    fila_nueva = nodo.showCaballoB()[0] - 1
    columna_nueva = nodo.showCaballoB()[1] - 2
    if fila_nueva >= 0 and columna_nueva>=0:
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="arriba izquierda inferior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="arriba izquierda inferior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)

    #-------------------------
    #abajo derecha superior
    fila_nueva = nodo.showCaballoB()[0] + 1
    columna_nueva = nodo.showCaballoB()[1] + 2
    if fila_nueva<mapa.shape[0] and columna_nueva<mapa.shape[1]:
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="abajo derecha superior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="abajo derecha superior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)

    #-------------------------
    #abajo izquierda superior
    fila_nueva = nodo.showCaballoB()[0] + 1
    columna_nueva = nodo.showCaballoB()[1] - 2
    if fila_nueva<mapa.shape[0] and columna_nueva>=0:
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="abajo izquierda superior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="abajo izquierda superior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)

    #-------------------------
    #abajo derecha inferior
    fila_nueva = nodo.showCaballoB()[0] + 2
    columna_nueva = nodo.showCaballoB()[1] + 1
    if fila_nueva<mapa.shape[0] and columna_nueva<mapa.shape[1]:
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="abajo derecha inferior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="abajo derecha inferior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)

    #-------------------------
    #abajo izquierda inferior
    fila_nueva = nodo.showCaballoB()[0] + 2
    columna_nueva = nodo.showCaballoB()[1] - 1
    if fila_nueva<mapa.shape[0] and columna_nueva>=0:
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="abajo izquierda inferior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="abajo izquierda inferior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)

    return nodos_posibles
            
def puede_moverseN(nodo):
    nodos_posibles = []
    #-----------------------
    #arriba derecha superior
    fila_nueva = nodo.showCaballoN()[0] - 2
    columna_nueva = nodo.showCaballoN()[1] + 1

    if fila_nueva >= 0 and columna_nueva<mapa.shape[1]:
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=nodo.puntos, padre=nodo, operador="arriba derecha superior",tipo="MAX")
            nodos_posibles.append(nodo_aux)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            puntos, puntuacionN = verificar_puntuacionN(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = nodo.puntuacionB, puntuacionN=puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=puntos, padre=nodo, operador="arriba derecha superior",tipo="MAX")
            nodos_posibles.append(nodo_aux)

    #-------------------------
    #arriba izquierda superior
    fila_nueva = nodo.showCaballoN()[0] - 2
    columna_nueva = nodo.showCaballoN()[1] - 1
    if fila_nueva >= 0 and columna_nueva>=0:
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=nodo.puntos, padre=nodo, operador="arriba izquierda superior",tipo="MAX")
            nodos_posibles.append(nodo_aux)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            puntos, puntuacionN = verificar_puntuacionN(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = nodo.puntuacionB, puntuacionN=puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=puntos, padre=nodo, operador="arriba izquierda superior",tipo="MAX")
            nodos_posibles.append(nodo_aux)

    #-------------------------
    #arriba derecha inferior
    fila_nueva = nodo.showCaballoN()[0] - 1
    columna_nueva = nodo.showCaballoN()[1] + 2
    if fila_nueva >= 0 and columna_nueva<mapa.shape[1]:
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=nodo.puntos, padre=nodo, operador="arriba derecha inferior",tipo="MAX")
            nodos_posibles.append(nodo_aux)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            puntos, puntuacionN = verificar_puntuacionN(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = nodo.puntuacionB, puntuacionN=puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=puntos, padre=nodo, operador="arriba derecha inferior",tipo="MAX")
            nodos_posibles.append(nodo_aux)

    #-------------------------
    #arriba izquierda inferior
    fila_nueva = nodo.showCaballoN()[0] - 1
    columna_nueva = nodo.showCaballoN()[1] - 2
    if fila_nueva >= 0 and columna_nueva>=0:
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=nodo.puntos, padre=nodo, operador="arriba izquierda inferior",tipo="MAX")
            nodos_posibles.append(nodo_aux)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            puntos, puntuacionN = verificar_puntuacionN(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = nodo.puntuacionB, puntuacionN=puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=puntos, padre=nodo, operador="arriba izquierda inferior",tipo="MAX")
            nodos_posibles.append(nodo_aux)

    #-------------------------
    #abajo derecha superior
    fila_nueva = nodo.showCaballoN()[0] + 1
    columna_nueva = nodo.showCaballoN()[1] + 2
    if fila_nueva<mapa.shape[0] and columna_nueva<mapa.shape[1]:
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=nodo.puntos, padre=nodo, operador="abajo derecha superior",tipo="MAX")
            nodos_posibles.append(nodo_aux)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            puntos, puntuacionN = verificar_puntuacionN(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = nodo.puntuacionB, puntuacionN=puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=puntos, padre=nodo, operador="abajo derecha superior",tipo="MAX")
            nodos_posibles.append(nodo_aux)

    #-------------------------
    #abajo izquierda superior
    fila_nueva = nodo.showCaballoN()[0] + 1
    columna_nueva = nodo.showCaballoN()[1] - 2
    if fila_nueva<mapa.shape[0] and columna_nueva>=0:
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=nodo.puntos, padre=nodo, operador="abajo izquierda superior",tipo="MAX")
            nodos_posibles.append(nodo_aux)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            puntos, puntuacionN = verificar_puntuacionN(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = nodo.puntuacionB, puntuacionN=puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=puntos, padre=nodo, operador="abajo izquierda superior",tipo="MAX")
            nodos_posibles.append(nodo_aux)

    #-------------------------
    #abajo derecha inferior
    fila_nueva = nodo.showCaballoN()[0] + 2
    columna_nueva = nodo.showCaballoN()[1] + 1
    if fila_nueva<mapa.shape[0] and columna_nueva<mapa.shape[1]:
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=nodo.puntos, padre=nodo, operador="abajo derecha inferior",tipo="MAX")
            nodos_posibles.append(nodo_aux)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            puntos, puntuacionN = verificar_puntuacionN(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = nodo.puntuacionB, puntuacionN=puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=puntos, padre=nodo, operador="abajo derecha inferior",tipo="MAX")
            nodos_posibles.append(nodo_aux)

    #-------------------------
    #abajo izquierda inferior
    fila_nueva = nodo.showCaballoN()[0] + 2
    columna_nueva = nodo.showCaballoN()[1] - 1
    if fila_nueva<mapa.shape[0] and columna_nueva>=0:
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=nodo.puntos, padre=nodo, operador="abajo izquierda inferior",tipo="MAX")
            nodos_posibles.append(nodo_aux)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            puntos, puntuacionN = verificar_puntuacionN(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = nodo.puntuacionB, puntuacionN=puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=puntos, padre=nodo, operador="abajo izquierda inferior",tipo="MAX")
            nodos_posibles.append(nodo_aux)
            
    return nodos_posibles

def verFuturo(dificultad, nodoRaiz):
    movimientoBlanco = None
    hijoMax = None
    movimientoNegro = []
    nodoRaiz.padre = None
    profundidad = 0

    if dificultad == "principiante":
        profundidad = 2
    elif dificultad == "amateur":
        profundidad = 4
    elif dificultad == "experto":
        profundidad = 6
    
    nodos=expandirNodos(profundidad,[nodoRaiz])
    nodos[0].recorrer_arbol_arriba()[-1].calcular_utilidad()
    arrayB=[]
    arrayN=[]
    utilidades=[]
    hijos=nodos[0].recorrer_arbol_arriba()[-1].showHijos()
    valorHijoMax=nodos[0].recorrer_arbol_arriba()[-1].showHijos()[0].showUtilidad()
    hijoMax=nodos[0].recorrer_arbol_arriba()[-1].showHijos()[0]
    for i in nodos[0].recorrer_arbol_arriba()[-1].showHijos():
        arrayB.append(i.showCaballoB())
        arrayN.append(i.showCaballoN())
        utilidades.append(i.showUtilidad())
    for i in range(len(hijos)):
        if hijos[i].showUtilidad()>valorHijoMax:
            valorHijoMax=hijos[i].showUtilidad()
            hijoMax=hijos[i]
    movimientoBlanco=hijoMax.showCaballoB()
    nodosNegro=puede_moverseN(hijoMax)
    for i in nodosNegro:
        movimientoNegro.append(i.showCaballoN())
    return movimientoNegro, hijoMax, nodosNegro

def expandirNodos(profundidad, nodos):
    if profundidad == 0:
        return nodos

    nuevosNodos = []
    for nodo in nodos:
        if profundidad % 2 == 0:
            movimientos = puede_moverseB(nodo)
        else:
            movimientos = puede_moverseN(nodo)
        if profundidad==1 or nodo.esMeta():
            nodo.utilidad = nodo.funcionUtilidad()
        for i in movimientos:
            nodo.agregar_hijo(i)
        nuevosNodos.extend(movimientos)
    return expandirNodos(profundidad - 1, nuevosNodos)

# esta funcion recibe un arreglo con los nodos de maxima profundidad por turno y nodos meta y retorna aquel que tenga una mayor funcion de utilidad
def nodo_maxima_utilidad(nodos):
    mayor = nodos[0].funcionUtilidad()
    index = 0
    for i in range(len(nodos)):
        if nodos[i].funcionUtilidad() > mayor:
            index = i
            mayor = nodos[i].funcionUtilidad()
    return nodos[index]

def randomize_board(size):
    global puntos
    puntos = []
    global caballoBlanco
    caballoBlanco = []
    global caballoNegro
    caballoNegro = []

    num_tuples = 9
    tuples = set() #conjunto para que no se repitan los valores
    # mientras no se tengan todas las posiciones se recalcula
    while len(puntos) + len(caballoBlanco) + len(caballoNegro) < num_tuples:
        new_tuple = tuple(random.randint(0, size-1) for _ in range(2))
        if new_tuple not in tuples:
            tuples.add(new_tuple)
            if len(puntos) != 7:
                puntos.append(new_tuple)
            elif len(caballoBlanco) != 1:
                caballoBlanco.append(new_tuple)
            elif len(caballoNegro) != 1:
                caballoNegro.append(new_tuple)

def asignar_coordenadas():
    aux = 1
    for punto in puntos:
        row = punto[0]
        cell = punto[1]
        mapa[row][cell] = aux
        aux = aux + 1
    mapa[caballoNegro[0][0]][caballoNegro[0][1]] = 8
    mapa[caballoBlanco[0][0]][caballoBlanco[0][1]] = 9

def verificarGanador(nodo):
    global ganador
    ganador = "Ninguno"
    if(nodo.esMeta()):
        if(nodo.showPuntuacionB()>nodo.showPuntuacionN()):
            ganador ="Blanco"
        elif(nodo.showPuntuacionB()<nodo.showPuntuacionN()):
            ganador="Negro"
        else:
            ganador="Empate"
    return ganador

mapa = np.zeros((8,8))
#mapa.astype(int)
randomize_board(8)
asignar_coordenadas()
find_initial_positions(mapa)
