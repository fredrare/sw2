import pygame
import time
import sys
import math
import pantallas
import config
import poder
import angulo
import sesion
import random
import vida
import turnos
from pygame.locals import *

class Bala(pantallas.Pantalla):

    def __init__(self, gestor):
        x = [random.randint(0, config.ANCHO - 100), random.randint(0, config.ANCHO - 100)]
        y = config.ALTO - 100
        self.gestor = gestor
        self.fin_partida = False
        self.xinicial = [i + 65 for i in x]
        self.yinicial= config.ALTO - 150
        self.direccion = [1, 1]
        self.radio = 10
        self.x = self.xinicial[:]
        self.y = y - self.radio
        self.v = 0
        self.tiempo = 0
        self.angulo = [45, 45]
        self.xmovimiento = x[:]
        self.ymovimiento = config.ANCHO - self.y
        self.disparando = [False, False]
        self.clock = pygame.time.Clock()
        self.fuente = pygame.font.Font(None, 15)
        self.bala = pygame.image.load(config.BALA)
        self.sesion = sesion.Sesion.get_instance()
        self.imagen_jugador = [pygame.image.load(self.sesion.avatar[0]),
                pygame.image.load(self.sesion.avatar[1])]
        self.fondo = pygame.image.load(self.sesion.fondo)
        self.piso = pygame.image.load(self.sesion.piso)
        self.cronometro = turnos.Cronometro()
        self.turno = 0
        self.gravedad = -50
        self.getTime = lambda: int(round(time.time() * 1000))
        self.tiempo_inicio = self.getTime()
        self.poder = poder.Power(1, 20, config.ANCHO - 2, 20, 250)
        self.vidas = [
                vida.Vida(1, 1, config.ANCHO / 2 - 2, 20, 100),
                vida.Vida(config.ANCHO / 2 + 2, 1, config.ANCHO / 2 - 2, 20, 100)]
        self.angulos = [angulo.Angle(i, config.ALTO - 100)
                for i in self.xinicial]
        pygame.key.set_repeat(10, 1)

    def update(self):
        if not self.fin_partida:
            self.poder.update(self.v)
            self.turno = 0 if self.cronometro.turno else 1
            vx = self.v * math.cos(math.radians(self.angulo[self.turno])) * self.direccion[self.turno]
            vy = self.v * math.sin(math.radians(self.angulo[self.turno]))
            if self.disparando[self.turno]:
                self.tiempo = (self.getTime() - self.tiempo_inicio) / 400.0
                self.xmovimiento[self.turno] = vx * self.tiempo
                self.ymovimiento = vy * self.tiempo + (self.gravedad * self.tiempo ** 2 / 2)
                self.x[self.turno] = self.xinicial[self.turno] + self.xmovimiento[self.turno]
                self.y = self.yinicial - self.ymovimiento
                if (self.x[self.turno] > config.ANCHO) or (self.y > config.ALTO):
                    self.x[self.turno] = self.xinicial[self.turno]
                    self.y = self.yinicial
                    self.tiempo = 0
                    self.tiempo_inicio = self.getTime()
                    self.v = 0
                    self.disparando[self.turno] = False
                    self.cronometro.restart()
            else:
                self.tiempo_inicio = self.getTime()
                self.angulos[self.turno].update(self.angulo[self.turno],
                        self.xinicial[self.turno])
        else:
            # Ir a la pantalla que permite visualizar los resultados
            pass

    def key_pressed(self, key):
        if not self.disparando[self.turno]:
            if key == K_DOWN:
                if self.angulo[self.turno] > 0:
                    self.angulo[self.turno] -= 1
            elif key == K_UP:
                if self.angulo[self.turno] < 90:
                    self.angulo[self.turno] += 1
            elif key == K_SPACE:
                if self.v < 250:
                    self.v += 2
            elif key == K_RIGHT:
                if self.direccion[self.turno] < 0:
                    self.direccion[self.turno] = -self.direccion[self.turno]
                    self.angulos[self.turno].flip()
                if self.x[self.turno] <= config.ANCHO:
                    self.x[self.turno] += 10
                    self.xinicial[self.turno] += 10
            elif key == K_LEFT:
                if self.direccion[self.turno] > 0:
                    self.direccion[self.turno] = - self.direccion[self.turno]
                    self.angulos[self.turno].flip()
                if self.x[self.turno] >= 0:
                    self.x[self.turno] -= 10
                    self.xinicial[self.turno] -= 10
            elif key == K_RETURN:
                self.disparando[self.turno] = True
        if key == K_ESCAPE:
            self.cronometro.fin = True
            pygame.quit()
            sys.exit()
            pygame.event.pump()

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.key_pressed(event.key)

    def render(self):
        self.gestor.pantalla.blit(self.fondo, (0, 0))
        if self.disparando[self.turno]:
            pygame.draw.circle(self.gestor.pantalla,
                    (155, 155, 155),
                    (int(self.x[self.turno]) + 50, int(self.y) + 50),
                    self.radio)
        for i in range(0, 2):
            self.angulos[i].draw(self.gestor.pantalla)
            if self.direccion[i] < 0:
                self.gestor.pantalla.blit(self.imagen_jugador[i],
                        (int(self.xinicial[i] - self.radio),
                            self.yinicial))
            else :
                self.gestor.pantalla.blit(
                        pygame.transform.flip(self.imagen_jugador[i], True, False),
                        (int(self.xinicial[i] - self.radio), self.yinicial))
        self.gestor.pantalla.blit(self.piso, (0, 550))
        for i in self.vidas:
            i.draw(self.gestor.pantalla)
        self.poder.draw(self.gestor.pantalla)
        pygame.display.update()

    def ir_login(self):
        pass

    def ir_jugador(self):
        pass

    def ir_admin(self):
        pass

