# -*- coding: utf-8 -*-
# Jugador Bomberman

import pygame
from pygame.locals import *
from Cuadricula import *
from Bomba import *

class Bomberman(Cuadricula):

    def __init__(self, pos, tamano, tamanoExplosion=2, velocidad=2, cantBombas=1):
        self.tamExplosion = tamanoExplosion
        self.vel = velocidad
        self.cantBombas = cantBombas
        Cuadricula.__init__(self, pos, tamano)
        
    # Se redefinirá la función de choque exclusivamente para el bomberman
    # El objetivo es hace más llevadero el juego y que camine mejor por los
    # caminos.
    def choca(self, cuadr2):
        dist_x = abs(self.pos[0] - cuadr2.pos[0])
        dist_y = abs(self.pos[1] - cuadr2.pos[1])
        margen = 2
        if (dist_x < self.ancho - margen and dist_y < self.alto - margen):
            return True
        return False
    
    # Llamada a poner una bomba
    # Se retorna la bomba para que el escenario la tenga
    def ponerBomba(self):
        x = int(round(self.pos[0]*1.0/self.ancho))
        y = int(round(self.pos[1]*1.0/self.alto))
        bomba = Bomba([x*self.ancho,y*self.alto],self.ancho)
        return bomba

    def dibujar(self,surface):
        # Colores
        negro = (0,0,0)
        azul_noche = (37,40,80)
        rosa_claro = (234,137,154)
        rojo_pardo = (120,31,25)
        azul_celeste = (34, 113, 179)
        
        # rect(Surface, color, (x,y,width,height), thickness)
        # line(Surface, color, start_pos, end_pos, width=1)
        # circle(Surface, color, pos, radius, width=0)
        # ellipse(Surface, color, [x, y, width, height], line_thickness)

        # Piernas
        pygame.draw.rect(surface, rosa_claro, (self.pos[0]+10,
                         self.pos[1]+self.alto-10, 5, 10))
        pygame.draw.rect(surface, rosa_claro, (self.pos[0]+25,
                         self.pos[1]+self.alto-10, 5, 10))

        # Cuerpo
        pygame.draw.circle(surface, azul_noche, (self.pos[0]+20, self.pos[1]+19),
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
        pygame.draw.ellipse(surface, azul_noche, [self.pos[0]+3,
                            self.pos[1]-10, 34, 20])

        # Cara
        pygame.draw.rect(surface, rosa_claro, [self.pos[0]+10, self.pos[1]-5,
                                               20,10])

        # Ojos
        pygame.draw.rect(surface, negro, [self.pos[0]+14, self.pos[1]-3,
                                          2,6])
        pygame.draw.rect(surface, negro, [self.pos[0]+24, self.pos[1]-3,
                                          2,6])
        

