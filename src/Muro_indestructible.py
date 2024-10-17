# -*- coding: utf-8 -*-
# Clase Muro_indestructible

from OpenGL.GL import *
from Cuadricula import *

class Muro_indestructible(Cuadricula):
    
    def __init__(self, pos, tamano):
        Cuadricula.__init__(self,pos,tamano)

    def dibujar(self):
        gris_mas_claro = (225/255.0,225/255.0,225/255.0)
        gris_luminoso = (215/255.0,215/255.0,215/255.0) # Luminosidad
        gris_piedra = (139/255.0,140/255.0,122/255.0) # Base
        gris_negruzco = (35/255.0,40/255.0,43/255.0) # Sombra
        
        x0 = self.pos[0]
        y0 = self.pos[1]
        xf = x0 + self.ancho
        yf = y0 + self.alto
        
        # Cuadrado base
        glBegin(GL_QUADS)
        glColor3f(gris_piedra[0],gris_piedra[1],gris_piedra[2])
        glVertex2f(x0,y0)
        glVertex2f(xf,y0)
        glVertex2f(xf,yf)
        glVertex2f(x0,yf)
        glEnd()

        # Sombras
        # Sombra lateral
        glBegin(GL_QUADS)
        glColor3f(gris_negruzco[0],gris_negruzco[1],gris_negruzco[2])
        glVertex2f(x0,y0)
        glVertex2f(x0+5,y0)
        glVertex2f(x0+5,yf)
        glVertex2f(x0,yf)
        glEnd()

        # Sombra de abajo
        glBegin(GL_QUADS)
        glColor3f(gris_negruzco[0],gris_negruzco[1],gris_negruzco[2])
        glVertex2f(x0,y0)
        glVertex2f(x0,y0+4)
        glVertex2f(xf,y0+4)
        glVertex2f(xf,y0)
        glEnd()

        # Luminosidad
        # Luminosidad superior
        glBegin(GL_QUADS)
        glColor3f(gris_luminoso[0],gris_luminoso[1],gris_luminoso[2])
        glVertex2f(x0+5,yf)
        glVertex2f(xf,yf)
        glVertex2f(xf,yf-5)
        glVertex2f(x0+5,yf-5)
        glEnd()

        # Luminosidad lateral
        glBegin(GL_QUADS)
        glColor3f(gris_luminoso[0],gris_luminoso[1],gris_luminoso[2])
        glVertex2f(xf-5,y0+4)
        glVertex2f(xf-5,yf)
        glVertex2f(xf,yf)
        glVertex2f(xf,y0+4)
        glEnd()
