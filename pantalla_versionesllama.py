#personalizar Llama
import pygame, sys, boton
from pygame.locals import *
import pantallas
import pantalla_personajes
import boton
import config
import pantalla_sala

class Llama(pantallas.PantallaJugador):
    def __init__(self, gestor):
        self.gestor = gestor
        pygame.display.set_caption("personalizarllama")

        self.fondo = pygame.image.load(config.fondo[0])
        self.postX = 650
        self.postY = 600
        self.ventana = pygame.display.set_mode((800,600))
        pygame.display.set_caption("listapersonalizacion")

        self.personajeLlama = pygame.image.load("Imagenes/Personaje/LlamaOriginal.png")
        self.posX_PL,self.posY_PL=150,100 #Posicion personaje Llama
        self.seleccionarLlama = boton.Button(150,200,140,40, text = 'LlamaBase')

        self.personajeLlama1 = pygame.image.load("Imagenes/Personaje/Llama-v1.png")
        self.posX_PL1,self.posY_PL1=150,250
        self.seleccionarL1 = boton.Button(150,350,140,40, text = 'LlamaV1')

        self.personajeLlama2 = pygame.image.load("Imagenes/Personaje/Llama-v2.png")
        self.posX_PL2,self.posY_PL2=500,100
        self.seleccionarL2 = boton.Button(500,200,140,40, text = 'LlamaV2')

        self.personajeLlama3 = pygame.image.load("Imagenes/Personaje/Llama-v3.png")
        self.posX_PL3,self.posY_PL3=500,250
        self.seleccionarL3 = boton.Button(500,350,140,40, text = 'LlamaV3')

        self.definitivo = boton.Button(600,450,130,40,text='Seleccionar') #para seleccionar definitivamente
        self.reset = boton.Button(200,450,100,40,text = 'Reset')
        self.atras = boton.Button(200,550,100,40, text = 'Atras')
        self.salir = boton.Button(600,550, 100, 40, text = 'Salir')

        self.situado = True
        self.seleccionado = False #flag

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.seleccionarLlama.handle_event(event)
            self.seleccionarL1.handle_event(event)
            self.seleccionarL2.handle_event(event)
            self.seleccionarL3.handle_event(event)

            self.definitivo.handle_event(event)
            self.reset.handle_event(event)
            self.atras.handle_event(event)
            self.salir.handle_event(event)

    def update(self):
        if self.seleccionarL1.active:
            self.personajeLlama = self.personajeLlama1
            self.seleccionado = True
        elif self.seleccionarL2.active:
            self.personajeLlama = self.personajeLlama2
            self.seleccionado = True
        elif self.seleccionarL3.active:
            self.personajeLlama = self.personajeLlama3
            self.seleccionado = True

        if self.definitivo.active: #si lo selecciona definitivamente va para la sala.
            self.gestor.pantalla_actual.ir_sala()

    def render(self):

        self.ventana.blit(self.fondo,(0,0))

        pygame.draw.rect(self.ventana,(0,100,205),(150,100,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(150,250,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(500,250,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(500,100,150,100))

        self.seleccionarL1.draw(self.ventana)
        self.seleccionarL2.draw(self.ventana)
        self.seleccionarL3.draw(self.ventana)

        self.definitivo.draw(self.ventana)
        self.reset.draw(self.ventana)
        self.atras.draw(self.ventana)
        self.salir.draw(self.ventana)

        if self.situado:
            self.ventana.blit(self.personajeLlama, (self.posX_PL, self.posY_PL))
            self.ventana.blit(self.personajeLlama1, (self.posX_PL1,self.posY_PL1))
            self.ventana.blit(self.personajeLlama2, (self.posX_PL2,self.posY_PL2))
            self.ventana.blit(self.personajeLlama3, (self.posX_PL3,self.posY_PL3))

        if self.reset.active:
            self.personajeLlama = pygame.image.load("Imagenes/Personaje/LlamaOriginal.png") #para que se resetee el personaje
            self.seleccionado = False
        if self.atras.active:
            self.gestor.pantalla_actual.ir_personajes() #si presiona atras va para escoger personajes
        if self.salir.active:
            pygame.quit()
            sys.exit()

        pygame.display.update()

    def ir_sala(self):
        self.gestor.personajeJugador1 = self.personajeLlama #poner personaje como el personaje del jugador 1
        self.gestor.pantalla_actual = pantalla_sala.PantallaSala(self.gestor)

    def ir_personajes(self):
        self.gestor.pantalla_actual = pantalla_personajes.Personajes(self.gestor)
