import pygame
import pantallas
import text_input
import config
import requests
import boton
import pantalla_login

class PantallaLobby(pantallas.Pantalla):
    fondo = pygame.image.load("Imagenes/peru.jpg")
    def get_input(self):
        pass

    def update(self):
        pass
    def render(self):
        self.gestor.pantalla.blit(self.gestor.superficie, (0,0))
        self.gestor.pantalla.blit(self.fondo, (0, 0))
        pygame.display.update()

    def ir_login(self):
        self.gestor.pantalla_actual = pantalla_lobby.PantallaLogin(self.gestor)
        pass
    def ir_jugador(self):
        pass
    def ir_admin(self):
        pass

