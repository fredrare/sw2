import pygame
import pantallas
import text_input
import config
import requests
import boton
import pantalla_login
import pantalla_sala

class PantallaLobby(pantallas.Pantalla):
    def __init__(self, gestor):
        self.gestor = gestor
        self.fondo = pygame.image.load("Imagenes/peru.jpg")
        self.sala = boton.Button((config.ANCHO - 50)/2, 200, 200, 100, "Sala 1")
    def get_input(self):
        for event in pygame.event.get():
            self.sala.handle_event(event)

    def update(self):
        if self.sala.active:
            self.sala.active = False
            self.gestor.pantalla_actual.ir_sala()
        pass
    def render(self):
        self.gestor.pantalla.blit(self.gestor.superficie, (0,0))
        self.gestor.pantalla.blit(self.fondo, (0, 0))
        self.sala.draw(self.gestor.pantalla)
        pygame.display.update()

    def ir_login(self):
        self.gestor.pantalla_actual = pantalla_lobby.PantallaLogin(self.gestor)
        pass
    def ir_sala(self):
        self.gestor.pantalla_actual = pantalla_sala.PantallaSala(self.gestor)
    def ir_jugador(self):
        pass
    def ir_admin(self):
        pass

