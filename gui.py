import pygame , sys
from pygame.locals import *
import math, time
from main import (dificultad,mapa,nodo_raiz)
from main import verFuturo, verificarGanador
from node import Nodo
pygame.font.init()

#se crea el tablero, nota si se actualiza el tablero se debe de referenciar otra vez ya que no esta en el while del refresco


def create_board (matriz,size):
    print("MATRIZ:",matriz)
    pintar_cuadricula(matriz,size)
    pintar_puntos(matriz,size)


def pintar_cuadricula(matriz,size):
    i = -1 #desplazamiento en las columnas
    j = 0  #desplazamiento en las filas
    tamanho = len(matriz) #tamanho de la matriz
    aux = 0 #corrimiento de los cuadrados
    for rows in matriz:
        i = i+1
        for cells in rows:
            screen.blit(roadImage, ((j*size)+aux,(i*size)+aux))
            j = j+1
            if (j==tamanho):
                j = 0
                break
            if (i==tamanho):
                break

def pintar_puntos(matriz,size):
    i = -1 #desplazamiento en las columnas
    j = 0  #desplazamiento en las filas
    tamanho = len(matriz) #tamanho de la matriz
    for rows in matriz:
        i = i+1
        for cells in rows:
            if (cells == 1):
                screen.blit(points1, ((j*size),(i*size)))
            elif (cells == 2):
                screen.blit(points2, ((j*size),(i*size)))
            elif (cells == 3):
                screen.blit(points3, ((j*size),(i*size)))
            elif (cells == 4):
                screen.blit(points4, ((j*size),(i*size)))
            elif (cells == 5):
                screen.blit(points5, ((j*size),(i*size)))
            elif (cells == 6):
                screen.blit(points6, ((j*size),(i*size)))
            elif (cells == 7):
                screen.blit(points7, ((j*size),(i*size)))
            j = j+1
            if (j==tamanho):
                j = 0
                break
            if (i==tamanho):
                break

    # se pintan los 
    """
    aux1 = 1
    for punto in puntos:
        screen.blit(points_values[aux1-1], ((int(punto[1])*size),(int(punto[0])*size)))
        aux1 = aux1 + 1
    screen.blit(blackHorse, ((caballoNegro[0][1]*size),(caballoNegro[0][0]*size)))
    screen.blit(whiteHorse, ((caballoBlanco[0][1]*size),(caballoBlanco[0][0]*size)))
    """
    return True

#-----------------

# tamaño de las filas y columnas 
# debe ser nxn
n = 8
m = 8
#-----------------#
#____________________________________________________________________________________________________________
def iniciarGUI(nodo):
    print("_____________________PuntosINICIO:",nodo_raiz.showPuntos())
    global puede_jugar, hijoMax, movimientoNegro, nodosNegro, auxiliar, tiempo
    tiempo=0
    auxiliar=0
    hijoMax=None
    movimientoNegro=None
    nodosNegro=None
    puede_jugar=False
    #se inicia la aplicacion
    #print("GUI:",movimientoBlanco,movimientoNegro)
    movimientoNegro, hijoMax, nodosNegro = verFuturo(dificultad,nodo_raiz)
    

    
    print("GUI NEGRO:",movimientoNegro)
    pygame.init()

    #Configuracion para el texto
    auxiliar=2 

    pintar_juego(nodo)
    #while para la logica o los eventos
    #while auxiliar < len(nodos_lista):
    aux = True
    t0 = time.time()
    while aux:
        t1=time.time()
        #tiempo = math.floor(pygame.time.get_ticks()/1000)
        dt=t1-t0
        if dt>2:
            if puede_jugar==False:
                #pintar_juego(nodo)
                pintar_juego(hijoMax)
                pintar_casillas_posibles(hijoMax,movimientoNegro)
                puede_jugar=True
            t1=t0
        finalizar_juego(hijoMax)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and puede_jugar==True:
                global pos, movimientoUsuario
                movimientoUsuario = None
                mousePos = pygame.mouse.get_pos()
                print('x: ',mousePos[0], 'y:',mousePos[1])
                pos,acierto = checkCasilla(mousePos, movimientoNegro)
                if acierto:
                    for i in range(len(nodosNegro)):
                        print('AQUI: ', nodosNegro[i].showCaballoB())
                    movimientoUsuario = nodosNegro[pos]
                    pintar_juego(movimientoUsuario)
                    print("------------nodoParaSanta----------:",nodosNegro[pos].showCaballoN())
                    puede_jugar=False
                    movimientoNegro, hijoMax, nodosNegro = verFuturo(dificultad,movimientoUsuario)
                    finalizar_juego(movimientoUsuario)

