# -*- coding: utf-8 -*-
# Clase Vista. Se encarga de la vista del juego

import pygame
from pygame.locals import *

class Vista:
    def __init__(self, surface, reloj, FPS, titulo, colorFondo=(0,0,0)):
        self.surface = surface
        self.reloj = reloj
        self.FPS = FPS
        self.titulo = titulo
        self.colorFondo = colorFondo

    def dibujar(self,escenario):
        FPS = self.FPS
        titulo = self.titulo
        reloj = self.reloj
        # Nuevo cuadro
        reloj.tick(FPS)
        # Título
        pygame.display.set_caption(titulo + ' (FPS={0})'.format(int(reloj.get_fps())))
        self.surface.fill(self.colorFondo)
        escenario.dibujar(self.surface)
        pygame.display.flip() # vuelca el dibujo en pantalla
        if escenario.bomberman.estaMuerto():
            self.gameOver(escenario)
        
    def gameOver(self, escenario):
##        self.message_display('GAME OVER', escenario)
        pygame.quit()
        quit()

    def message_display(self, text, escenario):
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = self.text_objects(text, 115)
        TextRect.center = (15*escenario.tamCuadr/2, 13*escenario.tamCuadr/2)
        self.surface.blit(TextSurf, TextRect)
        time.sleep(2)


    def text_objects(self, text, font):
        textSurface = font.render(text, True, [0,0,0])
        return textSurface, textSurface.get_rect()

    def load_music(self):
        """Load the music"""
        song1 = 'Hunting_High_and_Low_8_bit.ogg'
        pygame.mixer.music.load(song1)
        pygame.mixer.music.play(-1)
