# -*- coding: utf-8 -*-
# Clase Fondo: crea el fondo del escenario

from OpenGL.GL import *

class Fondo:
    def __init__(self,x0,y0,xf,yf,color):
        self.x0 = x0
        self.yo = y0
        self.xf = xf
        self.yf = yf
        self.color = color

    def dibujar(self):
        glBegin(GL_QUADS)
        # Color en RGB -> pasar a porcentaje (entre 0.0 y 1.0)
        color = self.color
        glColor3f(color[0],color[1],color[2])
        glVertex2f(self.x0,self.yo)
        glVertex2f(self.xf,self.yo)
        glVertex2f(self.xf,self.yf)
        glVertex2f(self.x0,self.yf)
        glEnd()