def finalizar_juego(nodo):
    ganador= verificarGanador(nodo)
    if ganador=="Blanco":
        print('gano el blanco')
        pintar_estadisticas(nodo, 1)
        #sys.exit()
    elif ganador=="Negro":
        print('gano el negro')
        pintar_estadisticas(nodo, 2)
        #sys.exit()
    elif ganador=="Empate":
        print('empate')
        pintar_estadisticas(nodo, 3)
        #sys.exit()

def pintar_estadisticas(nodo,case):
    screen.fill(white)
    puntosN = nodo.showPuntuacionN()
    puntosB = nodo.showPuntuacionB()
    text2 = fuente2.render('La dificultad de la maquina fue '+ dificultad, True, black)

    P1 = fuente2.render('Puntuacion final del P1: '+ str(puntosB), True, black)
    P2 = fuente2.render('Puntuacion final del P2: '+ str(puntosN), True, black)
    if (case == 1):
        text = fuente2.render('Ha ganado el jugador P1', True, black)
    elif (case == 2):
        text = fuente2.render('Ha ganado el jugador P2', True, black)
    elif (case == 3):
        text = fuente2.render('El juego ha terminado en empate', True, black)
    
    screen.blit(text, (15, 50))
    screen.blit(text2, (15, 100))
    screen.blit(P1,(15,150))
    screen.blit(P2,(15,200))

    pygame.display.flip()
    pygame.display.update()



def pintar_movimiento_maquina(nodo):


    caballoN = nodo.showCaballoN()
    caballoB = nodo.showCaballoB()

    screen.fill(white)
    create_board(modificar_mapa(mapa,nodo),imgsize)
    screen.blit(blackHorse, ((caballoN[1]*imgsize),(caballoN[0]*imgsize)))
    screen.blit(whiteHorse, ((caballoB[1]*imgsize),(caballoB[0]*imgsize)))


def modificar_mapa(mapa, nodo):
    print("Puntos:",nodo.showPuntos())
    i = -1 #desplazamiento en las columnas
    tamanho = len(mapa)
    tablero = mapa.copy()
    for rows in mapa:
        i = i+1
        for j in range(len(mapa)):
            cells = int(rows[j])
            #print("cells:",j)
            #print("INTcells:",int(j))
            #print("rows:",rows)
            aux = [i,int(j)]
            #print("AUX:",aux)
            #print("XD",rows[j])
            #print("---------")
            # print('aqui aux : ',aux)
            if (cells == 1):
                if not aux in nodo.showPuntos():
                    tablero[i][int(j)] = 0
            elif (cells == 2):
                if not aux in nodo.showPuntos():
                    tablero[i][int(j)] = 0
            elif (cells == 3):
                if not aux in nodo.showPuntos():
                    tablero[i][int(j)] = 0
            elif (cells == 4):
                if not aux in nodo.showPuntos():
                    tablero[i][int(j)] = 0
            elif (cells == 5):
                if not aux in nodo.showPuntos():
                    tablero[i][int(j)] = 0
            elif (cells == 6):
                if not aux in nodo.showPuntos():
                    tablero[i][int(j)] = 0
            elif (cells == 7):
                if not aux in nodo.showPuntos():
                    tablero[i][int(j)] = 0
            if (i==tamanho):
                break
    return tablero

def pintar_juego(nodo):
    screen.fill(white)
    create_board(modificar_mapa(mapa,nodo),imgsize)
    pintar_caballos(nodo,imgsize)
    pintar_score(nodo)
    pygame.display.flip()
    pygame.display.update()
    #screen.blit(blackHorse, ((caballoN[1]*imgsize),(caballoN[0]*imgsize)))
    #screen.blit(whiteHorse, ((caballoB[1]*imgsize),(caballoB[0]*imgsize)))

