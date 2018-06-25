# -*- coding: utf-8 -*-
# Clase Muro_destruible

from OpenGL.GL import *
from Cuadricula import *

import os

class Muro_destruible(Cuadricula):
    
    def __init__(self, pos, tamano):
        Cuadricula.__init__(self, pos, tamano)


    def dibujar(self):
        gris = (128/255.0,128/255.0,128/255.0)
        gris_oscuro = (64/255.0, 64/255.0, 64/255.0)
        
        # rect(Surface, color, (x,y,width,height), thickness)
        # line(Surface, color, start_pos, end_pos, width=1)

        x0 = self.pos[0]
        y0 = self.pos[1]
        # Cuadrado base
        glBegin(GL_QUADS)
        glColor3f(gris[0],gris[1],gris[2])
        glVertex2f(x0,y0)
        glVertex2f(x0+self.ancho,y0)
        glVertex2f(x0+self.ancho,y0+self.alto)
        glVertex2f(x0,y0+self.alto)
        glEnd()

        # Líneas tipo ladrillo
        glLineWidth(2)
        glBegin(GL_LINES)
        glColor3f(gris_oscuro[0],gris_oscuro[1],gris_oscuro[2])

        # Horizontales
        glVertex2f(x0, y0 + int(self.alto / 3.0))
        glVertex2f(x0 + self.ancho, y0 + int(self.alto / 3.0))
        
        glVertex2f(x0, y0 + 2*int(self.alto / 3.0))
        glVertex2f(x0 + self.ancho, y0 + 2*int(self.alto / 3.0))

        # Verticales
        glVertex2f(x0 + int(self.ancho/3.0), y0)
        glVertex2f(x0 + int(self.ancho/3.0), y0 + int(self.alto/3.0))

        glVertex2f(x0 + int(self.ancho/3.0), y0 + 2*int(self.alto/3.0))
        glVertex2f(x0 + int(self.ancho/3.0), y0 + self.alto)

        glVertex2f(x0 + 2*int(self.ancho/3.0), y0 + int(self.alto/3.0))
        glVertex2f(x0 + 2*int(self.ancho/3.0), y0 + 2*int(self.alto/3.0))
        
        glEnd()
        glLineWidth(1)

        
