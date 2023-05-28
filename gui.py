import pygame , sys
from pygame.locals import *
import math

pygame.font.init()

#se crea el tablero, nota si se actualiza el tablero se debe de referenciar otra vez ya que no esta en el while del refresco
def create_board (size):
    i = -1 #desplazamiento en las columnas
    j = 0  #desplazamiento en las filas
    tamanho = 8 #tamanho de la matriz
    aux = 0 #corrimiento de los cuadrados
    for rows in range(m):
        i = i+1
        for cells in range(n):
            screen.blit(roadImage, ((j*size)+aux,(i*size)+aux))
            if(rows == 1 and cells == 6):
                screen.blit(blackHorse, ((j*size)+aux,(i*size)+aux))
            if(rows == 4 and cells == 1):
                screen.blit(whiteHorse, ((j*size)+aux,(i*size)+aux))
            j = j+1
            if (j==tamanho):
                j = 0
                break
            if (i==tamanho):
                break
    return True
#-----------------

# tamaño de las filas y columnas 
# debe ser nxn
n = 8
m = 8
#-----------------#
#____________________________________________________________________________________________________________
def iniciarGUI():
    #se inicia la aplicacion
    
    pygame.init()

    #Configuracion para el texto
    auxiliar=1
    create_board(imgsize) #pinta el tablero

    #while para la logica o los eventos
    #while auxiliar < len(nodos_lista):
    aux = True
    while aux:
        tiempo = math.floor(pygame.time.get_ticks()/1000)

        if tiempo == auxiliar:
            create_board(imgsize)
            auxiliar = auxiliar+1
            pygame.display.flip()
            pygame.display.update()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
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
blackHorse = pygame.transform.scale(pygame.image.load('imagenes/CN.png'), (auxsize,auxsize))
whiteHorse = pygame.transform.scale(pygame.image.load('imagenes/CB.png'), (auxsize,auxsize))


#tamanho de la GUI
aux1 = n*imgsize
aux2 = m*imgsize
size = (aux1,aux2)

#definicion de la GUI
screen = pygame.display.set_mode(size)

iniciarGUI()