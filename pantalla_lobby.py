import pygame
import pantallas
import text_input
import config
import requests
import boton
import pantalla_login
import pantalla_sala
import sys

class PantallaLobby(pantallas.Pantalla):
    def __init__(self, gestor):
        pygame.display.set_caption("Lobby")
        self.gestor = gestor
        self.llama = pygame.image.load(config.avatar['l0'])
        self.perro = pygame.image.load(config.avatar['p1'])
        self.gallo = pygame.image.load(config.avatar['g2'])
        self.cuy = pygame.image.load(config.avatar['c3'])
        self.fondo = pygame.image.load(config.fondo[0])
        self.sala1 = boton.Button(225, 280, 380, 80, "Sala de juego", 80 )
        self.salir = boton.Button(700, 550 , 100, 40, "Salir")
    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.sala1.handle_event(event)
            self.salir.handle_event(event)

    def update(self):
        if self.salir.active:
            pygame.quit()
            sys.exit()
        if self.sala1.active:
            self.gestor.pantalla_actual.ir_sala()

    def render(self):
        self.gestor.pantalla.blit(self.gestor.superficie, (0,0))
        self.gestor.pantalla.blit(self.fondo, (0, 0))
        self.gestor.pantalla.blit(self.llama, (125, 100))
        self.gestor.pantalla.blit(self.perro, (275, 100))
        self.gestor.pantalla.blit(self.gallo, (425, 100))
        self.gestor.pantalla.blit(self.cuy, (575, 100))
        self.sala1.draw(self.gestor.pantalla)
        self.salir.draw(self.gestor.pantalla)
        pygame.display.update()

    def ir_sala(self):
        self.gestor.pantalla_actual = pantalla_sala.PantallaSala(self.gestor)
    def ir_login(self):
        pass
    def ir_sala(self):
        self.gestor.pantalla_actual = pantalla_sala.PantallaSala(self.gestor)
    def ir_jugador(self):
        pass
    def ir_admin(self):
        pass
