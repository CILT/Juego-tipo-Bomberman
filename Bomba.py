# -*- coding: utf-8 -*-
# Clase Bomba

import math
from OpenGL.GL import *
from Cuadricula import *
from Explosion import *

class Bomba(Cuadricula):

    def __init__(self, pos, tamano):
        self.tiempoVida = 0
        self.recienPuesta = True # Evita Bomberman se pegue en bomba
        Cuadricula.__init__(self, pos, tamano)

    def explotar(self):
        self.destruir() # Deja vida en 0

    def dibujar(self):
        # Colores
        negro = (0,0,0)
        azul_noche_perlado = (16/255.0,44/255.0,84/255.0)
        blanco_senales = (244/255.0,244/255.0,244/255.0)
        pi = math.pi
        cos = math.cos
        sin = math.sin

        # Base
        # Centro Bomba
        xi = self.pos[0] + 20
        yi = self.pos[1] + 25

        # Sombra
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(negro[0],negro[1],negro[2])
        glVertex2f(xi,yi)
        radio = 12
        ang = 2*pi/20
        for i in range(21):
            ang_i = ang*i
            rad_x = radio*cos(ang_i)
            rad_y = radio*sin(ang_i)
            glVertex2f(xi -3 + rad_x, yi - 3 + rad_y)
        glEnd()
        
        # Cuerpo
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(azul_noche_perlado[0],azul_noche_perlado[1],azul_noche_perlado[2])
        glVertex2f(xi,yi)
        radio = 12
        ang = 2*pi/20
        for i in range(21):
            ang_i = ang*i
            rad_x = radio*cos(ang_i)
            rad_y = radio*sin(ang_i)
            glVertex2f(xi + rad_x, yi + rad_y)
        glEnd()

        # Luz
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(blanco_senales[0],blanco_senales[1],blanco_senales[2])
        xc = xi + 6
        yc = yi + 6
        glVertex2f(xc, yc)
        radio = 4
        ang = 2*pi/20
        for i in range(21):
            ang_i = ang*i
            rad_x = radio*cos(ang_i)
            rad_y = radio*sin(ang_i)
            glVertex2f(xc + rad_x, yc + rad_y)
        glEnd()
        
        

