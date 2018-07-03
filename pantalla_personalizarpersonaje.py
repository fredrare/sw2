#personalizar personaje TODOS LOS PERSONAJJES EN UNO
#EN PANTALLA VERSIONES (CUY,GALLITO,LLAMA,PERRO) ESTAN SEPARADOS

import pygame, sys, boton
from pygame.locals import *
import pantallas
import pantalla_personajes
import boton
import config

class PantallaPersonalizar(pantallas.PantallaJugador):
    def __init__(self, gestor):
        self.gestor = gestor
        pygame.display.set_caption("personalizarcuy")

        self.fondo = pygame.image.load(config.fondo[0])
        self.postX = 650
        self.postY = 600
        self.ventana = pygame.display.set_mode((800,600))
        pygame.display.set_caption("listapersonalizacion")

        self.personaje = pygame.image.load("Imagenes/Personaje/CuyOriginal.png")#self.gestor.pantalla_personajes(self.elegido)  #que jale al personaje elegido
#Personaje CUY
        self.personajeCuy = pygame.image.load("Imagenes/Personaje/CuyOriginal.png")
        self.posX_PC,self.posY_PC=150,100 #Posicion personaje cuy
        self.seleccionarCuy = boton.Button(150,200,140,40, text = 'CuyBase')

        self.personajeCuy1 = pygame.image.load("Imagenes/Personaje/cuy-v1.png")
        self.posX_PC1,self.posY_PC1=150,250
        self.seleccionarC1 = boton.Button(150,350,140,40, text = 'CuyV1')

        self.personajeCuy2 = pygame.image.load("Imagenes/Personaje/cuy-v2.png")
        self.posX_PC2,self.posY_PC2=500,250
        self.seleccionarC2 = boton.Button(500,350,140,40, text = 'CuyV2')

        self.personajeCuy3 = pygame.image.load("Imagenes/Personaje/cuy-v3.png")
        self.posX_PC3,self.posY_PC3=500,100
        self.seleccionarC3 = boton.Button(500,200,140,40, text = 'CuyV3')

#Personaje GALLITO
        self.personajeGallito = pygame.image.load("Imagenes/Personaje/GallitoOriginal.png")
        self.posX_PG,self.posY_PG=150,100 #Posicion personaje Gallito
        self.seleccionarGallito = boton.Button(150,200,140,40, text = 'GallitoBase')

        self.personajeGallito1 = pygame.image.load("Imagenes/Personaje/Gallito-v1.png")
        self.posX_PG1,self.posY_PG1=150,250
        self.seleccionarG1 = boton.Button(150,350,140,40, text = 'GallitoV1')

        self.personajeGallito2 = pygame.image.load("Imagenes/Personaje/Gallito-v2.png")
        self.posX_PG2,self.posY_PG2=500,250
        self.seleccionarG2 = boton.Button(500,350,140,40, text = 'GallitoV2')

        self.personajeGallito3 = pygame.image.load("Imagenes/Personaje/Gallito-v3.png")
        self.posX_PG3,self.posY_PG3=500,100
        self.seleccionarG3 = boton.Button(500,200,140,40, text = 'GallitoV3')

