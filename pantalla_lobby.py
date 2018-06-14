import pygame
import pantallas
import text_input
import config
import requests
import boton
import pantalla_login

class PantallaLobby(pantallas.Pantalla):
    def __init__(self, gestor):
        self.gestor = gestor
        self.fondo = pygame.image.load("Imagenes/peru.jpg")
        sala = boton.Boton((config.ANCHO - 50)/2, 200, 200, 100, "Sala 1")
    def get_input(self):
        pass

    def update(self):
        pass
    def render(self):
        self.gestor.pantalla.blit(self.gestor.superficie, (0,0))
        self.gestor.pantalla.blit(self.fondo, (0, 0))
        self.gestor.pantalla.blit(self.boton)
        pygame.display.update()

    def ir_login(self):
        self.gestor.pantalla_actual = pantalla_lobby.PantallaLogin(self.gestor)
        pass
    def ir_jugador(self):
        pass
    def ir_admin(self):
        pass

