# -*- coding: utf-8 -*-
# Jugador Bomberman

from OpenGL.GL import *
from math import *
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

    def dibujar(self):
        # Colores
        negro = (0,0,0)
        azul_noche = (37/255.0,40/255.0,80/255.0)
        rosa_claro = (234/255.0,137/255.0,154/255.0)
        rojo_pardo = (120/255.0,31/255.0,25/255.0)
        azul_celeste = (34/255.0, 113/255.0, 179/255.0)

        # Constantes
        x0 = self.pos[0]
        y0 = self.pos[1]

        # Piernas
        glBegin(GL_QUADS)
        glColor3f(rosa_claro[0],rosa_claro[1],rosa_claro[2])
        glVertex2f(x0 + 10, y0 + 10)
        glVertex2f(x0 + 15, y0 + 10)
        glVertex2f(x0 + 15, y0)
        glVertex2f(x0 + 10, y0)

        glVertex2f(x0 + 25, y0 + 10)
        glVertex2f(x0 + 30, y0 + 10)
        glVertex2f(x0 + 30, y0)
        glVertex2f(x0 + 25, y0)
        glEnd()

        # Cuerpo
        glColor3f(azul_noche[0],azul_noche[1],azul_noche[2])
        # Centro del círculo
        xc, yc = x0 + int(self.ancho/2.0), y0 + self.alto - 19
        self.drawEllipse([xc,yc], 15, 15)

        # Cabeza
        # El color ya está puesto
        xc, yc = x0 + int(self.ancho/2.0), y0 + self.alto
        self.drawEllipse([xc,yc], 17, 10)

        # Cara
        glBegin(GL_QUADS)
        glColor3f(rosa_claro[0],rosa_claro[1],rosa_claro[2])
        glVertex2f(x0 + 10, y0 + self.alto + 5)
        glVertex2f(x0 + 30, y0 + self.alto + 5)
        glVertex2f(x0 + 30, y0 + self.alto - 5)
        glVertex2f(x0 + 10, y0 + self.alto - 5)

        # Ojos
        glColor3f(negro[0],negro[1],negro[2])
        # Derecho
        glVertex2f(x0 + 14, y0 + self.alto + 3)
        glVertex2f(x0 + 16, y0 + self.alto + 3)
        glVertex2f(x0 + 16, y0 + self.alto - 3)
        glVertex2f(x0 + 14, y0 + self.alto - 3)
        # Izquierdo
        glVertex2f(x0 + 24, y0 + self.alto + 3)
        glVertex2f(x0 + 26, y0 + self.alto + 3)
        glVertex2f(x0 + 26, y0 + self.alto - 3)
        glVertex2f(x0 + 24, y0 + self.alto - 3)
        glEnd()

        # Pies
        glColor3f(rojo_pardo[0],rojo_pardo[1],rojo_pardo[2])
        # Izquierdo
        xc, yc = x0 + 12, y0 + 3
        self.drawEllipse([xc,yc], 7, 3)
        # Derecho
        xc, yc = x0 + 27, y0 + 3
        self.drawEllipse([xc,yc], 7, 3)

        # Brazos
        glColor3f(rosa_claro[0],rosa_claro[1],rosa_claro[2])
        glBegin(GL_QUADS)
        glVertex2f(x0 + 34, y0 + self.alto - 10)
        glVertex2f(x0 + 39, y0 + self.alto - 10)
        glVertex2f(x0 + 39, y0 + self.alto - 20)
        glVertex2f(x0 + 34, y0 + self.alto - 20)

        glVertex2f(x0 + 1, y0 + self.alto - 10)
        glVertex2f(x0 + 6, y0 + self.alto - 10)
        glVertex2f(x0 + 6, y0 + self.alto - 20)
        glVertex2f(x0 + 1, y0 + self.alto - 20)
        glEnd()

        # Guantes
        glColor3f(azul_celeste[0],azul_celeste[1],azul_celeste[2])
        # Derecho
        centro = [x0 + self.ancho -3, y0 + self.alto - 21]
        self.drawEllipse(centro, 3, 3)
        # Izquierdo
        centro = [x0 + 3, y0 + self.alto - 21]
        self.drawEllipse(centro, 3, 3)
        

    # Para dibujar ellipses de forma más cómoda
    def drawEllipse(self, center, radiusX, radiusY):
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(center[0],center[1])
        ang = 2*pi/20
        for i in range(21):
            ang_i = ang*i
            glVertex2f(center[0] + radiusX*cos(ang_i), center[1] + radiusY*sin(ang_i))
        glEnd()
        
        

