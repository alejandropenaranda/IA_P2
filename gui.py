import pygame , sys
from pygame.locals import *
import math
from main import (dificultad,mapa,nodo_raiz)
from main import verFuturo
pygame.font.init()

#se crea el tablero, nota si se actualiza el tablero se debe de referenciar otra vez ya que no esta en el while del refresco
def create_board (matriz,size):
    i = -1 #desplazamiento en las columnas
    j = 0  #desplazamiento en las filas
    tamanho = len(matriz) #tamanho de la matriz
    aux = 0 #corrimiento de los cuadrados
    for rows in matriz:
        i = i+1
        for cells in rows:

            screen.blit(roadImage, ((j*size)+aux,(i*size)+aux))
            
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
    #se inicia la aplicacion
    #print("GUI:",movimientoBlanco,movimientoNegro)
    verFuturo(dificultad,nodo_raiz)
    pygame.init()

    #Configuracion para el texto
    auxiliar=1
    pintar_juego(nodo) #pinta el tablero

    #while para la logica o los eventos
    #while auxiliar < len(nodos_lista):
    aux = True
    while aux:
        tiempo = math.floor(pygame.time.get_ticks()/1000)

        if tiempo == auxiliar:
            #pintar_juego(nodo)
            auxiliar = auxiliar+1
            pygame.display.flip()
            pygame.display.update()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()

def pintar_juego(nodo):
    """
    freezers = nodo.showFreezers()
    cells = nodo.showCells()
    bolas = nodo.showBolas()
    semillas = nodo.showSemillas()
    kakaroto = nodo.showKakaroto()
    #fondo blanco
    
    #pintar el tablero
    

    pintar_freezers(freezers)
    pintar_cells(cells)
    pintar_balls(bolas)
    pintar_seeds(semillas)
    """
    caballoN = nodo.showCaballoN()
    caballoB = nodo.showCaballoB()

    screen.fill(white)
    create_board(mapa,imgsize)

    screen.blit(blackHorse, ((caballoN[1]*imgsize),(caballoN[0]*imgsize)))
    screen.blit(whiteHorse, ((caballoB[1]*imgsize),(caballoB[0]*imgsize)))

#def pintar_casillas_posibles():

#____________________________________________________________________________________________________________
#------------

#Definir colores
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)
    
fuente = pygame.font.SysFont('Segoe UI',28)
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


#tamanho de la GUI
aux1 = n*imgsize
aux2 = m*imgsize
size = (aux1,aux2)


#definicion de la GUI
screen = pygame.display.set_mode(size)

iniciarGUI(nodo_raiz)



#se planteo la conexion entre el main y la gui.py, ahora mismo solo se esta printeando el estado inicial, o sea el nodo_raiz cuando se tenga la solucion del problema en un array
#verificar con el proyecto anterior los cambios puntuales que se deben de hacer para que la gui se vaya actualizando
