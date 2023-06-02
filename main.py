from node import Nodo
import numpy as np

# Aqui se abre el archivo de texto que contiene el mapa y se guarda en la variable mapa en forma de matriz

# def crear_mapa_desde_archivo(nombre_archivo):
#     matriz = []
#     with open(nombre_archivo, 'r') as archivo:
#         lineas = archivo.readlines()
#         for linea in lineas:
#             valores = linea.strip().split()  # Separar los valores por espacio en blanco
#             fila = [valor for valor in valores]  # No es necesario convertirlos a tipo float en este caso
#             matriz.append(fila)
#     return matriz

def crear_mapa_desde_archivo(nombre_archivo):
    with open(nombre_archivo) as archivo:
        filas = archivo.readlines()
        mapa = []
        for fila in filas:
            mapa.append([x for x in fila.split()])
        archivo.close()
        return np.array(mapa)

mapa = crear_mapa_desde_archivo('Prueba1.txt')
#print(mapa)
# #__________________________________________definicion de variables globales
nodo_raiz= Nodo(puntuacionB=0,puntuacionN=0, caballoB=[], caballoN=[], puntos=[])

# #funcion que encuentra la posicion inicial de todos los elementos del tablero
def find_initial_positions(board):
    puntos = []
    caballoB = None
    caballoN = None
    for i in range(len(board)):
        for h in range(len(board)):
            if mapa[i][h] == "B":
                caballoB = [i,h]
                mapa[i][h]=0
            elif mapa[i][h] == "N":
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
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="arriba derecha superior")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="arriba derecha superior")
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
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="arriba izquierda superior")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="arriba izquierda superior")
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
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="arriba derecha inferior")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="arriba derecha inferior")
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
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="arriba izquierda inferior")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="arriba izquierda inferior")
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
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="abajo derecha superior")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="abajo derecha superior")
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
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="abajo izquierda superior")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="abajo izquierda superior")
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
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="abajo derecha inferior")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="abajo derecha inferior")
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
            nodo_aux = Nodo(nodo.puntuacionB, nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=nodo.puntos, padre=nodo, operador="abajo izquierda inferior")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)
        #Si es una casilla con puntuacion
        elif [fila_nueva,columna_nueva] != [nodo.showCaballoN()[0],nodo.showCaballoN()[1]] and int(mapa[fila_nueva][columna_nueva]) != 0: 
            #print(nodo.showPuntos())
            puntos, puntuacionB = verificar_puntuacionB(nodo, fila_nueva, columna_nueva)
            nodo_aux = Nodo(puntuacionB = puntuacionB, puntuacionN=nodo.puntuacionN, caballoB = [fila_nueva,columna_nueva], caballoN=nodo.caballoN, puntos=puntos, padre=nodo, operador="abajo izquierda inferior")
            nodo_verificado = evitar_devolverce(nodo_aux,nodos_recorridos)
            #print(mapa[fila_nueva,columna_nueva])
            if nodo_verificado != None:
                nodos_posibles.append(nodo_verificado)

    print("FINAL")
    print("nodos",nodos_posibles)
    print("Puntos",nodos_posibles[0].showPuntos())
    print("CaballoBlanco",nodos_posibles[0].showCaballoB())
    print("PuntuacionBlanco",nodos_posibles[0].showPuntuacionB())
    return nodos_posibles
            


find_initial_positions(mapa)

puede_moverseB(nodo_raiz)