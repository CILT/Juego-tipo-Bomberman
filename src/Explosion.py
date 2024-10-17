# -*- coding: utf-8 -*-
# Clase Explosion
# Sirve para cuando la bomba explota

from OpenGL.GL import *
import math
import numpy as np
from Cuadricula import *

class Explosion(Cuadricula):

    def __init__(self, pos, tamano, tipo):
        self.tiempoVida = 0
        self.tipo = tipo
        Cuadricula.__init__(self, pos, tamano)

    # dibujar: Explosion Surface String -> None
    def dibujar(self):
        tipo = self.tipo
        # Colores
        amarillo_brillante = (1.0,1.0,0.0)
        naranja_puro = (1.0,117/255.0,20/255.0)
        # Constantes
        x0 = self.pos[0]
        y0 = self.pos[1]
        anchoFuego = 5
        if tipo == 'en_mitad_hor':
            glBegin(GL_QUADS)
            # Cuerpo
            glColor3f(amarillo_brillante[0],amarillo_brillante[1],amarillo_brillante[2])
            glVertex2f(x0, y0)
            glVertex2f(x0, y0 + self.alto)
            glVertex2f(x0 + self.ancho, y0 + self.alto)
            glVertex2f(x0 + self.ancho, y0)

            # Fuego Abajo
            glColor3f(naranja_puro[0],naranja_puro[1],naranja_puro[2])
            glVertex2f(x0, y0)
            glVertex2f(x0, y0 + anchoFuego)
            glVertex2f(x0 + self.ancho, y0 + anchoFuego)
            glVertex2f(x0 + self.ancho, y0)
            
            # Fuego Arriba
            glVertex2f(x0, y0 + self.alto - anchoFuego)
            glVertex2f(x0, y0 + self.alto)
            glVertex2f(x0 + self.ancho, y0 + self.alto)
            glVertex2f(x0 + self.ancho, y0 + self.alto - anchoFuego)
            glEnd()
            
        elif tipo == 'en_mitad_vert':
            glBegin(GL_QUADS)
            # Cuerpo
            glColor3f(amarillo_brillante[0],amarillo_brillante[1],amarillo_brillante[2])
            glVertex2f(x0, y0)
            glVertex2f(x0, y0 + self.alto)
            glVertex2f(x0 + self.ancho, y0 + self.alto)
            glVertex2f(x0 + self.ancho, y0)

            # Fuego Derecha
            glColor3f(naranja_puro[0],naranja_puro[1],naranja_puro[2])
            glVertex2f(x0 + self.ancho - anchoFuego, y0)
            glVertex2f(x0 + self.ancho - anchoFuego, y0 + self.alto)
            glVertex2f(x0 + self.ancho, y0 + self.alto)
            glVertex2f(x0 + self.ancho, y0)
            
            # Fuego Izquierda
            glVertex2f(x0, y0)
            glVertex2f(x0, y0 + self.alto)
            glVertex2f(x0 + anchoFuego, y0 + self.alto)
            glVertex2f(x0 + anchoFuego, y0)
            glEnd()

        elif tipo == 'centro':
            glBegin(GL_QUADS)
            # Cuerpo
            glColor3f(amarillo_brillante[0],amarillo_brillante[1],amarillo_brillante[2])
            glVertex2f(x0, y0)
            glVertex2f(x0, y0 + self.alto)
            glVertex2f(x0 + self.ancho, y0 + self.alto)
            glVertex2f(x0 + self.ancho, y0)
            glEnd()
            
        elif tipo == 'punta_arr':
            # Parte gruesa
            glBegin(GL_QUADS)
            glColor3f(naranja_puro[0],naranja_puro[1],naranja_puro[2])
            glVertex2f(x0, y0 + int(self.alto/2.0))
            glVertex2f(x0 + self.ancho, y0 + int(self.alto/2.0))
            glVertex2f(x0 + self.ancho, y0 + self.alto)
            glVertex2f(x0, y0 + self.alto)
            glEnd()

            # Punta
            glBegin(GL_TRIANGLES)
            glVertex2f(x0, y0 + int(self.alto/2.0))
            glVertex2f(x0 + self.ancho, y0 + int(self.alto/2.0))
            glVertex2f(x0 + int(self.ancho/2.0), y0)
            glEnd()
            
        elif tipo == 'punta_abajo':
            # Parte gruesa
            glBegin(GL_QUADS)
            glColor3f(naranja_puro[0],naranja_puro[1],naranja_puro[2])
            glVertex2f(x0, y0)
            glVertex2f(x0 + self.ancho, y0)
            glVertex2f(x0 + self.ancho, y0 + int(self.alto/2.0))
            glVertex2f(x0, y0 + int(self.alto/2.0))
            glEnd()

            # Punta
            glBegin(GL_TRIANGLES)
            glVertex2f(x0, y0 + int(self.alto/2.0))
            glVertex2f(x0 + self.ancho, y0 + int(self.alto/2.0))
            glVertex2f(x0 + int(self.ancho/2.0), y0 + self.alto)
            glEnd()
            
        elif tipo == 'punta_izq':
            # Parte gruesa
            glBegin(GL_QUADS)
            glColor3f(naranja_puro[0],naranja_puro[1],naranja_puro[2])
            glVertex2f(x0 + int(self.ancho/2.0), y0)
            glVertex2f(x0 + int(self.ancho/2.0), y0 + self.alto)
            glVertex2f(x0 + self.ancho, y0 + self.ancho)
            glVertex2f(x0 + self.ancho, y0)
            glEnd()

            # Punta
            glBegin(GL_TRIANGLES)
            glVertex2f(x0 + int(self.ancho/2.0), y0)
            glVertex2f(x0, y0 + int(self.alto/2.0))
            glVertex2f(x0 + int(self.ancho/2.0), y0 + self.alto)
            glEnd()
            
        elif tipo == 'punta_der':
            # Parte gruesa
            glBegin(GL_QUADS)
            glColor3f(naranja_puro[0],naranja_puro[1],naranja_puro[2])
            glVertex2f(x0 + int(self.ancho/2.0), y0)
            glVertex2f(x0 + int(self.ancho/2.0), y0 + self.alto)
            glVertex2f(x0, y0 + self.ancho)
            glVertex2f(x0, y0)
            glEnd()

            # Punta
            glBegin(GL_TRIANGLES)
            glVertex2f(x0 + int(self.ancho/2.0), y0)
            glVertex2f(x0 + self.ancho, y0 + int(self.alto/2.0))
            glVertex2f(x0 + int(self.ancho/2.0), y0 + self.alto)
            glEnd()
        
            
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

            
