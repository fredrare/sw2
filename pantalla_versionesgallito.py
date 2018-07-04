#personalizar Gallito

import pygame, sys, boton
from pygame.locals import *
import pantallas
import pantalla_personajes
import boton
import config
import pantalla_sala
import sesion

class Gallo(pantallas.PantallaJugador):
    def __init__(self, gestor):
        self.gestor = gestor
        pygame.display.set_caption("personalizargallo")

        self.fondo = pygame.image.load(config.fondo[0])
        self.postX = 650
        self.postY = 600
        self.ventana = pygame.display.set_mode((800,600))
        pygame.display.set_caption("listapersonalizacion")

#Personaje GALLITO
        self.personajeGallito = pygame.image.load(config.avatar[0])
        self.posX_PG,self.posY_PG=150,100 #Posicion personaje Gallito
        self.seleccionarGallito = boton.Button(150,200,140,40, text = 'GallitoBase')

        self.personajeGallito1 = pygame.image.load(config.avatar[8])
        self.posX_PG1,self.posY_PG1=150,250
        self.seleccionarG1 = boton.Button(150,350,140,40, text = 'GallitoV1')

        self.personajeGallito2 = pygame.image.load(config.avatar[11])
        self.posX_PG2,self.posY_PG2=500,250
        self.seleccionarG2 = boton.Button(500,200,140,40, text = 'GallitoV2')

        self.personajeGallito3 = pygame.image.load(config.avatar[14])
        self.posX_PG3,self.posY_PG3=500,100
        self.seleccionarG3 = boton.Button(500,350,140,40, text = 'GallitoV3')

        self.definitivo = boton.Button(600,450,130,40,text='Seleccionar') #para seleccionar definitivamente
        self.reset = boton.Button(200,450,100,40,text = 'Reset')
        self.atras = boton.Button(200,550,100,40, text = 'Atras')
        self.salir = boton.Button(600,550, 100, 40, text = 'Salir')

        self.situado = True
        self.seleccionado = False #Flag para saber si ya se selecciono un cuy

        self.sesion = sesion.Sesion.get_instance()
        self.personaje = None

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.seleccionarGallito.handle_event(event)
            self.seleccionarG1.handle_event(event)
            self.seleccionarG2.handle_event(event)
            self.seleccionarG3.handle_event(event)

            self.definitivo.handle_event(event)
            self.reset.handle_event(event)
            self.atras.handle_event(event)
            self.salir.handle_event(event)

    def update(self):
        if self.seleccionarG1.active: #si se selecciona la primera version
            self.personajeGallito = self.personajeGallito1 #el personaje cambia a primera version
            self.seleccionado = True #cambiar flag a true
        elif self.seleccionarG2.active:
            self.personajeGallito = self.personajeGallito2
            self.seleccionado = True
        elif self.seleccionarG3.active:
            self.personajeGallito = self.personajeGallito3
            self.seleccionado = True

        if self.definitivo.active and self.seleccionado: #si lo selecciona definitivamente va para la sala.
            self.gestor.pantalla_actual.ir_sala() #solo puede haber un active a la vez.

    def render(self):

        self.ventana.blit(self.fondo,(0,0))

        pygame.draw.rect(self.ventana,(0,100,205),(150,100,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(150,250,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(500,250,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(500,100,150,100))

        self.seleccionarG1.draw(self.ventana)
        self.seleccionarG2.draw(self.ventana)
        self.seleccionarG3.draw(self.ventana)

        self.definitivo.draw(self.ventana)
        self.reset.draw(self.ventana)
        self.atras.draw(self.ventana)
        self.salir.draw(self.ventana)

        if self.situado:

            self.ventana.blit(self.personajeGallito, (self.posX_PG, self.posY_PG))
            self.ventana.blit(self.personajeGallito1, (self.posX_PG1,self.posY_PG1))
            self.ventana.blit(self.personajeGallito2, (self.posX_PG2,self.posY_PG2))
            self.ventana.blit(self.personajeGallito3, (self.posX_PG3,self.posY_PG3))

        if self.reset.active:
            self.personajeGallito = pygame.image.load("Imagenes/Personaje/GallitoOriginal.png") #para que se resetee el personaje
            self.seleccionado = False
        if self.atras.active:
            self.gestor.pantalla_actual.ir_personajes() #si presiona atras va para escoger personajes
        if self.salir.active:
            pygame.quit()
            sys.exit()

        pygame.display.update()

    def ir_sala(self):
        self.sesion.avatar[self.sesion.personaje] = self.personaje
        self.gestor.pantalla_actual = pantalla_sala.PantallaSala(self.gestor)

    def ir_personajes(self):
        self.gestor.pantalla_actual = pantalla_personajes.Personajes(self.gestor)
