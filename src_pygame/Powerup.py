# -*- coding: utf-8 -*-
# Implementación de Pwer-Ups

import pygame
from pygame.locals import *
from Cuadricula import *

class Powerup(Cuadricula):

    def __init__(self, pos, tamano, tipo):
        self.tipo = tipo
        Cuadricula.__init__(self, pos, tamano)

    def dibujar(self, surface):
        if self.tipo == 'velocidad':
            self.dibujar_vel(surface)
        elif self.tipo == 'explosion':
            self.dibujar_expl(surface)
        elif self.tipo == 'salida':
            self.dibujar_sal(surface)
        else:
            print 'Power-Up aún no implementado'


    def dibujar_vel(self, surface):
        # Colores
        azul_pastel = (93,155,155)
        verde_hoja = (45,87,44)
        amarillo_de_zinc = (248,243,53)
        amarillo_senales = (229,190,1)
        
        # rect(Surface, color, (x,y,width,height), thickness)
        # line(Surface, color, start_pos, end_pos, width=1)
        # circle(Surface, color, pos, radius, width=0)
        # ellipse(Surface, color, [x, y, width, height], line_thickness)

        # Fondo
        pygame.draw.rect(surface, azul_pastel, [self.pos[0], self.pos[1],
                        self.ancho, self.alto])

        # Punta del pie
        pygame.draw.ellipse(surface, amarillo_de_zinc, [self.pos[0]+5,
                            self.pos[1]+25, 20, 10])
        
        # Pie
        pygame.draw.rect(surface, verde_hoja, [self.pos[0]+25, self.pos[1]+5,
                         10, 30])
        pygame.draw.rect(surface, verde_hoja, [self.pos[0]+15, self.pos[1]+25,
                         10, 10])

        # Ruedas
        pygame.draw.circle(surface, amarillo_senales, [self.pos[0]+15,
                            self.pos[1]+36], 4)
        pygame.draw.circle(surface, amarillo_senales, [self.pos[0]+30,
                            self.pos[1]+36], 4)


    def dibujar_expl(self, surface):
        # Colores
        azul_noche_perlado = (16,44,84)
        gris_plata = (138,149,151)

        # Fondo
        pygame.draw.rect(surface, azul_noche_perlado, [self.pos[0], self.pos[1],
                                                       self.ancho, self.alto])
        # Marco
        pygame.draw.rect(surface, gris_plata, [self.pos[0], self.pos[1],
                                               self.alto, self.ancho], 2)

        # Rayo
        pygame.draw.line(surface, gris_plata, [self.pos[0]+self.ancho, self.pos[1]],
                         [self.pos[0]+6, self.pos[1]+self.alto-6])
        
        pygame.draw.line(surface, gris_plata, [self.pos[0]+30, self.pos[1]+10],
                         [self.pos[0]+20, self.pos[1]+7])
        
        pygame.draw.line(surface, gris_plata, [self.pos[0]+20, self.pos[1]+7],
                         [self.pos[0]+10, self.pos[1]+3])

        pygame.draw.line(surface, gris_plata, [self.pos[0]+20, self.pos[1]+7],
                         [self.pos[0]+12, self.pos[1]+10])

        pygame.draw.line(surface, gris_plata, [self.pos[0]+12, self.pos[1]+10],
                         [self.pos[0]+5, self.pos[1]+13])

        pygame.draw.line(surface, gris_plata, [self.pos[0]+12, self.pos[1]+10],
                         [self.pos[0]+5, self.pos[1]+25])

        pygame.draw.line(surface, gris_plata, [self.pos[0]+20, self.pos[1]+20],
                         [self.pos[0]+10, self.pos[1]+23])

        pygame.draw.line(surface, gris_plata, [self.pos[0]+30, self.pos[1]+10],
                         [self.pos[0]+25, self.pos[1]+25])

        pygame.draw.line(surface, gris_plata, [self.pos[0]+25, self.pos[1]+25],
                         [self.pos[0]+20, self.pos[1]+35])

        pygame.draw.line(surface, gris_plata, [self.pos[0]+25, self.pos[1]+25],
                         [self.pos[0]+30, self.pos[1]+35])


    def dibujar_sal(self, surface):
        # Colores
        azul_luminoso = (59,131,189)

        # Forma
        pygame.draw.rect(surface, azul_luminoso, [self.pos[0], self.pos[1],
                                               self.alto, self.ancho])

        
