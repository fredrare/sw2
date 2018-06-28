import pygame
import pantallas
import text_input
import config
import requests
import boton
import sys
import pantalla_lobby
#import bala

class PantallaSala(pantallas.Pantalla):
    def __init__(self, gestor):
        self.gestor = gestor
        pygame.display.set_caption("sala")

        self.fondo = pygame.image.load(config.fondo[0])

        self.imagen_otorongo = pygame.image.load(config.avatar['l0']).convert_alpha()
        self.imagen_llamita = pygame.image.load(config.avatar['l1']).convert_alpha()
        self.posX_Llama,self.posY_Llama = 150,100
        self.is_ready = False
        #self.derecha = True
        self.imagen_ready = pygame.image.load("Imagenes/ready.png")
        #self.cambiar_equipo = boton.Button(400, 550, 100, 40, text = 'Cambiar')
        self.ready = boton.Button(350, 550, 100, 40, text = 'Ready')
        self.iniciar = boton.Button(350, 450, 100, 40, text = 'Iniciar')
        self.salir = boton.Button(700, 550 , 100, 40, "Salir")
        self.regresar = boton.Button(10, 550 , 100, 40, "Regresar")

    def get_input(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #self.cambiar_equipo.handle_event(event)
            self.ready.handle_event(event)
            self.salir.handle_event(event)
            self.regresar.handle_event(event)
            self.iniciar.handle_event(event)

    def update(self):
        #if self.cambiar_equipo.active:
        #    self.derecha = not self.derecha
        #    self.cambiar_equipo.active = False
        if self.ready.active:
            self.is_ready = not self.is_ready
            self.ready.active = False
            self.gestor.pantalla
        if self.salir.active:
            pygame.quit()
            sys.exit()
        if self.regresar.active:
            self.gestor.pantalla_actual.ir_lobby()
        if self.iniciar.active:
            self.gestor.pantalla_actual.ir_bala()

    def render(self):
        self.gestor.pantalla.blit(self.fondo,(0,0))
        pygame.draw.rect(self.gestor.pantalla,(130,70,70),(150,100,150,120))
        #pygame.draw.rect(self.gestor.pantalla,(130,70,70),(150,250,150,100))
        #pygame.draw.rect(self.gestor.pantalla,(130,70,70),(150,400,150,100))
        pygame.draw.rect(self.gestor.pantalla,(130,70,70),(500,100,150,120))
        #pygame.draw.rect(self.gestor.pantalla,(130,70,70),(500,250,150,100))
        #pygame.draw.rect(self.gestor.pantalla,(130,70,70),(500,400,150,100))
        # if self.derecha:
        #    self.gestor.pantalla.blit(pygame.transform.flip(self.imagen_otorongo, True, False),(550, 100))
        #else:
        self.gestor.pantalla.blit(self.imagen_llamita , (150, 100))
        self.gestor.pantalla.blit(pygame.transform.flip(self.imagen_otorongo, True, False),(550, 100))
        if self.is_ready:
            self.gestor.pantalla.blit(self.imagen_ready,(330,200))
        #self.cambiar_equipo.draw(self.gestor.pantalla)
        self.ready.draw(self.gestor.pantalla)
        self.salir.draw(self.gestor.pantalla)
        self.iniciar.draw(self.gestor.pantalla)
        self.regresar.draw(self.gestor.pantalla)
        pygame.display.update()

    def ir_bala(self):
        self.gestor.pantalla_actual = bala.Bala(self.gestor)
    def ir_lobby(self):
        self.gestor.pantalla_actual = pantalla_lobby.PantallaLobby(self.gestor)
    def ir_login(self):
        pass
    def ir_jugador(self):
        pass
    def ir_admin(self):
        pass
