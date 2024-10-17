# -*- coding: utf-8 -*-
# Clase Muro_indestructible

import pygame
from pygame import *
from Cuadricula import *

class Muro_indestructible(Cuadricula):
    
    def __init__(self, pos, tamano):
        Cuadricula.__init__(self,pos,tamano)

    def dibujar(self, surface):
        gris_mas_claro = (225,225,225)
        gris_luminoso = (215,215,215) # Luminosidad
        gris_piedra = (139,140,122) # Base
        gris_negruzco = (35,40,43) # Sombra
        
        # rect(Surface, color, (x,y,width,height), width=0)

        # Cuadrado base
        pygame.draw.rect(surface, gris_piedra, (self.pos[0], self.pos[1],
                                               self.ancho, self.alto))

        # Sombras
        # Sombra lateral
        pygame.draw.rect(surface, gris_negruzco, (self.pos[0], self.pos[1],
                                        5, self.alto))
        # Sombra de abajo
        pygame.draw.rect(surface, gris_negruzco, (self.pos[0], self.pos[1]+self.alto-4,
                                         self.ancho, 5))

        # Luminosidad
        # Luminosidad superior
        pygame.draw.rect(surface, gris_luminoso, (self.pos[0]+5, self.pos[1],
                                                  self.ancho-5, 5))
        # Luminosidad lateral
        pygame.draw.rect(surface, gris_luminoso, (self.pos[0]+self.ancho-5,
                                                  self.pos[1],
                                                  5, self.alto-4))
