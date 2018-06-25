# -*- coding: utf-8 -*-
# Enemigos de bomberman

from OpenGL.GL import *
from math import *
from Cuadricula import *

class Enemigo(Cuadricula):

    def __init__(self, pos, tamano, tipo):
        self.tipo = tipo
        Cuadricula.__init__(self, pos, tamano)

    def dibujar(self):
        if self.tipo == 1:
            self.dibujar_1()
        elif self.tipo == 2:
            self.dibujar_2()
        else:
            print "Enemigo no implementado"

    def dibujar_1(self):
        # Colores
        negro = (0,0,0)
        azul_noche = (37/255.0,40/255.0,80/255.0)
        rosa_claro = (234/255.0,137/255.0,154/255.0)
        rojo_pardo = (120/255.0,31/255.0,25/255.0)
        azul_celeste = (34/255.0, 113/255.0, 179/255.0)
        blanco_perla = (234/255.0,230/255.0,202/255.0)
        blanco_trafico = (246/255.0,246/255.0,246/255.0)
        aluminio_gris = (143/255.0,143/255.0,143/255.0)
        aluminio_blanco = (165/255.0,165/255.0,165/255.0)

        # Constantes
        x0 = self.pos[0]
        y0 = self.pos[1]

        # Piernas
        glBegin(GL_QUADS)
        glColor3f(blanco_trafico[0],blanco_trafico[1],blanco_trafico[2])
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
        glColor3f(negro[0],negro[1],negro[2])
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
        # Izquierdo
        glVertex2f(x0 + 14, y0 + self.alto + 3)
        glVertex2f(x0 + 16, y0 + self.alto + 3)
        glVertex2f(x0 + 16, y0 + self.alto - 3)
        glVertex2f(x0 + 14, y0 + self.alto - 3)
        # Derecho
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

        # Calavera
        self.dibujarCalavera()

        # Espada
        xi = x0 + self.ancho - 3
        yi = y0 + self.alto - 21
        # Mango
        glLineWidth(2)
        glBegin(GL_LINES)
        glColor3f(negro[0],negro[1],negro[2])
        glVertex2f(xi, yi)
        glVertex2f(xi + 2, yi + 8)
        glEnd()

        glLineWidth(2)
        glBegin(GL_LINES)
        glVertex2f(xi - 1, yi + 9)
        glVertex2f(xi + 4, yi + 7)
        glEnd()

        # Filo
        glLineWidth(3)
        glBegin(GL_LINES)
        glColor3f(aluminio_blanco[0],aluminio_blanco[1],aluminio_blanco[2])
        glVertex2f(xi + 2, yi + 8)
        glVertex2f(xi + 5, yi + 20)
        glEnd()
        glLineWidth(1) # Lo vuelve a poner en 1
        

    def dibujar_2(self):
        # Colores
        negro = (0,0,0)
        azul_noche = (37/255.0,40/255.0,80/255.0)
        rosa_claro = (234/255.0,137/255.0,154/255.0)
        rojo_pardo = (120/255.0,31/255.0,25/255.0)
        azul_celeste = (34/255.0, 113/255.0, 179/255.0)
        blanco_perla = (234/255.0,230/255.0,202/255.0)
        blanco_trafico = (246/255.0,246/255.0,246/255.0)
        pardo_rojo = (89/255.0,35/255.0,33/255.0)

        x0 = self.pos[0]
        y0 = self.pos[1]

        # Piernas
        glBegin(GL_QUADS)
        glColor3f(azul_noche[0],azul_noche[1],azul_noche[2])
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
        glColor3f(pardo_rojo[0],pardo_rojo[1],pardo_rojo[2])
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
        glVertex2f(x0 + 24, y0 + self.alto + 3)
        glVertex2f(x0 + 26, y0 + self.alto + 3)
        glVertex2f(x0 + 26, y0 + self.alto - 3)
        glVertex2f(x0 + 24, y0 + self.alto - 3)
        glEnd()
        # Izquierdo: Parche
        # Tiras
        glBegin(GL_LINES)
        glVertex2f(x0 + 15, y0 + self.alto + 8)
        glVertex2f(x0 + 15, y0 + self.alto)
        
        glVertex2f(x0 + 3, y0 + self.alto)
        glVertex2f(x0 + 15, y0 + self.alto)
        glEnd()
        # Tapa-ojo
        centro = [x0 + 15, y0 + self.alto]
        self.drawEllipse(centro, 4, 4)

        # Pies
        glColor3f(negro[0],negro[1],negro[2])
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
        glColor3f(azul_noche[0],azul_noche[1],azul_noche[2])
        # Derecho
        centro = [x0 + self.ancho -3, y0 + self.alto - 21]
        self.drawEllipse(centro, 3, 3)
        # Izquierdo
        centro = [x0 + 3, y0 + self.alto - 21]
        self.drawEllipse(centro, 3, 3)

        # Calavera
        self.dibujarCalavera()
        
        
    def dibujarCalavera(self):
        # Colores
        negro = (0,0,0)
        azul_noche = (37/255.0,40/255.0,80/255.0)
        rosa_claro = (234/255.0,137/255.0,154/255.0)
        rojo_pardo = (120/255.0,31/255.0,25/255.0)
        azul_celeste = (34/255.0, 113/255.0, 179/255.0)
        blanco_perla = (234/255.0,230/255.0,202/255.0)
        blanco_trafico = (246/255.0,246/255.0,246/255.0)
        aluminio_gris = (143/255.0,143/255.0,143/255.0)
        aluminio_blanco = (165/255.0,165/255.0,165/255.0)
        
        # Calavera
        x0, y0 = self.pos[0], self.pos[1]
        xi, yi = x0 + 10, y0 + self.alto - 10

        # Maxilar
        glColor3f(blanco_perla[0], blanco_perla[1], blanco_perla[2])
        glBegin(GL_QUADS)
        glVertex2f(xi + 7, yi - 9)
        glVertex2f(xi + 7 + 6, yi - 9)
        glVertex2f(xi + 7 + 6, yi - 9 - 3)
        glVertex2f(xi + 7, yi - 9 - 3)
        glEnd()

        # Mandíbula
        glBegin(GL_QUADS)
        glVertex2f(xi + 7, yi - 14)
        glVertex2f(xi + 7 + 6, yi - 14)
        glVertex2f(xi + 7 + 6, yi - 14 - 3)
        glVertex2f(xi + 7, yi - 14 - 3)
        glEnd()

        # Dientes
        glColor3f(negro[0],negro[1],negro[2])
        glBegin(GL_LINES)
        glVertex2f(xi + 9, yi - 9)
        glVertex2f(xi + 9, yi - 12)

        glVertex2f(xi + 11, yi - 9)
        glVertex2f(xi + 11, yi - 12)

        glVertex2f(xi + 9, yi - 14)
        glVertex2f(xi + 9, yi - 17)

        glVertex2f(xi + 11, yi - 14)
        glVertex2f(xi + 11, yi - 17)
        glEnd()
        
        # Cabeza
        glColor3f(blanco_trafico[0],blanco_trafico[1],blanco_trafico[2])
        centro = [xi + 10, yi - 7]
        self.drawEllipse(centro, 8, 5)

        # Ojos
        glColor3f(negro[0],negro[1],negro[2])
        # Izquierdo
        centro = [xi + 8, yi - 6]
        self.drawEllipse(centro, 2, 2)
        # Derecho
        centro = [xi + 12, yi - 6]
        self.drawEllipse(centro, 2, 2)


    # Para dibujar ellipses de forma más cómoda
    def drawEllipse(self, center, radiusX, radiusY):
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(center[0],center[1])
        ang = 2*pi/20
        for i in range(21):
            ang_i = ang*i
            glVertex2f(center[0] + radiusX*cos(ang_i), center[1] + radiusY*sin(ang_i))
        glEnd()
        
