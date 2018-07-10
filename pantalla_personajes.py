import pygame, sys
from pygame.locals import *
import pantallas
import pantalla_sala
import pantalla_versionescuy
import pantalla_versionesllama
import pantalla_versionesperro
import pantalla_versionesgallito
import boton
import config

class Personajes(pantallas.PantallaJugador):
    def __init__(self, gestor):

        self.gestor = gestor
        pygame.display.set_caption("escogerpersonaje")

        self.fondo = pygame.image.load(config.fondo[0])
        self.postX = 650
        self.postY = 600
        self.ventana = pygame.display.set_mode((800,600))
        pygame.display.set_caption("listapersonajes")

        self.elegido = pygame.image.load("Imagenes/peru.jpg")#iniciar con ninguno default peru

        self.personaje1 = pygame.image.load(config.avatar['c0'])
        self.posX_P1,self.posY_P1=150,100
        self.seleccionar1 = boton.Button(150,200,140,40, text = 'Cuy')

        self.personaje2 = pygame.image.load(config.avatar['g0'])
        self.posX_P2,self.posY_P2=150,250
        self.seleccionar2 = boton.Button(150,350,140,40, text = 'Gallito')

        self.personaje3 = pygame.image.load(config.avatar['l0'])
        self.posX_P3,self.posY_P3=500,250
        self.seleccionar3 = boton.Button(500,350,140,40, text = 'Llama')

        self.personaje4 = pygame.image.load(config.avatar['p0'])
        self.posX_P4,self.posY_P4=500,100
        self.seleccionar4 = boton.Button(500,200,140,40, text = 'Perro')

        self.atras = boton.Button(200,500,100,40, text = 'Atras')
        self.salir = boton.Button(600,500, 100, 40, text = 'Salir')

        self.situado = True
        self.seleccionado = False

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.seleccionar1.handle_event(event)
            self.seleccionar2.handle_event(event)
            self.seleccionar3.handle_event(event)
            self.seleccionar4.handle_event(event)

            self.atras.handle_event(event)
            self.salir.handle_event(event)

#va a personalizar
    def update(self):
        if self.seleccionar1.active:
            self.elegido = self.personaje1 #el cuy se vuelve el elegido
            self.gestor.pantalla_actual.ir_personalizarcuy() #SE REDIRIGE A LA PAGINA SOLO DE VERSIONES DE CUY
        elif self.seleccionar2.active:
            self.elegido = self.personaje2
            self.gestor.pantalla_actual.ir_personalizargallito() #SOLO DE GALLITOS
        elif self.seleccionar3.active:
            self.elegido = self.personaje3
            self.gestor.pantalla_actual.ir_personalizarllama() #SOLO DE LLAMAS
        elif self.seleccionar4.active:
            self.elegido = self.personaje4
            self.gestor.pantalla_actual.ir_personalizarperro() #SOLO DE PERROS

    def render(self):

        self.ventana.blit(self.fondo,(0,0))

        pygame.draw.rect(self.ventana,(0,100,205),(150,100,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(150,250,150,100))
        pygame.draw.rect(self.ventana,(0,100,205),(500,250,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(500,100,150,100))

        self.seleccionar1.draw(self.ventana)
        self.seleccionar2.draw(self.ventana)
        self.seleccionar3.draw(self.ventana)
        self.seleccionar4.draw(self.ventana)

        self.atras.draw(self.ventana)
        self.salir.draw(self.ventana)

        if self.situado:
            self.ventana.blit(self.personaje1, (self.posX_P1, self.posY_P1))
            self.ventana.blit(self.personaje2, (self.posX_P2,self.posY_P2))
            self.ventana.blit(self.personaje3, (self.posX_P3,self.posY_P3))
            self.ventana.blit(self.personaje4, (self.posX_P4,self.posY_P4))

        if self.atras.active:
            self.gestor.pantalla_actual.ir_sala() #si presiona atras va para el lobby
        if self.salir.active:
            pygame.quit()
            sys.exit()

        pygame.display.update()

    def ir_personalizarcuy(self):
        self.gestor.pantalla_actual = pantalla_versionescuy.Cuy(self.gestor)

    def ir_personalizarllama(self):
        self.gestor.pantalla_actual = pantalla_versionesllama.Llama(self.gestor)

    def ir_personalizargallito(self):
        self.gestor.pantalla_actual = pantalla_versionesgallito.Gallo(self.gestor)

    def ir_personalizarperro(self):
        self.gestor.pantalla_actual = pantalla_versionesperro.Perro(self.gestor)

    def ir_sala(self):
        self.gestor.pantalla_actual = pantalla.sala.PantallaSala(self)



        #self.gestor.pantalla_actual = pantalla_lobby.PantallaLobby(self.gestor)
