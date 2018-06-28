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
        pygame.display.set_caption("lobby")
        self.gestor = gestor
        self.fondo = pygame.image.load("Imagenes/Machu_Pichu.png")
        self.sala1 = boton.Button(300, 280, 250, 80, "Sala 1", 80 )
        self.tienda = boton.Button(700, 70, 90, 50, "Tienda")
        self.salir = boton.Button(700, 550 , 100, 40, "Salir")
    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.sala1.handle_event(event)
            self.tienda.handle_event(event)
            self.salir.handle_event(event)

    def update(self):
        if self.salir.active:
            pygame.quit()
            sys.exit()
        if self.tienda.active:
            self.gestor.pantalla_actual.ir_tienda()
        if self.sala1.active:
            self.gestor.pantalla_actual.ir_sala()

    def render(self):
        self.gestor.pantalla.blit(self.gestor.superficie, (0,0))
        self.gestor.pantalla.blit(self.fondo, (0, 0))
        #self.gestor.pantalla.blit(self.boton)
        self.sala1.draw(self.gestor.pantalla)
        self.tienda.draw(self.gestor.pantalla)
        self.salir.draw(self.gestor.pantalla)
        pygame.display.update()

    def ir_tienda(self):
        self.gestor.pantalla_actual = pantalla_tienda.PantallaTienda(self.gestor)
    def ir_sala(self):
        self.gestor.pantalla_actual = pantalla_sala.PantallaSala(self.gestor)

    def ir_login(self):
        pass
    def ir_jugador(self):
        pass
    def ir_admin(self):
        pass
