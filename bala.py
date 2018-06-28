import pygame
import sys
import math
import pantallas
import config
import sesion
import random
import turnos
from pygame.locals import *

class Bala(pantallas.Pantalla):

    def __init__(self, gestor):
        x = [random.randint(0, config.ANCHO - 100), random.randint(0, config.ANCHO - 100)]
        y = config.ALTO - 150
        self.gestor = gestor
        self.fin_partida = False
        self.xinicial = [x[0] + 65, x[1] + 65]
        self.direccion = [1, 1]
        self.radio = 10
        self.x = [x[0] + 65, x[1] + 65]
        self.y = y - self.radio - 70
        self.v = 150
        self.tiempo = 0
        self.angulo = 45
        self.xmovimiento = [x[0], x[1]]
        self.ymovimiento = config.ANCHO - self.y
        self.disparo = [False, False]
        self.clock = pygame.time.Clock()
        self.fuente = pygame.font.Font(None, 15)
        self.bala = pygame.image.load(config.BALA)
        self.sesion = sesion.Sesion.get_instance()
        self.imagen_jugador = [pygame.image.load(self.sesion.avatar[0]),
                pygame.image.load(self.sesion.avatar[1])]
        self.fondo = pygame.image.load(self.sesion.fondo)
        self.piso = pygame.image.load(self.sesion.piso)

    def update(self):
        if not self.fin_partida:
            self.vx = self.v * math.cos(math.radians(self.angulo)) * self.direccion[0]
            self.vy = self.v * math.sin(math.radians(self.angulo))

            if self.disparo[0] == True:
                self.xmovimiento[0] = self.vx * self.tiempo
                self.ymovimiento = self.vy *self.tiempo + (-50*(self.tiempo**2)/2)
                self.x[0] = self.xmovimiento[0] + self.xinicial[0]
                self.y = config.ANCHO - self.ymovimiento

            if (self.x[0] > config.ANCHO) or (self.y > config.ALTO):
                self.x[0] = self.xinicial[0]
                self.y = config.ALTO
                self.tiempo = 0
                self.disparo[0] = False
        else:
            # Ir a la pantalla que permite visualizar los resultados
            pass

    def get_input(self):
        pygame.key.set_repeat(1, 80)
        tick = self.clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_DOWN:
                    if self.angulo > 0 and self.disparo[0] == False:
                        self.angulo = self.angulo - 1
                elif event.key == K_UP:
                    if self.angulo < 90  and self.disparo[0] == False:
                        self.angulo = self.angulo + 1
                elif event.key == K_SPACE:
                    if self.v < 150  and self.disparo[0] == False:
                        self.v = self.v + 1
                elif event.key == K_RIGHT:
                    if self.direccion[0] < 0 and self.disparo[0] == False:
                        self.direccion[0] = -self.direccion[0]
                    self.x[0] = self.x[0] + 10
                    self.xinicial[0] = self.xinicial[0] +10
                elif event.key == K_LEFT:
                    if self.direccion[0] > 0 and self.disparo[0] == False:
                        self.direccion[0] = -self.direccion[0]
                    self.x[0] = self.x[0] - 10
                    self.xinicial[0] = self.xinicial[0] -10
                elif event.key == K_RETURN:
                    self.disparo[0] = True
                elif event.key == K_ESCAPE:
                    sys.exit()
        if self.disparo[0]:
            self.tiempo = self.tiempo + (tick / 1000.0)
    def render(self):
        self.gestor.pantalla.blit(self.fondo, (0,0))
        if self.disparo[0]:
            pygame.draw.circle(self.gestor.pantalla,(155,155,155),(int(self.x[0]),int(self.y)),self.radio)
        if self.direccion[0] < 0:
            self.gestor.pantalla.blit(self.imagen_jugador[0],(int(self.xinicial[0]-self.radio),config.ALTO-150))
        else :
            self.gestor.pantalla.blit(pygame.transform.flip(self.imagen_jugador[0],True,False),(int(self.xinicial[0]-self.radio),config.ALTO-150))
        self.gestor.pantalla.blit(self.piso, (0, 550))
        pygame.display.update()

    def ir_login(self):
        pass

    def ir_jugador(self):
        pass

    def ir_admin(self):
        pass

