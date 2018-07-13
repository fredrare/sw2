import pygame
import pantallas
import config
import boton
import sys
import pantalla_admin_baneo
import pantalla_admin_tiempo

class PantallaAdmin(pantallas.Pantalla):
    def __init__(self,gestor):
        self.gestor = gestor
        pygame.display.set_caption("Pantalla Admin")

        self.fondo = pygame.image.load(config.fondo[0])

        self.llama = pygame.image.load(config.avatar['l0'])
        self.perro = pygame.image.load(config.avatar['p1'])
        self.gallo = pygame.image.load(config.avatar['g2'])
        self.cuy = pygame.image.load(config.avatar['c3'])

        self.banear = boton.Button(400,300,100,40, "Banear")
        self.salir = boton.Button(700, 550 , 100, 40, "Salir")
        self.tiempo = boton.Button(250, 300 , 100, 40, "Tiempo")



    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.banear.handle_event(event)
            self.salir.handle_event(event)
            self.tiempo.handle_event(event)

    def update(self):

        if self.salir.active:
            pygame.quit()
            sys.exit()
        if self.banear.active:
            self.gestor.pantalla_actual.ir_baneo()
        if self.tiempo.active:
            self.gestor.pantalla_actual.ir_tiempo()


    def render(self):
        self.gestor.pantalla.blit(self.fondo,(0,0))

        self.gestor.pantalla.blit(self.llama, (125, 100))
        self.gestor.pantalla.blit(self.perro, (275, 100))
        self.gestor.pantalla.blit(self.gallo, (425, 100))
        self.gestor.pantalla.blit(self.cuy, (575, 100))

        self.banear.draw(self.gestor.pantalla)
        self.salir.draw(self.gestor.pantalla)
        self.tiempo.draw(self.gestor.pantalla)
        pygame.display.update()

    def ir_baneo(self):
        self.gestor.pantalla_actual = pantalla_admin_baneo.PantallaBaneo(self.gestor)
    def ir_tiempo(self):
        self.gestor.pantalla_actual = pantalla_admin_tiempo.PantallaTiempo(self.gestor)
