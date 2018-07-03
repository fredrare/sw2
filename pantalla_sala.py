import pygame
import pantallas
import text_input
import config
import requests
import boton
import sys
import bala
import pantalla_lobby
import sesion
import pantalla_versionescuy
import pantalla_versionesllama
import pantalla_versionesperro
import pantalla_versionesgallito
import pantalla_personajes
#import bala

class PantallaSala(pantallas.Pantalla):

    def __init__(self, gestor):
        self.sesion = sesion.Sesion.get_instance()
        self.gestor = gestor
        pygame.display.set_caption("sala")

        self.fondo = pygame.image.load(config.fondo[0])

        self.imagen_jugador_2 = pygame.image.load(config.avatar['l1']).convert_alpha()
        self.imagen_jugador_1 = gestor.personajeJugador1
        self.posX_Llama,self.posY_Llama = 150,100
        self.is_ready = False
        #self.derecha = True
        self.imagen_ready = pygame.image.load("Imagenes/ready.png")
        #self.cambiar_equipo = boton.Button(400, 550, 100, 40, text = 'Cambiar')
        self.ready = boton.Button(350, 550, 100, 40, text = 'Ready')
        self.iniciar = boton.Button(350, 450, 100, 40, text = 'Iniciar')
        self.salir = boton.Button(700, 550 , 100, 40, "Salir")
        self.regresar = boton.Button(10, 550 , 100, 40, "Regresar")
        self.cambiar_fondo = boton.Button(330, 350, 160, 40, "Cambiar Fondo" )
        self.cambiar_piso = boton.Button(330, 250, 160, 40, "Cambiar Piso")

        self.cambiar_personaje = boton.Button(330,150,160,40, "Cambiar Personaje")
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
            self.cambiar_fondo.handle_event(event)
            self.cambiar_piso.handle_event(event)
            self.cambiar_personaje.handle_event(event)

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
        if self.cambiar_fondo.active:
            self.sesion.fondo = config.fondo[(config.fondo.index(self.sesion.fondo)+1)%len(config.fondo)]
            self.cambiar_fondo.active = False
        if self.cambiar_piso.active:
            self.sesion.piso = config.piso[(config.piso.index(self.sesion.piso)+1)%len(config.piso)]
            self.cambiar_piso.active = False
        if self.cambiar_personaje.active:
            self.gestor.pantalla_actual.ir_personaje()

    def render(self):
        self.gestor.pantalla.blit(self.fondo,(0,0))
        pygame.draw.rect(self.gestor.pantalla,(130,70,70),(150,100,150,120))
        #pygame.draw.rect(self.gestor.pantalla,(130,70,70),(150,250,150,100))
        #pygame.draw.rect(self.gestor.pantalla,(130,70,70),(150,400,150,100))
        pygame.draw.rect(self.gestor.pantalla,(130,70,70),(500,100,150,120))
        #pygame.draw.rect(self.gestor.pantalla,(130,70,70),(500,250,150,100))
        #pygame.draw.rect(self.gestor.pantalla,(130,70,70),(500,400,150,100))
        # if self.derecha:
        #    self.gestor.pantalla.blit(pygame.transform.flip(self.imagen_jugador_2, True, False),(550, 100))
        #else:
        self.gestor.pantalla.blit(self.imagen_jugador_1 , (150, 100))
        self.gestor.pantalla.blit(pygame.transform.flip(self.imagen_jugador_2, True, False),(550, 100))
        if self.is_ready:
            self.gestor.pantalla.blit(self.imagen_ready,(330,200))
        #self.cambiar_equipo.draw(self.gestor.pantalla)
        self.ready.draw(self.gestor.pantalla)
        self.salir.draw(self.gestor.pantalla)
        self.iniciar.draw(self.gestor.pantalla)
        self.regresar.draw(self.gestor.pantalla)
        self.cambiar_fondo.draw(self.gestor.pantalla)
        self.cambiar_piso.draw(self.gestor.pantalla)
        self.cambiar_personaje.draw(self.gestor.pantalla)
        pygame.display.update()

    def ir_bala(self):
        self.gestor.pantalla_actual = bala.Bala(self.gestor)
    def ir_lobby(self):
        self.gestor.pantalla_actual = pantalla_lobby.PantallaLobby(self.gestor)
    def ir_personaje(self):
        self.gestor.pantalla_actual = pantalla_personajes.Personajes(self.gestor)
    def ir_login(self):
        pass
    def ir_jugador(self):
        pass
    def ir_admin(self):
        pass
