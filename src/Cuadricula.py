# -*- coding: utf-8 -*-
# Clase Cuadrícula representa una cuadrícula de la pantalla

import pygame
from pygame.locals import *

class Cuadricula:
    def __init__(self, pos, tamanoCuadricula):
        self.pos = pos #[x,y] 
        self.ancho = tamanoCuadricula
        self.alto = tamanoCuadricula # En pixeles
        self.vida = True

    # choca: Cuadricula Cuadricula -> bool
    # detecta choques entre cuadrículas
    def choca(self,cuadr2):
        if abs(self.pos[0] - cuadr2.pos[0]) < self.ancho and abs(self.pos[1] - cuadr2.pos[1]) < self.alto:
            return True
        return False

    # destruir: self -> None
    # Destruye la cuadrícula
    def destruir(self):
        self.vida = False

    # estaVivo: self -> bool
    # Pregunta si está muerto. True si sí, False si no.
    def estaMuerto(self):
        return not self.vida

    # subir: Cuadrícula -> None
    # Sube una determinada cantidad de pixeles la cuadrícula
    def subir(self, pixeles):
        self.pos[1] += pixeles

    # Baja una determinada cantidad de pixeles la cuadrícula
    def bajar(self, pixeles):
        self.pos[1] -= pixeles
        
    # Mueve hacia la izquierda una determinada cantidad de pixeles la cuadrícula
    def moverIzq(self, pixeles):
        self.pos[0] -= pixeles

    # Mueve hacia la derecha una determinada cantidad de pixeles la cuadrícula
    def moverDer(self, pixeles):
        self.pos[0] += pixeles
        
