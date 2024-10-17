# -*- coding: utf-8 -*-
# Controlador

import pygame
from pygame.locals import *

class Controlador:

    def __init__(self, escenario):
        self.escenario = escenario

    def controlar(self, run, DT):
        escenario = self.escenario
        # Término del juego
        if escenario.bomberman.estaMuerto():
            run = False
            
        # Manejo de eventos del teclado, mouse, etc.
        events = pygame.event.get()
        
        for event in events:
            if event.type == QUIT:
                run = False
                
            if event.type == KEYDOWN:
                if event.key == K_q:
                    run = False

                if event.key == K_a:
                    bomba = escenario.bomberman.ponerBomba()
                    escenario.bombas.append(bomba)

                if event.key == K_LEFT:
                    escenario.bomberman.moverIzq(1)
                    if escenario.chocaConMuro(escenario.bomberman):
                        escenario.bomberman.moverDer(1)
                if event.key == K_RIGHT:
                    escenario.bomberman.moverDer(1)
                    if escenario.chocaConMuro(escenario.bomberman):
                        escenario.bomberman.moverIzq(1)
                if event.key == K_UP:
                    escenario.bomberman.subir(1)
                    if escenario.chocaConMuro(escenario.bomberman):
                        escenario.bomberman.bajar(1)
                if event.key == K_DOWN:
                    escenario.bomberman.bajar(1)
                    if escenario.chocaConMuro(escenario.bomberman):
                        escenario.bomberman.subir(1)

        # Para tecla mantenida apretada
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[K_LEFT]:
            escenario.bomberman.moverIzq(escenario.bomberman.vel)
            if escenario.chocaConMuro(escenario.bomberman) or escenario.chocaConBomba(escenario.bomberman):
                escenario.bomberman.moverDer(escenario.bomberman.vel) # Retrocede el avance si choca con muro
                
        if keys_pressed[K_RIGHT]:
            escenario.bomberman.moverDer(escenario.bomberman.vel)
            if escenario.chocaConMuro(escenario.bomberman) or escenario.chocaConBomba(escenario.bomberman):
                escenario.bomberman.moverIzq(escenario.bomberman.vel)
                
        if keys_pressed[K_DOWN]:
            escenario.bomberman.bajar(escenario.bomberman.vel)
            if escenario.chocaConMuro(escenario.bomberman) or escenario.chocaConBomba(escenario.bomberman):
                escenario.bomberman.subir(escenario.bomberman.vel)
                
        if keys_pressed[K_UP]:
            escenario.bomberman.subir(escenario.bomberman.vel)
            if escenario.chocaConMuro(escenario.bomberman) or escenario.chocaConBomba(escenario.bomberman):
                escenario.bomberman.bajar(escenario.bomberman.vel)

        escenario.actualizarBombas(DT) # Revisa las bombas
        escenario.actualizarExplosiones(DT) # Actualiza las Exlosiones
        escenario.actualizarEnemigos() # Revisa si les llegó explosión
        escenario.actualizarBomberman() # Revisa la interacción de Bomberman
        escenario.actualizarMuros()
        escenario.limpiar() # Saca todos los que murieron este ciclo

        return run


    def message_display(self, text, escenario):
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = self.text_objects(text, 115)
        TextRect.center = (15*escenario.tamCuadr/2, 13*escenario.tamCuadr/2)
        self.surface.blit(TextSurf, TextRect)
        time.sleep(2)


    def text_objects(self, text, font):
        textSurface = font.render(text, True, [0,0,0])
        return textSurface, textSurface.get_rect()


            
