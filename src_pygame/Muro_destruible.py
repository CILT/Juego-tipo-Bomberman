# -*- coding: utf-8 -*-
# Clase Muro_destruible

import pygame
from pygame.locals import *
from Cuadricula import *

import os

class Muro_destruible(Cuadricula):
    
    def __init__(self, pos, tamano):
        Cuadricula.__init__(self, pos, tamano)


    def dibujar(self,surface):
        gris = (128,128,128)
        gris_oscuro = (64, 64, 64)
        
        # rect(Surface, color, (x,y,width,height), thickness)
        # line(Surface, color, start_pos, end_pos, width=1)

        # Cuadrado base
        pygame.draw.rect(surface, gris,(self.pos[0],self.pos[1],self.ancho,self.alto))

        # Líneas tipo ladrillo
        # Horizontales
        pygame.draw.line(surface, gris_oscuro,
                         (self.pos[0], self.pos[1]+int(self.alto/3.0)),
                         (self.pos[0]+self.ancho-1,self.pos[1]+int(self.alto/3.0)))
        pygame.draw.line(surface, gris_oscuro,
                         (self.pos[0], self.pos[1]+int(self.alto*2/3.0)),
                         (self.pos[0]+self.ancho-1,self.pos[1]+int(self.alto*2/3.0)))
        # Verticales
        pygame.draw.rect(surface, gris_oscuro, (self.pos[0]+int(self.ancho/3.0),
                                                self.pos[1],
                                                1,
                                                int(self.alto/3.0)))
        pygame.draw.rect(surface, gris_oscuro, (self.pos[0]+int(self.ancho/3.0),
                                                self.pos[1]+int(self.alto*2/3.0),
                                                1,
                                                int(self.alto/3.0)))
        pygame.draw.rect(surface, gris_oscuro, (self.pos[0]+int(self.ancho*2/3.0),
                                                self.pos[1]+int(self.alto/3.0),
                                                1,
                                                int(self.alto/3.0)))

        

                         

##
##"""
##Constantes de la aplicación
##"""
##COLOR_FONDO = (255,255,0) # No definido
##FPS = 60.0 # Cuadros por segundo
##tamanoCuadricula = 40
##display_h = 13*tamanoCuadricula
##display_w = 15*tamanoCuadricula
##titulo = 'Ejemplo choro'
##
##"""
##Creación de la ventana
##"""
##pygame.init()
##DISPLAYSURF = pygame.display.set_mode((display_w,display_h))
##os.environ['SDL_VIDEO_CENTERED'] = '1' # Ventana centrada al iniciarse
### Crea el reloj de la aplicación
##reloj = pygame.time.Clock()  # Reloj de pygame
##
##DT = 1.0 / FPS  # Cuánto tiempo real entre cada cuadro
##t = 0.0  # Tiempo de simulación. Inicializa en 0.
##
##muro = Muro_destruible(DISPLAYSURF,[200,300],tamanoCuadricula)
##
##run = True
##while run:
##
##    # Nuevo cuadro
##    reloj.tick(FPS)
##    # Título
##    pygame.display.set_caption(titulo + ' (FPS={0})'.format(int(reloj.get_fps())))
##    
##    """
##    Controlador
##    """
##    # Manejo de eventos del teclado, mouse, etc.
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            run = False
##
##        print event
##        
##        if event.type == KEYDOWN:
##            if event.key == K_q:
##                run = False
##    DISPLAYSURF.fill(COLOR_FONDO)
##    muro.dibujar()
##    pygame.display.flip()
##pygame.quit()
##quit()
