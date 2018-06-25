# -*- coding: utf-8 -*-
# Clase Escenario. Forma inicializa la ventana y dibuja las cosas

# Importar librerías
import pygame
from pygame.locals import *
import random

# Modelos
from Muro_destruible import *
from Muro_indestructible import *
from Enemigo import *
from Bomberman import *
from Explosion import *
from Powerup import *

class Escenario:

    def __init__(self, tamCuadr, fondo, muros_destruibles=[], muros_indestructibles=[],
                 bomberman=[], enemigos=[], bombas=[], powerups=[], explosiones=[]):
        # Parámetros
        self.tamCuadr = tamCuadr
        self.fondo = fondo
        # Objetos
        self.muros_destruibles = muros_destruibles
        self.muros_indestructibles = muros_indestructibles
        self.bomberman = bomberman
        self.enemigos = enemigos
        self.bombas = bombas
        self.powerups = powerups
        self.explosiones = explosiones
        # Indicadores
        self.salida = False # Detecta si ya hay una salida
        self.cantidadPowerups = 4
        self.cantidadEnemigos = 4
        # Sonidos
        pygame.mixer.init(44100) # Frecuencia
        self.sonido_explosion = pygame.mixer.Sound("8 Bit Explosion 1 SOUND Effect.wav")
        self.sonido_explosion.set_volume(0.5)

    """
    Dibujo y limpieza del escenario
    """
    # limpiar: Escenario -> None
    # Busca qué elementos de la pantalla murieron en la partida y los borra
    def limpiar(self):
        k = 0
        for muro in self.muros_destruibles:
            if muro.estaMuerto():
                self.muros_destruibles.pop(k)
            k += 1
        k = 0
        for enemigo in self.enemigos:
            if enemigo.estaMuerto():
                self.enemigos.pop(k)
            k += 1
        k = 0
        for bomba in self.bombas:
            if bomba.estaMuerto():
                self.bombas.pop(k)
            k += 1
        k = 0
        for powerup in self.powerups:
            if powerup.estaMuerto():
                self.powerups.pop(k)
            k += 1
        k = 0
        for explosion in self.explosiones:
            if explosion.estaMuerto():
                self.explosiones.pop(k)
            k += 1
            

    # Dibuja los elementos
    def dibujar(self):
        # Primero el fondo
        self.fondo.dibujar()
        # Objetos
        for muro in self.muros_destruibles:
            muro.dibujar()
        for muro in self.muros_indestructibles:
            muro.dibujar()
        for bomba in self.bombas:
            bomba.dibujar()
        for powerup in self.powerups:
            powerup.dibujar()
        for explosion in self.explosiones:
            explosion.dibujar()
        for enemigo in self.enemigos:
            enemigo.dibujar()
        self.bomberman.dibujar()

    
    """
    Creación de los niveles
    """
    # crear: Escenario -> None
    # Crea un nivel pedido
    def crear(self):
        # Creación de muros indestructibles
        self.ponerMurosIndestructibles()
        self.ponerMurosDestruibles(12)
        self.crearEnemigos(self.cantidadEnemigos)
        self.crearBomberman()
        self.crearPowerups(self.cantidadPowerups)


    # ponerMurosIndestructibles: Escenario -> None
    # Función auxiliar para dibujar todos los muros indestructibles del mapa
    def ponerMurosIndestructibles(self):
        muros_ind = []
        # Muros externos
        # Columna Izquierda
        for i in range(13):
            muro_ind = Muro_indestructible([0, i*self.tamCuadr], self.tamCuadr)
            muros_ind.append(muro_ind)
        # Columna Derecha
        for i in range(13):
            muro_ind = Muro_indestructible([14*self.tamCuadr, i*self.tamCuadr], self.tamCuadr)
            muros_ind.append(muro_ind)
        # Fila Superior
        for i in range(1,14):
            muro_ind = Muro_indestructible([i*self.tamCuadr, 0], self.tamCuadr)
            muros_ind.append(muro_ind)
        # Fila Inferior
        for i in range(1,14):
            muro_ind = Muro_indestructible([i*self.tamCuadr, 12*self.tamCuadr], self.tamCuadr)
            muros_ind.append(muro_ind)

        # Muros al interior
        for i in range(2,13,2):
            for j in range(2,11,2):
                muro_ind = Muro_indestructible([i*self.tamCuadr,
                           j*self.tamCuadr], self.tamCuadr)
                muros_ind.append(muro_ind)
            
        self.muros_indestructibles = muros_ind

    # ponerMurosDestruibles: Escenario int -> None
    # Pone los muros destruibles en posiciones aleatorias
    def ponerMurosDestruibles(self, cantidad):
        for i in range(cantidad):
            posx = random.randint(1, 14)
            posy = random.randint(1, 12)
            while True: # Se va a poner sobre un muro indestructible
                muro = Muro_destruible([posx*self.tamCuadr, posy*self.tamCuadr], self.tamCuadr)
                if not self.chocaConMuro(muro):
                    self.muros_destruibles.append(muro)
                    break
                else:
                    posy = random.randint(1,12)
                    posx = random.randint(1,14)

    # Crea los enemigos para cierto nivel
    def crearEnemigos(self, cantidad):
        # En nivel 1 se crean 4 enemigos
        for i in range(cantidad):
            posx = random.randint(1,14)
            posy = random.randint(1, 12)
            tipo = random.randint(1,2)
            while True:
                enemigo = Enemigo([posx*self.tamCuadr, posy*self.tamCuadr], self.tamCuadr, tipo)
                if not self.chocaConMuro(enemigo):
                    self.enemigos.append(enemigo)
                    break
                else:
                    posx = random.randint(1,14)
                    posy = random.randint(1, 12)

    # Crea los power-ups iniciales
    def crearPowerups(self, cantidad):
        # En el nivel 1 se crearán 4 powerups
        for i in range(cantidad):
            posx = random.randint(1,14)
            posy = random.randint(1, 12)
            tipo = random.randint(1,2)
            if tipo == 1:
                tipo = 'velocidad'
            if tipo == 2:
                tipo = 'explosion'

            while True:
                powerup = Powerup([posx*self.tamCuadr, posy*self.tamCuadr], self.tamCuadr, tipo)
                if not self.chocaConMuro(powerup):
                    self.powerups.append(powerup)
                    break
                else:
                    posx = random.randint(1,14)
                    posy = random.randint(1,12)
       
    
    # Crea al bomberman para el nivel
    def crearBomberman(self):
        posx = random.randint(1,14)
        posy = random.randint(1,12)
        while True:
            self.bomberman = Bomberman([posx*self.tamCuadr,posy*self.tamCuadr],self.tamCuadr)
            if not self.chocaConMuro(self.bomberman) and not self.chocaConEnemigo(self.bomberman):
                break
            else:
                posx = random.randint(1,14)
                posy = random.randint(1, 12)
    

    """
    Funciones de actualización de los elementos del escenario
    """
    # actaulizarBombas: Escenario int -> None
    # Actualiza el tiempo de vida que tienen las bombas en juego
    def actualizarBombas(self, DT):
        for bomba in self.bombas:
            bomba.tiempoVida += DT
            if bomba.tiempoVida >= 3: # 3 segundos de vida
                bomba.explotar()
                self.lanzarExplosion(bomba.pos, self.tamCuadr)
                self.sonido_explosion.play()
            if bomba.recienPuesta:
                if not bomba.choca(self.bomberman):
                    bomba.recienPuesta = False

    # lanzarExplosión: Escenario [int,int] int -> None
    # Lanza una explosión en el lugar en que explotó la bomba
    def lanzarExplosion(self, pos, tamano):
        explosion = Explosion(pos, tamano, 'centro')
        self.explosiones.append(explosion)
        explosion.crearExplosiones(self.bomberman.tamExplosion, self.explosiones, self)

    # actualizarExplosiones: Escenario int -> None
    # Se encarga de actualizar las explosiones, para sacarlas del mapa
    def actualizarExplosiones(self, DT):
        for explosion in self.explosiones:
            explosion.tiempoVida += DT
            if explosion.tiempoVida >= 1: # 1 seg de vida
                explosion.destruir()


    # actualizarEnemigos: Escenario -> None
    # Actualiza la posición de los enemigos y si chocan con una explosión
    def actualizarEnemigos(self):
        for enemigo in self.enemigos:
            # Movimientos
            movimiento = random.randint(1, 4)
            if movimiento == 1: # Subir
                enemigo.subir(3)
                if self.chocaConMuro(enemigo):
                    enemigo.bajar(3)
            if movimiento == 2: # Bajar
                enemigo.bajar(3)
                if self.chocaConMuro(enemigo):
                    enemigo.subir(3)
            if movimiento == 3: # Derecha
                enemigo.moverDer(3)
                if self.chocaConMuro(enemigo):
                    enemigo.moverIzq(3)
            if movimiento == 4: # Izquierda
                enemigo.moverIzq(3)
                if self.chocaConMuro(enemigo):
                    enemigo.moverDer(3)

            # Choque con explosiones
            for explosion in self.explosiones:
                if enemigo.choca(explosion):
                    enemigo.destruir()

    # actualizarBomberman: Escenario -> None
    # Actualiza al Bomberman. Busca choques con explosiones, enemigos o Power-Ups.
    def actualizarBomberman(self):
        for explosion in self.explosiones:
            if self.bomberman.choca(explosion):
                self.bomberman.destruir()
        for enemigo in self.enemigos:
            if self.bomberman.choca(enemigo):
                self.bomberman.destruir()
        for powerup in self.powerups:
            if self.bomberman.choca(powerup):
                if powerup.tipo == 'velocidad':
                    self.bomberman.vel += 1
                if powerup.tipo == 'explosion':
                    self.bomberman.tamExplosion += 1
                if powerup.tipo == 'salida':
                    self.borrarTodo()
                    # Condiciones para el sig. nivel:
                    self.salida = False
                    self.cantidadEnemigos += 1
                    if self.cantidadPowerups > 1:
                        self.cantidadPowerups -= 1
                    self.crear()
                    break
                powerup.destruir()

    # actualizarMuros: Escenario -> None
    # Actualiza los muros chequeando si siguen vivos esta partida
    def actualizarMuros(self):
        for explosion in self.explosiones:
            for muro in self.muros_destruibles:
                if muro.choca(explosion):
                    muro.destruir()
                    if not self.salida:
                        probSalida = random.random()
                        ultimo_muro = len(self.muros_destruibles) == 1 # Último muto juego
                        if probSalida <= 0.2 or ultimo_muro: # Se crea una salida
                            salida = Powerup(muro.pos, self.tamCuadr, 'salida') # La
                                            # salida está implementada como Powerup
                            self.powerups.append(salida)
                            self.salida = True # Ya existe salida
                            


    """
    Funciones de apoyo
    """
    # Chequea que el objeto no se ponga sobre un muro, indestructible o no.
    def chocaConMuro(self, objeto):
        for muro in self.muros_destruibles:
            if objeto.choca(muro):
                return True
        for muro in self.muros_indestructibles:
            if objeto.choca(muro):
                return True
        return False

    # chocaConBomba: Escenario -> bool
    # Detecta si efectivamente Bomberman choca con una bomba, siempre después
    # de haberla puesto.
    def chocaConBomba(self, bomberman):
        for bomba in self.bombas:
            if not bomba.recienPuesta:
                if bomberman.choca(bomba):
                    return True
        return False

    # chocaConEnemigo: Escenario -> bool
    # Detecta si efectivamente Bomberman choca con un enemigo.
    def chocaConEnemigo(self, bomberman):
        for enemigo in self.enemigos:
            if bomberman.choca(enemigo):
                return True
        return False

    # borrarTodo: Escenario -> None
    # Borra todos los elementos del escenario
    def borrarTodo(self):
        for muro in self.muros_destruibles:
            muro.destruir()
        for muro in self.muros_indestructibles:
            muro.destruir()
        for bomba in self.bombas:
            bomba.destruir()
        for enemigo in self.enemigos:
            enemigo.destruir()
        for powerup in self.powerups:
            powerup.destruir()
        for explosion in self.explosiones:
            explosion.destruir()
        self.limpiar()
    
                    

            
