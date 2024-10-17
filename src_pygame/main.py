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

# Importa módulos
from Vista import *
from Controlador import *
from Escenario import *

# Otras librerías
import os

"""
Constantes de la aplicación
"""
COLOR_FONDO = (40,114,51) # No definido
FPS = 60.0 # Cuadros por segundo
tamanoCuadricula = 40 # En pixeles
display_h = 13*tamanoCuadricula
display_w = 15*tamanoCuadricula
titulo = 'Bomberman'

"""
Parámetros de creación de la ventana
"""
pygame.init()
DISPLAYSURF = pygame.display.set_mode((display_w,display_h))
os.environ['SDL_VIDEO_CENTERED'] = '1' # Ventana centrada al iniciarse
# Crea el reloj de la aplicación
reloj = pygame.time.Clock()  # Reloj de pygame
DT = 1.0 / FPS  # Cuánto tiempo real entre cada cuadro
t = 0.0  # Tiempo de simulación. Inicializa en 0.

"""
Objetos
"""
escenario = Escenario(tamanoCuadricula, DISPLAYSURF)
escenario.crear()
controlador = Controlador(escenario)
ventana = Vista(DISPLAYSURF, reloj, FPS, titulo, COLOR_FONDO)

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

ventana.gameOver(escenario)
pygame.quit()
quit()

