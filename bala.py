import pygame
import sys
import math
import pantallas
import config
from pygame.locals import *

class Bala(pantallas.Pantalla):

    def __init__(self, gestor, x, y):
        self.gestor = gestor
        self.xinicial = x
        self.direccion = 1
        self.x = x
        self.y = y
        self.v = 150
        self.tiempo = 0
        self.angulo = 45
        self.xmovimiento = x
        self.ymovimiento = config.ANCHO - self.y
        self.disparo = False
      self.fondo = pygame.image.load("Imagenes/peru.j")
        self.clock = pygame.time.Clock()
        self.fuente = pygame.font.Font(None, 15)

    def update(self):

        self.vx = self.v * math.cos(math.radians(self.angulo))*self.direccion
        self.vy = self.v * math.sin(math.radians(self.angulo))

        if self.disparo == True:
            self.xmovimiento = self.vx * self.tiempo
            self.ymovimiento = self.vy *self.tiempo + (-50*(self.tiempo**2)/2)
            self.x = self.xmovimiento + self.xinicial
            self.y = config.ANCHO - self.ymovimiento

        else :
            pass

        if (self.x > config.ANCHO) or (self.y > config.ALTO):
            self.x = self.xinicial
            self.y = config.ALTO
            self.tiempo = 0
            self.disparo = False

    def get_input(self):
        pygame.key.set_repeat(1, 80)
        tick = self.clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_DOWN:
                    if self.angulo > 0 and self.disparo == False:
                        self.angulo = self.angulo - 1
                elif event.key == K_UP:
                    if self.angulo < 90  and self.disparo == False:
                        self.angulo = self.angulo + 1
                elif event.key == K_SPACE:
                    if self.v < 150  and self.disparo == False:
                        self.v = self.v + 1
                elif event.key == K_RIGHT:
                    if self.direccion < 0 and self.disparo == False:
                        self.direccion = -self.direccion
                elif event.key == K_LEFT:
                    if self.direccion > 0 and self.disparo == False:
                        self.direccion = -self.direccion
                    pass
                elif event.key == K_RETURN:
                    self.disparo = True
                elif event.key == K_ESCAPE:
                    sys.exit()
        if self.disparo == True:
            self.tiempo = self.tiempo + (tick / 1000.0)
    def render(self):

        self.gestor.pantalla.blit(self.fondo,(0,0))
        pygame.draw.circle(self.gestor.pantalla,(155,155,155),(int(self.x),int(self.y)),10)
        pygame.display.update()

    def ir_login(self):
        pass

    def ir_jugador(self):
        pass

    def ir_admin(self):
        pass
