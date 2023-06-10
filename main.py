from node import Nodo
import numpy as np
import random

# #__________________________________________definicion de variables globales
nodo_raiz= Nodo(puntuacionB=0,puntuacionN=0, caballoB=[], caballoN=[], puntos=[], tipo="MAX")
arbol=[]
ganador=None
global dificultad
dificultad = "amateur"

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
    #Se añade el nodo_raiz a la cola
    #cola.append(nodo_raiz)
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
    #print([fila_nueva,columna_nueva])
    #print([nodo.showCaballoN()[0],nodo.showCaballoN()[1]])

    if fila_nueva >= 0 and columna_nueva<mapa.shape[1]:
        #print(mapa[fila_nueva][columna_nueva])
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            #print(nodo.showPuntos())
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="arriba derecha superior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="arriba derecha superior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)

    #-------------------------
    #arriba izquierda superior
    fila_nueva = nodo.showCaballoB()[0] - 2
    columna_nueva = nodo.showCaballoB()[1] - 1
    if fila_nueva >= 0 and columna_nueva>=0:
        #print(mapa[fila_nueva][columna_nueva])
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            #print(nodo.showPuntos())
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="arriba izquierda superior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="arriba izquierda superior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)

    #-------------------------
    #arriba derecha inferior
    fila_nueva = nodo.showCaballoB()[0] - 1
    columna_nueva = nodo.showCaballoB()[1] + 2
    if fila_nueva >= 0 and columna_nueva<mapa.shape[1]:
        #print(mapa[fila_nueva][columna_nueva])
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            #print(nodo.showPuntos())
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="arriba derecha inferior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="arriba derecha inferior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)

    #-------------------------
    #arriba izquierda inferior
    fila_nueva = nodo.showCaballoB()[0] - 1
    columna_nueva = nodo.showCaballoB()[1] - 2
    if fila_nueva >= 0 and columna_nueva>=0:
        #print(mapa[fila_nueva][columna_nueva])
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            #print(nodo.showPuntos())
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="arriba izquierda inferior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="arriba izquierda inferior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)

    #-------------------------
    #abajo derecha superior
    fila_nueva = nodo.showCaballoB()[0] + 1
    columna_nueva = nodo.showCaballoB()[1] + 2
    if fila_nueva<mapa.shape[0] and columna_nueva<mapa.shape[1]:
        #print(mapa[fila_nueva][columna_nueva])
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            #print(nodo.showPuntos())
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="abajo derecha superior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="abajo derecha superior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)

    #-------------------------
    #abajo izquierda superior
    fila_nueva = nodo.showCaballoB()[0] + 1
    columna_nueva = nodo.showCaballoB()[1] - 2
    if fila_nueva<mapa.shape[0] and columna_nueva>=0:
        #print(mapa[fila_nueva][columna_nueva])
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            #print(nodo.showPuntos())
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="abajo izquierda superior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="abajo izquierda superior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)

    #-------------------------
    #abajo derecha inferior
    fila_nueva = nodo.showCaballoB()[0] + 2
    columna_nueva = nodo.showCaballoB()[1] + 1
    if fila_nueva<mapa.shape[0] and columna_nueva<mapa.shape[1]:
        #print(mapa[fila_nueva][columna_nueva])
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            #print(nodo.showPuntos())
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="abajo derecha inferior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="abajo derecha inferior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)

    #-------------------------
    #abajo izquierda inferior
    fila_nueva = nodo.showCaballoB()[0] + 2
    columna_nueva = nodo.showCaballoB()[1] - 1
    if fila_nueva<mapa.shape[0] and columna_nueva>=0:
        #print(mapa[fila_nueva][columna_nueva])
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            #print(nodo.showPuntos())
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="abajo izquierda inferior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="abajo izquierda inferior",tipo="MIN")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)

    # print("FINAL BLANCO")
    # print("nodos",nodos_posibles)
    # print("Puntos",nodos_posibles[0].showPuntos())
    # print("CaballoBlanco",nodos_posibles[0].showCaballoB())
    # print("PuntuacionBlanco",nodos_posibles[0].showPuntuacionB())
    # coordenadas=[]
    # for i in nodos_posibles:
    #     coordenadas.append(i.showCaballoB())
    # print("casillas posibles",coordenadas)
    return nodos_posibles
            
