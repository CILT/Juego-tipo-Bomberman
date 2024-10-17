# -*- coding: utf-8 -*-
# Clase Explosion
# Sirve para cuando la bomba explota

import pygame
from pygame.locals import *
from Cuadricula import *

class Explosion(Cuadricula):

    def __init__(self, pos, tamano, tipo):
        self.tiempoVida = 0
        self.rect = pygame.Rect(pos[0], pos[1], tamano, tamano)
        if tipo == 'en_mitad_hor':
            self.img = pygame.image.load('Sprites-Explosiones/En_mitad_horizontal.png')
        elif tipo == 'en_mitad_vert':
            self.img = pygame.image.load('Sprites-Explosiones/En_mitad_vertical.png')
        elif tipo == 'centro':
            self.img = pygame.image.load('Sprites-Explosiones/Centro.png')
        elif tipo == 'punta_arr':
            self.img = pygame.image.load('Sprites-Explosiones/Punta_arriba.png')
        elif tipo == 'punta_abajo':
            self.img = pygame.image.load('Sprites-Explosiones/Punta_abajo.png')
        elif tipo == 'punta_izq':
            self.img = pygame.image.load('Sprites-Explosiones/Punta_izquierda.png')
        elif tipo == 'punta_der':
            self.img = pygame.image.load('Sprites-Explosiones/Punta_derecha.png')
        self.img = pygame.transform.scale(self.img, [tamano, tamano])
        Cuadricula.__init__(self, pos, tamano)

    # dibujar: Explosion Surface String -> None
    def dibujar(self, surface):
        # Sprite de la explosión
        surface.blit(self.img, self.rect)
            
    # crearExplosiones: Explosion int [Explosion] Escenario -> None
    # Crea la ráfaga de explosiones que rodean al sitio donde explotó
    # la bomba
    # "Cantidad" es la cantidad de cuadros que se expande
    def crearExplosiones(self, cantidad, listaExpl, escenario):
        cuadricula = self.ancho
        
        # Direccionadas:
        # Hacia arriba
        for i in range(1,cantidad+1): # Se asume cantidad mínima como 2
            if i == cantidad: # Es la punta
                exp_arr = Explosion([self.pos[0], self.pos[1] - cantidad*cuadricula],
                                    self.ancho, 'punta_arr')
            else:
                exp_arr = Explosion([self.pos[0], self.pos[1] - i*cuadricula],
                                    self.ancho, 'en_mitad_vert')

            # Se revisa si la explosión choca con un muro indestructible
            if self.checkChoqueMuroInd(exp_arr, escenario): # Chocó, no se dibuja
                break
            
            listaExpl.append(exp_arr)

            # Se reivsa si la explosión chocó con un muro destruible
            if self.checkChoqueMuroDes(exp_arr, escenario): # Es el último en aparecer
                break
            
        # Hacia Abajo
        for i in range(1,cantidad+1):
            if i == cantidad: # Es la punta
                exp_abajo = Explosion([self.pos[0], self.pos[1] + cantidad*cuadricula],
                                      self.ancho, 'punta_abajo')
            else:
                exp_abajo = Explosion([self.pos[0], self.pos[1] + i*cuadricula],
                                      self.ancho, 'en_mitad_vert')

            # Se revisa si la explosión choca con un muro indestructible
            if self.checkChoqueMuroInd(exp_abajo, escenario): # Chocó, no se dibuja
                break
            
            listaExpl.append(exp_abajo)

            # Se reivsa si la explosión chocó con un muro destruible
            if self.checkChoqueMuroDes(exp_abajo, escenario): # Es el último en aparecer
                break

        # Hacia el lado Izq
        for i in range(1,cantidad+1):
            if i == cantidad: # Es la punta
                exp_izq = Explosion([self.pos[0] - cantidad*cuadricula, self.pos[1]],
                                    self.ancho, 'punta_izq')
            else:
                exp_izq = Explosion([self.pos[0] - i*cuadricula, self.pos[1]],
                                    self.ancho, 'en_mitad_hor')

            # Se revisa si la explosión choca con un muro indestructible
            if self.checkChoqueMuroInd(exp_izq, escenario): # Chocó, no se dibuja
                break
            
            listaExpl.append(exp_izq)

            # Se reivsa si la explosión chocó con un muro destruible
            if self.checkChoqueMuroDes(exp_izq, escenario): # Es el último en aparecer
                break
            
        # Hacia el lado Der
        for i in range(1,cantidad+1):
            if i == cantidad: # Es la punta
                exp_der = Explosion([self.pos[0] + cantidad*cuadricula, self.pos[1]],
                                    self.ancho, 'punta_der')
            else:
                exp_der = Explosion([self.pos[0] + i*cuadricula, self.pos[1]],
                                    self.ancho, 'en_mitad_hor')

            # Se revisa si la explosión choca con un muro indestructible
            if self.checkChoqueMuroInd(exp_der, escenario): # Chocó, no se dibuja
                break
            
            listaExpl.append(exp_der)

            # Se reivsa si la explosión chocó con un muro destruible
            if self.checkChoqueMuroDes(exp_der, escenario): # Es el último en aparecer
                break

    # Retorna True si la explosion dada choca con un muro indestructible
    def checkChoqueMuroInd(self, explosion, escenario):
        for muro in escenario.muros_indestructibles:
            if explosion.choca(muro):
                return True
        return False

    # Retorna True si la explosion dada choca con un muro destruible
    def checkChoqueMuroDes(self, explosion, escenario):
        for muro in escenario.muros_destruibles:
            if explosion.choca(muro):
                return True
        return False

            
