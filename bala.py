<<<<<<< HEAD
import pygame
import pantalla_resultados
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
import model_vida
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
        self.cronometro = turnos.Cronometro.get_instance()
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
        self.model = model_vida.ModelVida(self.xinicial[0], self.xinicial[1])
        pygame.key.set_repeat(10, 1)

    def update(self):
        if not self.fin_partida:
            self.model.update(self.xinicial[0], self.xinicial[1])
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
                hit = self.model.colision(self.x[0], self.y, self.x[1], self.y)
                if hit > 0 or (self.x[self.turno] > config.ANCHO) or (self.y > config.ALTO):
                    self.vidas[1 - self.turno].update(hit)
                    self.x[self.turno] = self.xinicial[self.turno]
                    self.y = self.yinicial
                    self.tiempo = 0
                    self.tiempo_inicio = self.getTime()
                    self.v = 0
                    self.disparando[self.turno] = False
                    self.cronometro.restart()
                    if self.vidas[1 - self.turno].ammount <= 0:
                        self.sesion.ganador = self.turno
                        self.fin_partida = True
            else:
                self.tiempo_inicio = self.getTime()
                self.angulos[self.turno].update(self.angulo[self.turno],
                        self.xinicial[self.turno])
        else:
            # Ir a la pantalla que permite visualizar los resultados
            self.ir_resultados()

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

    def ir_resultados(self):
        self.gestor.pantalla_actual = pantalla_resultados.PantallaResultados(self.gestor)

    def ir_jugador(self):
        pass

    def ir_admin(self):
        pass

=======
import pygame
import sys
import math
import pantallas
import config
from pygame.locals import *

class Bala(pantallas.Pantalla):

    def __init__(self, gestor, x, y):
        self.gestor = gestor
        self.xinicial = x +65
        self.direccion = 1
        self.radio = 10
        self.x = x + 65
        self.y = y - self.radio - 70
        self.v = 150
        self.tiempo = 0
        self.angulo = 45
        self.xmovimiento = x
        self.ymovimiento = config.ANCHO - self.y
        self.disparo = False
        self.fondo = pygame.image.load("Imagenes/peru.jpg")
        self.clock = pygame.time.Clock()
        self.fuente = pygame.font.Font(None, 15)
        self.imagen_otorongo = pygame.image.load("Imagenes/Otorongo.png").convert_alpha()

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
                    self.x = self.x + 10
                    self.xinicial = self.xinicial +10
                elif event.key == K_LEFT:
                    if self.direccion > 0 and self.disparo == False:
                        self.direccion = -self.direccion
                    self.x = self.x - 10
                    self.xinicial = self.xinicial -10
                elif event.key == K_RETURN:
                    self.disparo = True
                elif event.key == K_ESCAPE:
                    sys.exit()
        if self.disparo == True:
            self.tiempo = self.tiempo + (tick / 1000.0)
    def render(self):
        self.gestor.pantalla.blit(self.fondo,(0,0))
        pygame.draw.circle(self.gestor.pantalla,(155,155,155),(int(self.x),int(self.y)),self.radio)
        if self.direccion > 0  :
            self.gestor.pantalla.blit(self.imagen_otorongo,(int(self.xinicial-self.radio),config.ALTO-100))
        else :
            self.gestor.pantalla.blit(pygame.transform.flip(self.imagen_otorongo,True,False),(int(self.xinicial-self.radio),config.ALTO-100))

        pygame.display.update()


    def ir_login(self):
        pass

    def ir_jugador(self):
        pass

    def ir_admin(self):
        pass
>>>>>>> ec347ad4fcdf3d822d9a7f0c78eb5a8bc4844326
