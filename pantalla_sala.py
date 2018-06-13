import pygame
import pantallas
import text_input
import config
import requests
import boton
import sys

class PantallaSala(pantallas.Pantalla):
    def __init__(self, gestor):
        self.gestor = gestor
        pygame.display.set_caption("lobby")

        self.fondo = pygame.image.load("Imagenes/peru.jpg")

        self.imagen_otorongo = pygame.image.load("Imagenes/Otorongo.png").convert_alpha()
        self.posX_Oto,self.posY_Oto = 150,100
        self.is_ready = False
        self.derecha = True
        self.dere = True
        self.imagen_ready = pygame.image.load("Imagenes/ready.png")
        self.imagen_peru = pygame.image.load("Imagenes/peru.png")
        self.postX = 650
        self.postY = 600
        self.cambiar_equipo = boton.Button(400, 550, 100, 40, text = 'Cambiar')
        self.ready = boton.Button(300, 550, 100, 40, text = 'Ready')
        self.iniciar = boton.Button(360, 500, 100, 40, text = 'Iniciar')
        self.salir = boton.Button(650, 650, 100, 40, text = 'Salir')
        self.velocidad = 2

    def get_input(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.cambiar_equipo.handle_event(event)
            self.ready.handle_event(event)
            self.salir.handle_event(event)

    def update(self):
        if self.cambiar_equipo.active:
            self.derecha = not self.derecha
            self.cambiar_equipo.active = False
        if self.ready.active:
            self.is_ready = not self.is_ready
            self.ready.active = False
        if self.salir.active:
            pygame.quit()
            sys.exit()
        if self.dere == True:
            if self.postX<800:
                self.postX+=self.velocidad
            else:
                self.dere = False
        else:
            if self.postX>1:
                self.postX-=self.velocidad
            else:
                self.dere = True

    def render(self):
        self.gestor.pantalla.blit(self.fondo,(0,0))
        pygame.draw.rect(self.gestor.pantalla,(130,70,70),(150,100,150,100))
        pygame.draw.rect(self.gestor.pantalla,(130,70,70),(150,250,150,100))
        pygame.draw.rect(self.gestor.pantalla,(130,70,70),(150,400,150,100))
        pygame.draw.rect(self.gestor.pantalla,(130,70,70),(500,100,150,100))
        pygame.draw.rect(self.gestor.pantalla,(130,70,70),(500,250,150,100))
        pygame.draw.rect(self.gestor.pantalla,(130,70,70),(500,400,150,100))
        if self.derecha:
            self.gestor.pantalla.blit(self.imagen_otorongo, (self.posX_Oto, self.posY_Oto))
        else:
            self.gestor.pantalla.blit(pygame.transform.flip(self.imagen_otorongo, True, False),(550, 100))
        if self.is_ready:
            self.gestor.pantalla.blit(self.imagen_ready,(330,200))
        self.cambiar_equipo.draw(self.gestor.pantalla)
        self.ready.draw(self.gestor.pantalla)
        self.salir.draw(self.gestor.pantalla)
        self.gestor.pantalla.blit(self.imagen_peru,(self.postX,self.postY))
        pygame.display.update()
    def ir_login(self):
        pass

    def ir_jugador(self):
        pass

    def ir_admin(self):
        pass
