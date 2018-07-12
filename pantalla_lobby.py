import pygame
import pantallas
import text_input
import config
import requests
import boton
import pantalla_login
import pantalla_sala
<<<<<<< HEAD
import sys
=======
>>>>>>> ec347ad4fcdf3d822d9a7f0c78eb5a8bc4844326

class PantallaLobby(pantallas.Pantalla):
    def __init__(self, gestor):
        pygame.display.set_caption("lobby")
        self.gestor = gestor
<<<<<<< HEAD
        self.fondo = pygame.image.load(config.fondo[0])
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
=======
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
>>>>>>> ec347ad4fcdf3d822d9a7f0c78eb5a8bc4844326
        pygame.display.update()

    def ir_tienda(self):
        self.gestor.pantalla_actual = pantalla_tienda.PantallaTienda(self.gestor)
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