def puede_moverseN(nodo):
    nodos_posibles = []
    #-----------------------
    #arriba derecha superior
    fila_nueva = nodo.showCaballoN()[0] - 2
    columna_nueva = nodo.showCaballoN()[1] + 1
    #print([fila_nueva,columna_nueva])
    #print([nodo.showCaballoN()[0],nodo.showCaballoN()[1]])

    if fila_nueva >= 0 and columna_nueva<mapa.shape[1]:
        #print(mapa[fila_nueva][columna_nueva])
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            #print(nodo.showPuntos())
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=nodo.puntos, padre=nodo, operador="arriba derecha superior",tipo="MAX")
            nodos_posibles.append(nodo_aux)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionN = verificar_puntuacionN(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = nodo.puntuacionB, puntuacionN=puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=puntos, padre=nodo, operador="arriba derecha superior",tipo="MAX")
            nodos_posibles.append(nodo_aux)

    #-------------------------
    #arriba izquierda superior
    fila_nueva = nodo.showCaballoN()[0] - 2
    columna_nueva = nodo.showCaballoN()[1] - 1
    if fila_nueva >= 0 and columna_nueva>=0:
        #print(mapa[fila_nueva][columna_nueva])
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            #print(nodo.showPuntos())
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=nodo.puntos, padre=nodo, operador="arriba izquierda superior",tipo="MAX")
            nodos_posibles.append(nodo_aux)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionN = verificar_puntuacionN(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = nodo.puntuacionB, puntuacionN=puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=puntos, padre=nodo, operador="arriba izquierda superior",tipo="MAX")
            nodos_posibles.append(nodo_aux)

    #-------------------------
    #arriba derecha inferior
    fila_nueva = nodo.showCaballoN()[0] - 1
    columna_nueva = nodo.showCaballoN()[1] + 2
    if fila_nueva >= 0 and columna_nueva<mapa.shape[1]:
        #print(mapa[fila_nueva][columna_nueva])
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            #print(nodo.showPuntos())
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=nodo.puntos, padre=nodo, operador="arriba derecha inferior",tipo="MAX")
            nodos_posibles.append(nodo_aux)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionN = verificar_puntuacionN(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = nodo.puntuacionB, puntuacionN=puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=puntos, padre=nodo, operador="arriba derecha inferior",tipo="MAX")
            nodos_posibles.append(nodo_aux)

    #-------------------------
    #arriba izquierda inferior
    fila_nueva = nodo.showCaballoN()[0] - 1
    columna_nueva = nodo.showCaballoN()[1] - 2
    if fila_nueva >= 0 and columna_nueva>=0:
        #print(mapa[fila_nueva][columna_nueva])
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            #print(nodo.showPuntos())
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=nodo.puntos, padre=nodo, operador="arriba izquierda inferior",tipo="MAX")
            nodos_posibles.append(nodo_aux)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionN = verificar_puntuacionN(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = nodo.puntuacionB, puntuacionN=puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=puntos, padre=nodo, operador="arriba izquierda inferior",tipo="MAX")
            nodos_posibles.append(nodo_aux)

    #-------------------------
    #abajo derecha superior
    fila_nueva = nodo.showCaballoN()[0] + 1
    columna_nueva = nodo.showCaballoN()[1] + 2
    if fila_nueva<mapa.shape[0] and columna_nueva<mapa.shape[1]:
        #print(mapa[fila_nueva][columna_nueva])
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            #print(nodo.showPuntos())
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=nodo.puntos, padre=nodo, operador="abajo derecha superior",tipo="MAX")
            nodos_posibles.append(nodo_aux)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionN = verificar_puntuacionN(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = nodo.puntuacionB, puntuacionN=puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=puntos, padre=nodo, operador="abajo derecha superior",tipo="MAX")
            nodos_posibles.append(nodo_aux)

    #-------------------------
    #abajo izquierda superior
    fila_nueva = nodo.showCaballoN()[0] + 1
    columna_nueva = nodo.showCaballoN()[1] - 2
    if fila_nueva<mapa.shape[0] and columna_nueva>=0:
        #print(mapa[fila_nueva][columna_nueva])
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            #print(nodo.showPuntos())
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=nodo.puntos, padre=nodo, operador="abajo izquierda superior",tipo="MAX")
            nodos_posibles.append(nodo_aux)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionN = verificar_puntuacionN(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = nodo.puntuacionB, puntuacionN=puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=puntos, padre=nodo, operador="abajo izquierda superior",tipo="MAX")
            nodos_posibles.append(nodo_aux)

    #-------------------------
    #abajo derecha inferior
    fila_nueva = nodo.showCaballoN()[0] + 2
    columna_nueva = nodo.showCaballoN()[1] + 1
    if fila_nueva<mapa.shape[0] and columna_nueva<mapa.shape[1]:
        #print(mapa[fila_nueva][columna_nueva])
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            #print(nodo.showPuntos())
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=nodo.puntos, padre=nodo, operador="abajo derecha inferior",tipo="MAX")
            nodos_posibles.append(nodo_aux)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionN = verificar_puntuacionN(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = nodo.puntuacionB, puntuacionN=puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=puntos, padre=nodo, operador="abajo derecha inferior",tipo="MAX")
            nodos_posibles.append(nodo_aux)

    #-------------------------
    #abajo izquierda inferior
    fila_nueva = nodo.showCaballoN()[0] + 2
    columna_nueva = nodo.showCaballoN()[1] - 1
    if fila_nueva<mapa.shape[0] and columna_nueva>=0:
        #print(mapa[fila_nueva][columna_nueva])
        #Si es una casilla vacia
        if [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) == 0:
            #print(nodo.showPuntos())
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=nodo.puntos, padre=nodo, operador="abajo izquierda inferior",tipo="MAX")
            nodos_posibles.append(nodo_aux)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoB()[0],nodo.showCaballoB()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionN = verificar_puntuacionN(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = nodo.puntuacionB, puntuacionN=puntuacionN, caballoB = nodo.caballoB, caballoN=[fila_nueva,columna_nueva], puntos=puntos, padre=nodo, operador="abajo izquierda inferior",tipo="MAX")
            nodos_posibles.append(nodo_aux)

    # print("FINAL NEGRO")
    # print("nodos",nodos_posibles)
    # print("Puntos",nodos_posibles[0].showPuntos())
    # print("CaballoNegro",nodos_posibles[0].showCaballoN())
    # print("PuntuacionNegro",nodos_posibles[0].showPuntuacionN())
    # coordenadas=[]
    # for i in nodos_posibles:
    #     coordenadas.append(i.showCaballoN())
    # print("casillas posibles",coordenadas)
    return nodos_posibles

