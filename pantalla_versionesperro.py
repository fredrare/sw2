#personalizar Perro

import pygame, sys, boton
from pygame.locals import *
import pantallas
import pantalla_personajes
import boton
import config

class Perro(pantallas.PantallaJugador):
    def __init__(self, gestor):
        self.gestor = gestor
        pygame.display.set_caption("personalizarcuy")

        self.fondo = pygame.image.load(config.fondo[0])
        self.postX = 650
        self.postY = 600
        self.ventana = pygame.display.set_mode((800,600))
        pygame.display.set_caption("listapersonalizacion")

#Personaje PERRO
        self.personajePerro = pygame.image.load("Imagenes/Personaje/PerroOriginal.png")
        self.posX_PP,self.posY_PP=150,100 #Posicion personaje perro
        self.seleccionarPerro = boton.Button(150,200,140,40, text = 'PerroBase')

        self.personajePerro1 = pygame.image.load("Imagenes/Personaje/Perro-v1.png")
        self.posX_PP1,self.posY_PP1=150,250
        self.seleccionarP1 = boton.Button(150,350,140,40, text = 'PerroV1')

        self.personajePerro2 = pygame.image.load("Imagenes/Personaje/Perro-v2.png")
        self.posX_PP2,self.posY_PP2=500,250
        self.seleccionarP2 = boton.Button(500,200,140,40, text = 'PerroV2')

        self.personajePerro3 = pygame.image.load("Imagenes/Personaje/Perro-v3.png")
        self.posX_PP3,self.posY_PP3=500,100
        self.seleccionarP3 = boton.Button(500,200,140,40, text = 'PerroV3')

        self.atras = boton.Button(200,500,100,40, text = 'Atras')
        self.salir = boton.Button(600,500, 100, 40, text = 'Salir')

        self.situado = True
        self.seleccionado = False

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.seleccionarPerro.handle_event(event)
            self.seleccionarP1.handle_event(event)
            self.seleccionarP2.handle_event(event)
            self.seleccionarP3.handle_event(event)

            self.atras.handle_event(event)
            self.salir.handle_event(event)

    def update(self):

        if self.seleccionarP1.active:
            self.personajePerro = self.personalizarPerro1
            if self.personajePerro.active:
                self.gestor.pantalla_actual.ir_juego()
        elif self.seleccionarP2.active:
            self.personajePerro = self.personalizarPerro2
            if self.personajePerro.active:
                self.gestor.pantalla_actual.ir_juego()
        elif self.seleccionarP3.active:
            self.personajePerro = self.personalizarPerro3
            if self.personajePerro.active:
                self.gestor.pantalla_actual.ir_juego()

    def render(self):

        self.ventana.blit(self.fondo,(0,0))

        pygame.draw.rect(self.ventana,(0,100,205),(150,100,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(150,250,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(500,250,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(500,100,150,100))

        self.seleccionarP1.draw(self.ventana)
        self.seleccionarP2.draw(self.ventana)
        self.seleccionarP3.draw(self.ventana)

        self.atras.draw(self.ventana)
        self.salir.draw(self.ventana)

        if self.situado:
            self.ventana.blit(self.personajePerro, (self.posX_PP, self.posY_PP))
            self.ventana.blit(self.personajePerro1, (self.posX_PP1,self.posY_PP1))
            self.ventana.blit(self.personajePerro2, (self.posX_PP2,self.posY_PP2))
            self.ventana.blit(self.personajePerro3, (self.posX_PP3,self.posY_PP3))
        if self.atras.active:
            self.gestor.pantalla_actual.ir_personajes() #si presiona atras va para escoger personajes
        if self.salir.active:
            pygame.quit()
            sys.exit()

        pygame.display.update()

    def ir_sala(self):
        self.gestor.pantalla_actual = pantalla_sala.PantallaSala(self.gestor)
        pass
    def ir_personajes(self):
        self.gestor.pantalla_actual = pantalla_personajes.Personajes(self.gestor)
