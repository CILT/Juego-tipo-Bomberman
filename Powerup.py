# -*- coding: utf-8 -*-
# Implementación de Pwer-Ups

from OpenGL.GL import *
from math import *
from Cuadricula import *

class Powerup(Cuadricula):

    def __init__(self, pos, tamano, tipo):
        self.tipo = tipo
        Cuadricula.__init__(self, pos, tamano)

    def dibujar(self):
        if self.tipo == 'velocidad':
            self.dibujar_vel()
        elif self.tipo == 'explosion':
            self.dibujar_expl()
        elif self.tipo == 'salida':
            self.dibujar_sal()
        else:
            print 'Power-Up aún no implementado'


    def dibujar_vel(self):
        # Colores
        azul_pastel = (93/255.0,155/255.0,155/255.0)
        verde_hoja = (45/255.0,87/255.0,44/255.0)
        amarillo_de_zinc = (248/255.0,243/255.0,53/255.0)
        amarillo_senales = (229/255.0,190/255.0,1/255.0)

        # Constantes
        x0 = self.pos[0]
        y0 = self.pos[1]
        
        # Fondo
        glColor3f(azul_pastel[0],azul_pastel[1],azul_pastel[2])
        glBegin(GL_QUADS)
        glVertex2f(x0, y0)
        glVertex2f(x0, y0 + self.alto)
        glVertex2f(x0 + self.ancho, y0 + self.alto)
        glVertex2f(x0 + self.ancho, y0)
        glEnd()
        
        # Punta del pie
        glColor3f(amarillo_de_zinc[0],amarillo_de_zinc[1],amarillo_de_zinc[2])
        centro = [x0 + 15, y0 + int(25/2.0)]
        self.drawEllipse(centro, 10, 5)
        
        # Pie
        glColor3f(verde_hoja[0],verde_hoja[1],verde_hoja[2])
        glBegin(GL_QUADS)
        glVertex2f(x0 + 25, y0 + self.alto - 5)
        glVertex2f(x0 + 25, y0 + self.alto - 35)
        glVertex2f(x0 + 35, y0 + self.alto - 35)
        glVertex2f(x0 + 35, y0 + self.alto - 5)

        glVertex2f(x0 + 15, y0 + self.alto - 25)
        glVertex2f(x0 + 15, y0 + self.alto - 35)
        glVertex2f(x0 + 25, y0 + self.alto - 35)
        glVertex2f(x0 + 25, y0 + self.alto - 25)
        glEnd()

        # Ruedas
        glColor3f(amarillo_senales[0],amarillo_senales[1],amarillo_senales[2])
        centro = [x0 + 15, y0 + self.alto - 36]
        self.drawEllipse(centro, 4, 4)

        centro = [x0 + 30, y0 + self.alto - 36]
        self.drawEllipse(centro, 4, 4)

    def dibujar_expl(self):
        # Colores
        azul_noche_perlado = (16/255.0,44/255.0,84/255.0)
        gris_plata = (138/255.0,149/255.0,151/255.0)

        # Constantes
        x0 = self.pos[0]
        y0 = self.pos[1]

        # Fondo
        glColor3f(azul_noche_perlado[0],azul_noche_perlado[1],azul_noche_perlado[2])
        glBegin(GL_QUADS)
        glVertex2f(x0, y0)
        glVertex2f(x0, y0 + self.alto)
        glVertex2f(x0 + self.ancho, y0 + self.alto)
        glVertex2f(x0 + self.ancho, y0)
        glEnd()

        # Marco
        glColor3f(gris_plata[0],gris_plata[1],gris_plata[2])
        glLineWidth(2)
        glBegin(GL_LINES)
        # abajo
        glVertex2f(x0, y0)
        glVertex2f(x0 + self.ancho, y0)

        # arriba
        glVertex2f(x0, y0 + self.alto)
        glVertex2f(x0 + self.ancho, y0 + self.alto)

        # izquierda
        glVertex2f(x0, y0)
        glVertex2f(x0, y0 + self.alto)

        # derecha
        glVertex2f(x0 + self.ancho, y0)
        glVertex2f(x0 + self.ancho, y0 + self.alto)
        glEnd()

        # Rayo
        glLineWidth(1)
        glBegin(GL_LINES)
        glVertex2f(x0 + self.ancho, y0 + self.alto)
        glVertex2f(x0 + 6, y0 + 6)

        glVertex2f(x0 + 30, y0 + self.alto - 10)
        glVertex2f(x0 + 20, y0 + 7)

        glVertex2f(x0 + 20, y0 + self.alto - 7)
        glVertex2f(x0 + 10, y0 + self.alto - 3)
        
        glVertex2f(x0 + 20, y0 + self.alto - 7)
        glVertex2f(x0 + 12, y0 + self.alto - 10)

        glVertex2f(x0 + 12, y0 + self.alto - 10)
        glVertex2f(x0 + 5, y0 + self.alto - 13)

        glVertex2f(x0 + 12, y0 + self.alto - 10)
        glVertex2f(x0 + 5, y0 + self.alto - 25)

        glVertex2f(x0 + 20, y0 + self.alto - 20)
        glVertex2f(x0 + 10, y0 + self.alto - 23)

        glVertex2f(x0 + 30, y0 + self.alto - 10)
        glVertex2f(x0 + 25, y0 + self.alto - 25)

        glVertex2f(x0 + 25, y0 + self.alto - 25)
        glVertex2f(x0 + 20, y0 + self.alto - 35)

        glVertex2f(x0 + 25, y0 + self.alto - 25)
        glVertex2f(x0 + 30, y0 + self.alto - 35)
        glEnd()


    def dibujar_sal(self):
        # Colores
        azul_luminoso = (59/255.0,131/255.0,189/255.0)

        # Constantes
        x0 = self.pos[0]
        y0 = self.pos[1]

        # Forma
        glColor3f(azul_luminoso[0], azul_luminoso[1], azul_luminoso[2])
        glBegin(GL_QUADS)
        glVertex2f(x0, y0)
        glVertex2f(x0 + self.ancho, y0)
        glVertex2f(x0 + self.ancho, y0 + self.ancho)
        glVertex2f(x0, y0 + self.ancho)
        glEnd()

    # Para dibujar ellipses de forma más cómoda
    def drawEllipse(self, center, radiusX, radiusY):
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(center[0],center[1])
        ang = 2*pi/20
        for i in range(21):
            ang_i = ang*i
            glVertex2f(center[0] + radiusX*cos(ang_i), center[1] + radiusY*sin(ang_i))
        glEnd()

        