#Personaje LLAMA
        self.personajeLlama = pygame.image.load("Imagenes/Personaje/LlamaOriginal.png")
        self.posX_PL,self.posY_PL=150,100 #Posicion personaje Llama
        self.seleccionarLlama = boton.Button(150,200,140,40, text = 'LlamaBase')

        self.personajeLlama1 = pygame.image.load("Imagenes/Personaje/Llama-v1.png")
        self.posX_PL1,self.posY_PL1=150,250
        self.seleccionarL1 = boton.Button(150,350,140,40, text = 'LlamaV1')

        self.personajeLlama2 = pygame.image.load("Imagenes/Personaje/Llama-v2.png")
        self.posX_PL2,self.posY_PL2=500,250
        self.seleccionarL2 = boton.Button(500,350,140,40, text = 'LlamaV2')

        self.personajeLlama3 = pygame.image.load("Imagenes/Personaje/Llama-v3.png")
        self.posX_PL3,self.posY_PL3=500,100
        self.seleccionarL3 = boton.Button(500,200,140,40, text = 'LlamaV3')

        self.atras = boton.Button(350,600,100,40, text = 'Atras')
        self.salir = boton.Button(600, 650, 100, 40, text = 'Salir')

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
            self.seleccionarCuy.handle_event(event)
            self.seleccionarC1.handle_event(event)
            self.seleccionarC2.handle_event(event)
            self.seleccionarC3.handle_event(event)

            self.seleccionarGallito.handle_event(event)
            self.seleccionarG1.handle_event(event)
            self.seleccionarG2.handle_event(event)
            self.seleccionarG3.handle_event(event)

            self.seleccionarLlama.handle_event(event)
            self.seleccionarL1.handle_event(event)
            self.seleccionarL2.handle_event(event)
            self.seleccionarL3.handle_event(event)

            self.seleccionarPerro.handle_event(event)
            self.seleccionarP1.handle_event(event)
            self.seleccionarP2.handle_event(event)
            self.seleccionarP3.handle_event(event)

            self.atras.handle_event(event)
            self.salir.handle_event(event)

    def update(self):

        if self.personaje == self.personajeCuy: #pygame.image.load("Imagenes/Personajes/CuyOriginal.png"): #sicuy
            if self.seleccionarC1.active: #si se selecciona la primera version
                self.personajeCuy = self.personalizarCuy1 #el personaje cambia a primera version
                if self.personajeCuy.active:
                    self.gestor.pantalla_actual.ir_juego()
            elif self.seleccionarC2.active:
                self.personajeCuy = self.personalizarCuy2
                if self.personajeCuy.active:
                    self.gestor.pantalla_actual.ir_juego()
            elif self.seleccionarC3.active:
                self.personajeCuy = self.personalizarCuy3
                if self.personajeCuy.active:
                    self.gestor.pantalla_actual.ir_juego()
        elif self.personaje == pygame.image.load("Imagenes/Personaje/GallitoOriginal.png"):#si el personaje es gallo
            if self.seleccionarG1.active:
                self.personajeGallito = self.personalizarGallito1
                if self.personajeGallito.active:
                    self.gestor.pantalla_actual.ir_juego()
            elif self.seleccionarG2.active:
                self.personajeGallito = self.personalizarGallito2
                if self.personajeGallito.active:
                    self.gestor.pantalla_actual.ir_juego()
            elif self.seleccionarG3.active:
                self.personajeGallito = self.personalizarGallito3
                if self.personajeGallito.active:
                    self.gestor.pantalla_actual.ir_juego()
        elif self.personaje == pygame.image.load("Imagenes/Personaje/PerroOriginal.png"): #si el personaje es perro
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
        elif self.personaje == pygame.image.load("Imagenes/Personaje/LlamaOriginal.png"): #si el personaje es Llama
            if self.seleccionarL1.active:
                self.personajeLlama = self.personalizarLlama1
                if self.personajeLlama.active:
                    self.gestor.pantalla_actual.ir_juego()
            elif self.seleccionarL2.active:
                self.personajeLlama = self.personalizarLlama2
                if self.personajeLlama.active:
                    self.gestor.pantalla_actual.ir_juego()
            elif self.seleccionarL3.active:
                self.personajeLlama = self.personalizarLlama3
                if self.personajeLlama.active:
                    self.gestor.pantalla_actual.ir_juego()



    def render(self):

        self.ventana.blit(self.fondo,(0,0))

        pygame.draw.rect(self.ventana,(0,100,205),(150,100,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(150,250,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(500,250,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(500,100,150,100))

        if self.personaje == pygame.image.load("Imagenes/Personaje/CuyOriginal.png"): #si el personaje es cuy
            self.seleccionarC1.draw(self.ventana)
            self.seleccionarC2.draw(self.ventana)
            self.seleccionarC3.draw(self.ventana)
        elif self.personaje == pygame.image.load("Imagenes/Personaje/GallitoOriginal.png"): #si el personaje es gallo
            self.seleccionarG1.draw(self.ventana)
            self.seleccionarG2.draw(self.ventana)
            self.seleccionarG3.draw(self.ventana)
        elif self.personaje == pygame.image.load("Imagenes/Personaje/LlamaOriginal.png"): #si el personaje es Llama
            self.seleccionarL1.draw(self.ventana)
            self.seleccionarL2.draw(self.ventana)
            self.seleccionarL3.draw(self.ventana)
        elif self.personaje == pygame.image.load("Imagenes/Personaje/PerroOriginal.png"): #si el personaje es Perro
            self.seleccionarP1.draw(self.ventana)
            self.seleccionarP2.draw(self.ventana)
            self.seleccionarP3.draw(self.ventana)

        self.atras.draw(self.ventana)
        self.salir.draw(self.ventana)

        if self.situado:
            if self.personaje == pygame.image.load("Imagenes/Personaje/CuyOriginal.png"):
                self.ventana.blit(self.personajeCuy1, (self.posX_PC1, self.posY_PC1))
                self.ventana.blit(self.personajeCuy2, (self.posX_PC2,self.posY_PC2))
                self.ventana.blit(self.personajeCuy3, (self.posX_PC3,self.posY_PC3))
                self.ventana.blit(self.personajeCuy, (self.posX_PC,self.posY_PC))
            elif self.personaje == pygame.image.load("Imagenes/Personaje/GallitoOriginal.png"):
                self.ventana.blit(self.personajeGallito, (self.posX_PG, self.posY_PG))
                self.ventana.blit(self.personajeGallito1, (self.posX_PG1,self.posY_PG1))
                self.ventana.blit(self.personajeGallito2, (self.posX_PG2,self.posY_PG2))
                self.ventana.blit(self.personajeGallito3, (self.posX_PG3,self.posY_PG3))
            elif self.personaje == pygame.image.load("Imagenes/Personaje/LlamaOriginal.png"):
                self.ventana.blit(self.personajeLlama, (self.posX_PL, self.posY_PL))
                self.ventana.blit(self.personajeLlama1, (self.posX_PL1,self.posY_PL1))
                self.ventana.blit(self.personajeLlama2, (self.posX_PL2,self.posY_PL2))
                self.ventana.blit(self.personajeLlama3, (self.posX_PL3,self.posY_PL3))
            elif self.personaje == pygame.image.load("Imagenes/Personaje/PerroOriginal.png"):
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
