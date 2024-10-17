# -*- coding: utf-8 -*-
# Clase Bomba

import pygame
from pygame.locals import *
from Cuadricula import *
from Explosion import *

class Bomba(Cuadricula):

    def __init__(self, pos, tamano):
        self.tiempoVida = 0
        self.recienPuesta = True # Evita Bomberman se pegue en bomba
        Cuadricula.__init__(self, pos, tamano)

    def explotar(self):
        self.destruir() # Deja vida en 0

    def dibujar(self,surface):
        # Colores
        negro = (0,0,0)
        azul_noche_perlado = (16,44,84)

        # Base
        # Centro bomba
        xi = self.pos[0] + 20
        yi = self.pos[1] + 25
        
        # rect(Surface, color, (x,y,width,height), thickness)
        # line(Surface, color, start_pos, end_pos, width=1)
        # circle(Surface, color, pos, radius, width=0)
        # ellipse(Surface, color, [x, y, width, height], line_thickness)
        
        # Cuerpo
        pygame.draw.circle(surface, negro, [xi+3,yi+3], 12)
        pygame.draw.circle(surface, azul_noche_perlado, [xi, yi], 12)
        
