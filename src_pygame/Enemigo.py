# -*- coding: utf-8 -*-
# Enemigos de bomberman

import pygame
from pygame.locals import *
from Cuadricula import *

class Enemigo(Cuadricula):

    def __init__(self, pos, tamano, tipo):
        self.tipo = tipo
        Cuadricula.__init__(self, pos, tamano)

    def dibujar(self,surface):
        if self.tipo == 1:
            self.dibujar_1(surface)
        elif self.tipo == 2:
            self.dibujar_2(surface)
        else:
            print "Enemigo no implementado"

    def dibujar_1(self,surface):
        # Colores
        negro = (0,0,0)
        azul_noche = (37,40,80)
        rosa_claro = (234,137,154)
        rojo_pardo = (120,31,25)
        azul_celeste = (34, 113, 179)
        blanco_perla = (234,230,202)
        blanco_trafico = (246,246,246)
        aluminio_gris = (143,143,143)
        aluminio_blanco = (165,165,165)
        
        # rect(Surface, color, (x,y,width,height), thickness)
        # line(Surface, color, start_pos, end_pos, width=1)
        # circle(Surface, color, pos, radius, width=0)
        # ellipse(Surface, color, [x, y, width, height], line_thickness)

        # Piernas
        pygame.draw.rect(surface, blanco_trafico, (self.pos[0]+10,
                         self.pos[1]+self.alto-10, 5, 10))
        pygame.draw.rect(surface, blanco_trafico, (self.pos[0]+25,
                         self.pos[1]+self.alto-10, 5, 10))

        # Cuerpo
        pygame.draw.circle(surface, negro, (self.pos[0]+20, self.pos[1]+19),
                           15)

        # Pies
        pygame.draw.ellipse(surface, rojo_pardo, [self.pos[0]+5, self.pos[1]+self.alto-5,
                            15, 7])
        pygame.draw.ellipse(surface, rojo_pardo, [self.pos[0]+20, self.pos[1]+self.alto-5,
                            15, 7])
        
        # Brazos
        pygame.draw.rect(surface, rosa_claro, [self.pos[0]+34, self.pos[1]+10,
                         5,10])
        pygame.draw.rect(surface, rosa_claro, [self.pos[0]+1, self.pos[1]+10,
                         5,10])

        # Guantes
        pygame.draw.circle(surface, azul_celeste, [self.pos[0]+self.ancho-3,
                           self.pos[1]+21],3)
        pygame.draw.circle(surface, azul_celeste, [self.pos[0]+3,
                           self.pos[1]+21],3)

        # Cabeza
        pygame.draw.ellipse(surface, negro, [self.pos[0]+3,
                            self.pos[1]-10, 34, 20])

        # Cara
        pygame.draw.rect(surface, rosa_claro, [self.pos[0]+10, self.pos[1]-5,
                                               20,10])

        # Ojos
        pygame.draw.rect(surface, negro, [self.pos[0]+14, self.pos[1]-3,
                                          2,6])
        pygame.draw.rect(surface, negro, [self.pos[0]+24, self.pos[1]-3,
                                          2,6])
        
        # Calavera
        xi = self.pos[0] + 10
        yi = self.pos[1] + 10
        # Maxilar
        pygame.draw.rect(surface, blanco_perla, [xi+7, yi+9, 6, 3])

        # Mandíbula
        pygame.draw.rect(surface, blanco_perla, [xi+7, yi+14, 6, 3])

        # Dientes
        pygame.draw.rect(surface, negro, [xi+9, yi+9, 1, 3])
        pygame.draw.rect(surface, negro, [xi+11, yi+9, 1, 3])

        pygame.draw.rect(surface, negro, [xi+9, yi+14, 1, 3])
        pygame.draw.rect(surface, negro, [xi+11, yi+14, 1, 3])
        
        # Cabeza
        pygame.draw.ellipse(surface, blanco_trafico, [xi+2, yi+2, 16, 10])

        # Ojos
        pygame.draw.circle(surface, negro, [xi+8,yi+6], 2)
        pygame.draw.circle(surface, negro, [xi+12,yi+6], 2)

        # Espada
        xi = self.pos[0]+self.ancho-3
        yi = self.pos[1]+21
        # Mango
        pygame.draw.line(surface, negro, [xi,yi], [xi+2,yi-8], 2)
        pygame.draw.line(surface, negro, [xi-1,yi-9], [xi+4,yi-7], 2)

        # Filo
        pygame.draw.line(surface, aluminio_blanco, [xi+2,yi-8], [xi+5,yi-20], 3)
        

    def dibujar_2(self,surface):
        # Colores
        negro = (0,0,0)
        azul_noche = (37,40,80)
        rosa_claro = (234,137,154)
        rojo_pardo = (120,31,25)
        azul_celeste = (34, 113, 179)
        blanco_perla = (234,230,202)
        blanco_trafico = (246,246,246)
        pardo_rojo = (89,35,33)
        
        # rect(Surface, color, (x,y,width,height), thickness)
        # line(Surface, color, start_pos, end_pos, width=1)
        # circle(Surface, color, pos, radius, width=0)
        # ellipse(Surface, color, [x, y, width, height], line_thickness)

        # Piernas
        pygame.draw.rect(surface, azul_noche, (self.pos[0]+10,
                         self.pos[1]+self.alto-10, 5, 10))
        pygame.draw.rect(surface, azul_noche, (self.pos[0]+25,
                         self.pos[1]+self.alto-10, 5, 10))

        # Cuerpo
        pygame.draw.circle(surface, pardo_rojo, (self.pos[0]+20, self.pos[1]+19),
                           15)

        # Pies
        pygame.draw.ellipse(surface, negro, [self.pos[0]+5, self.pos[1]+self.alto-5,
                            15, 7])
        pygame.draw.ellipse(surface, negro, [self.pos[0]+20, self.pos[1]+self.alto-5,
                            15, 7])
        
        # Brazos
        pygame.draw.rect(surface, rosa_claro, [self.pos[0]+34, self.pos[1]+10,
                         5,10])
        pygame.draw.rect(surface, rosa_claro, [self.pos[0]+1, self.pos[1]+10,
                         5,10])

        # Guantes
        pygame.draw.circle(surface, azul_noche, [self.pos[0]+self.ancho-3,
                           self.pos[1]+21],3)
        pygame.draw.circle(surface, azul_noche, [self.pos[0]+3,
                           self.pos[1]+21],3)

        # Cabeza
        pygame.draw.ellipse(surface, pardo_rojo, [self.pos[0]+3,
                            self.pos[1]-10, 34, 20])

        # Cara
        pygame.draw.rect(surface, rosa_claro, [self.pos[0]+10, self.pos[1]-5,
                                               20,10])

        # Ojos
        # Parche
        pygame.draw.circle(surface, negro, [self.pos[0]+15, self.pos[1]], 4)
        pygame.draw.line(surface, negro, [self.pos[0]+15, self.pos[1]-8],
                         [self.pos[0]+15,self.pos[1]],2)
        pygame.draw.line(surface, negro, [self.pos[0]+3, self.pos[1]],
                         [self.pos[0]+15, self.pos[1]], 2)
        pygame.draw.rect(surface, negro, [self.pos[0]+24, self.pos[1]-3,
                                          2,6])
        
        # Calavera
        xi = self.pos[0] + 10
        yi = self.pos[1] + 10
        # Maxilar
        pygame.draw.rect(surface, blanco_perla, [xi+7, yi+9, 6, 3])

        # Mandíbula
        pygame.draw.rect(surface, blanco_perla, [xi+7, yi+14, 6, 3])

        # Dientes
        pygame.draw.rect(surface, negro, [xi+9, yi+9, 1, 3])
        pygame.draw.rect(surface, negro, [xi+11, yi+9, 1, 3])

        pygame.draw.rect(surface, negro, [xi+9, yi+14, 1, 3])
        pygame.draw.rect(surface, negro, [xi+11, yi+14, 1, 3])
        
        # Cabeza
        pygame.draw.ellipse(surface, blanco_trafico, [xi+2, yi+2, 16, 10])

        # Ojos
        pygame.draw.circle(surface, negro, [xi+8,yi+6], 2)
        pygame.draw.circle(surface, negro, [xi+12,yi+6], 2)
        
