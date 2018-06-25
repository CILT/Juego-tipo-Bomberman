# -*- coding: utf-8 -*-
# Clase Vista. Se encarga de la vista del juego

import pygame
from pygame.locals import *
from OpenGL.GL import *

class Vista:
    def __init__(self, FPS, titulo, display_w, display_h, reloj):
        self.FPS = FPS
        self.titulo = titulo
        self.width = display_w
        self.height = display_h
        self.reloj = reloj
        self.load_music()

    def dibujar(self,escenario):
        FPS = self.FPS
        titulo = self.titulo
        # Título
        pygame.display.set_caption(titulo + ' (FPS = {0})'.format(int(self.reloj.get_fps())))

        # Se dibuja el escenario
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.reloj.tick(FPS) # Ajusta a FPS
        escenario.dibujar()
        pygame.display.flip() # vuelca el dibujo en pantalla

    def load_music(self):
        """Load the music"""
        song1 = 'Hunting_High_and_Low_8_bit.ogg'
        pygame.mixer.music.load(song1)
        pygame.mixer.music.play(-1,0.0) # Repetición indefinida
##        pygame.mixer.music.set_volume()
