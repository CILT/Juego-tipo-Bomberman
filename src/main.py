# -*- coding: utf-8 -*-
# Tarea 2
# Autor: Cristián Llull T.
# Este arhivo realiza la tarea 2
# Programa probado en Python 2.7

"""
Importa librerías
"""
# Importar PyGame
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Importa módulos
from Vista import *
from Controlador import *
from Escenario import *
from Fondo import *

# Otras librerías
import os

""" Función para inicializar OpenGL """
def init_opengl(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, w, 0.0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Variables de opengl
    glClearColor(0.0, 0.0, 0.0, 0.0) # Color del fondo
    glShadeModel(GL_SMOOTH)
    glClearDepth(1.0)

"""
Constantes de la aplicación
"""
COLOR_FONDO = (40/255.0,114/255.0,51/255.0) # Verdoso
FPS = 60.0 # Cuadros por segundo.
DT = 1.0 / FPS
tamanoCuadricula = 40 # En pixeles
display_h = 13*tamanoCuadricula
display_w = 15*tamanoCuadricula
titulo = 'Bomberman'

pygame.init()
pygame.display.set_mode((display_w,display_h), DOUBLEBUF | OPENGL)
init_opengl(display_w, display_h)
reloj = pygame.time.Clock()
os.environ['SDL_VIDEO_CENTERED'] = '1' # Ventana centrada al iniciarse

"""
Objetos
"""
fondo = Fondo(0,0,display_w,display_h,COLOR_FONDO)
escenario = Escenario(tamanoCuadricula, fondo)
escenario.crear()
controlador = Controlador(escenario)
ventana = Vista(FPS, titulo, display_w, display_h, reloj)

"""
Bucle de la aplicación
"""
run = True
while run:
    """
    Controlador
    """
    run = controlador.controlar(run, DT)

    """
    Vista
    """    
    ventana.dibujar(escenario)
        
pygame.quit()
quit()