def verFuturo(dificultad, nodoRaiz):
    nodoRaiz.padre = None
    profundidad = 0

    arbol.append(nodoRaiz)

    if dificultad == "principiante":
        profundidad = 2
    elif dificultad == "amateur":
        profundidad = 4
    elif dificultad == "experto":
        profundidad = 6
    
    expandirNodos(profundidad,[nodoRaiz])
    print("arbol:",arbol)
    coordenadasB=[]
    coordenadasN=[]
    for i in arbol:
        coordenadasB.append(i.showCaballoB())
        coordenadasN.append(i.showCaballoN())
    print("CaballoBlanco:",coordenadasB)
    print("CaballoNegro:",coordenadasN)
    nodosFiltrados=filtrarNodos(profundidad)
    arbol.clear()
    nodoSolucion=nodo_maxima_utilidad(nodosFiltrados)
    movimientoBlanco(nodoSolucion)


def expandirNodos(profundidad, nodos):
    nuevosNodos=None
    while(profundidad>0):
        if profundidad%2==0:
            profundidad=profundidad-1
            for i in nodos:
                nuevosNodos = puede_moverseB(i)
                arbol.extend(nuevosNodos)
        elif profundidad%2!=0:
            profundidad=profundidad-1
            for i in nodos:
                nuevosNodos = puede_moverseN(i)
                arbol.extend(nuevosNodos)
        expandirNodos(profundidad, nuevosNodos)


def filtrarNodos(profundidad):
    nodos=[]
    for i in arbol:
        if i.esMeta() or i.showProfundidad()==profundidad:
            nodos.append(i)
            #print("Profundidad:",i.showProfundidad())
    print("Nodos",nodos)
    return nodos

# esta funcion recibe un arreglo con los nodos de maxima profundidad por turno y nodos meta y retorna aquel que tenga una mayor funcion de utilidad
def nodo_maxima_utilidad(nodos):
    mayor = nodos[0].funcionUtilidad()
    index = 0
    for i in range(len(nodos)):
        if nodos[i].funcionUtilidad() > mayor:
            index = i
            mayor = nodos[i].funcionUtilidad()
    print("Nodo de mayor Utilidad:",nodos[index])
    print("Utilidad:",nodos[index].showUtilidad())
    return nodos[index]

def movimientoBlanco(nodo):
    global nodosPosibles
    global casillaB
    #caballoB = nodo.recorrer_arbol_arriba()
    # camino=[]
    # for i in caballoB:
    #     camino.append(i.showCaballoB())
    # print("caminoB:",camino)
    nodoaux = nodo.recorrer_arbol_arriba().pop(-2)
    print("CASILLA:",nodoaux.showCaballoB())
    casillaB = nodoaux.showCaballoB()

    nodosN=puede_moverseN(nodoaux)
    coordenadas=[]
    for i in nodosN:
        coordenadas.append(i.showCaballoN())

    nodosPosibles = coordenadas
    print("PosibleCaballoNegro:",coordenadas)
    




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
    print(puntos,caballoBlanco,caballoNegro)

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
    if(nodo.esMeta()):
        if(nodo.showPuntuacionB()>nodo.showPuntuacionN()):
            ganador ="Blanco"
        elif(nodo.showPuntuacionB()<nodo.showPuntuacionN()):
            ganador="Negro"
        else:
            ganador="Empate"

mapa = np.zeros((8,8))
mapa.astype(str)
randomize_board(8)
asignar_coordenadas()
print("este es el mapa",mapa)
find_initial_positions(mapa)

verFuturo(dificultad, nodo_raiz)
#puede_moverseB(nodo_raiz)
#puede_moverseN(nodo_raiz)