def pintar_caballos(nodo,size):

    caballoN = nodo.showCaballoN()
    caballoB = nodo.showCaballoB()

    screen.blit(blackHorse, ((caballoN[1]*size),(caballoN[0]*size)))
    screen.blit(whiteHorse, ((caballoB[1]*size),(caballoB[0]*size)))

def pintar_casillas_posibles(nodo,casillas):
    board = modificar_mapa(mapa, nodo)
    print('tablero:', board)
    pintar_cuadricula(board,imgsize)
    for casilla in casillas:
        screen.blit(tileImage, ((casilla[1]*imgsize),(casilla[0]*imgsize)))
    pintar_puntos(board,imgsize)    
    pintar_caballos(nodo,imgsize) 
    pygame.display.flip()
    pygame.display.update()

#def actualizar_casillas_posibles(nodo, casillas):
    


def checkCasilla(posicion, posibles_movimientos):
    index = 0
    acierto=False

    for i in range(len(posibles_movimientos)):
        coordx = posibles_movimientos[i][0]
        coordy = posibles_movimientos[i][1]
        if posicion[1] > coordx*imgsize and posicion[1] < (coordx+1)*imgsize:
            if posicion[0] > coordy*imgsize and posicion[0] < (coordy+1)*imgsize:
                index = i
                print('casilla correcta pulsada')
                pintarCaballoN(posibles_movimientos[index])
                acierto=True
                break
    return index,acierto
            


def pintar_score(nodo):
    puntosN = nodo.showPuntuacionN()
    puntosB = nodo.showPuntuacionB()
    P1 = font.render('P1: '+ str(puntosB), True, black)
    P2 = font.render('P2: '+ str(puntosN), True, black)
    screen.blit(P1,(10,725))
    screen.blit(P2,(600,725))


def pintarCaballoN(pos):
    screen.blit(blackHorse, ((pos[1]*imgsize),(pos[0]*imgsize)))
    pygame.display.flip()
    pygame.display.update()
#____________________________________________________________________________________________________________
#------------

#Definir colores
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)
    
fuente = pygame.font.SysFont('Segoe UI',28)
font = pygame.font.SysFont('arialblack',30)
fuente2 = pygame.font.SysFont('Segoe UI', 40)
texto = fuente.render("prueba de texto",True,black)

#se carga la imagen del raton y demas
imgsize = 90
auxsize = 85
roadImage = pygame.image.load('imagenes/path.png')
points1 = pygame.transform.scale(pygame.image.load('imagenes/1.png'), (auxsize,auxsize))
points2 = pygame.transform.scale(pygame.image.load('imagenes/2.png'), (auxsize,auxsize))
points3 = pygame.transform.scale(pygame.image.load('imagenes/3.png'), (auxsize,auxsize))
points4 = pygame.transform.scale(pygame.image.load('imagenes/4.png'), (auxsize,auxsize))
points5 = pygame.transform.scale(pygame.image.load('imagenes/5.png'), (auxsize,auxsize))
points6 = pygame.transform.scale(pygame.image.load('imagenes/6.png'), (auxsize,auxsize))
points7 = pygame.transform.scale(pygame.image.load('imagenes/7.png'), (auxsize,auxsize))
blackHorse = pygame.transform.scale(pygame.image.load('imagenes/CN.png'), (auxsize,auxsize))
whiteHorse = pygame.transform.scale(pygame.image.load('imagenes/CB.png'), (auxsize,auxsize))
tileImage = pygame.transform.scale(pygame.image.load('imagenes/casilla.png'), (imgsize,imgsize))


#tamanho de la GUI
aux1 = n*imgsize
aux2 = m*imgsize + 50
size = (aux1,aux2)


#definicion de la GUI
screen = pygame.display.set_mode(size)

iniciarGUI(nodo_raiz)




#se planteo la conexion entre el main y la gui.py, ahora mismo solo se esta printeando el estado inicial, o sea el nodo_raiz cuando se tenga la solucion del problema en un array
#verificar con el proyecto anterior los cambios puntuales que se deben de hacer para que la gui se vaya actualizando
