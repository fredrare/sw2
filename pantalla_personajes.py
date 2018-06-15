import pygame, sys, boton
from pygame.locals import *
import pantallas
import pantalla_sala
#import pantalla_lobby
#import boton

class Personajes(pantallas.PantallaJugador):
    def __init__(self, gestor):
        self.gestor = gestor
        pygame.display.set_caption("lobby")

        self.fondo = pygame.image.load("Imagenes/peru.jpg")
        self.postX = 650
        self.postY = 600
        self.ventana = pygame.display.set_mode((800,800))
        pygame.display.set_caption("listapersonajes")

        self.personaje1 = pygame.image.load("Imagenes/Otorongo.png")
        self.posX_P1,self.posY_P1=150,100
        self.seleccionar1 = boton.Button(150,200,140,40, text = 'Otorongo')

        self.personaje2 = pygame.image.load("Imagenes/Llamita2.png")
        self.posX_P2,self.posY_P2=150,250
        self.seleccionar2 = boton.Button(150,350,140,40, text = 'Llama')

        self.personaje3 = pygame.image.load("Imagenes/aguila.png")
        self.posX_P3,self.posY_P3=150,400
        self.seleccionar3 = boton.Button(150,500,140,40, text = 'Aguila')

        self.personaje4 = pygame.image.load("Imagenes/cuy.png")
        self.posX_P4,self.posY_P4=500,100
        self.seleccionar4 = boton.Button(500,200,140,40, text = 'Cuy')

        self.personaje5 = pygame.image.load("Imagenes/gallitorocas.png")
        self.posX_P5,self.posY_P5=500,250
        self.seleccionar5 = boton.Button(500,350,140,40, text = 'Gallito')

        self.personaje6 = pygame.image.load("Imagenes/perroperuano.png")
        self.posX_P6,self.posY_P6=500,400
        self.seleccionar6 = boton.Button(500,500,140,40, text = 'Perro')

        self.atras = boton.Button(350,600,100,40, text = 'Atras')
        self.salir = boton.Button(600, 650, 100, 40, text = 'Salir')

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
            self.seleccionar5.handle_event(event)
            self.seleccionar6.handle_event(event)

            self.atras.handle_event(event)
            self.salir.handle_event(event)

    def update(self):
        if self.seleccionar1.active:
            self.gestor.pantalla_actual.ir_sala()
        elif self.seleccionar2.active:
            self.gestor.pantalla_actual.ir_sala()
        elif self.seleccionar3.active:
            self.gestor.pantalla_actual.ir_sala()
        elif self.seleccionar4.active:
            self.gestor.pantalla_actual.ir_sala()
        elif self.seleccionar5.active:
            self.gestor.pantalla_actual.ir_sala()
        elif self.seleccionar6.active:
            self.gestor.pantalla_actual.ir_sala()

    def render(self):

        self.ventana.blit(self.fondo,(0,0))

        pygame.draw.rect(self.ventana,(0,100,205),(150,100,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(150,250,150,100))
        pygame.draw.rect(self.ventana,(0,100,205),(150,400,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(500,100,150,100))
        pygame.draw.rect(self.ventana,(0,100,205),(500,250,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(500,400,150,100))
        self.seleccionar1.draw(self.ventana)
        self.seleccionar2.draw(self.ventana)
        self.seleccionar3.draw(self.ventana)
        self.seleccionar4.draw(self.ventana)
        self.seleccionar5.draw(self.ventana)
        self.seleccionar6.draw(self.ventana)
        self.atras.draw(self.ventana)
        self.salir.draw(self.ventana)

        if self.situado:
            self.ventana.blit(self.personaje1, (self.posX_P1, self.posY_P1))
            self.ventana.blit(self.personaje2, (self.posX_P2,self.posY_P2))
            self.ventana.blit(self.personaje3, (self.posX_P3,self.posY_P3))
            self.ventana.blit(self.personaje4, (self.posX_P4,self.posY_P4))
            self.ventana.blit(self.personaje5, (self.posX_P5,self.posY_P5))
            self.ventana.blit(self.personaje6, (self.posX_P6,self.posY_P6))

        if self.atras.active:
            self.gestor.pantalla_actual.ir_lobby() #si presiona atras va para el lobby
        if self.salir.active:
            pygame.quit()
            sys.exit()

        pygame.display.update()

    def ir_sala(self):
        self.gestor.pantalla_actual = pantalla_sala.PantallaSala(self.gestor)
        pass
    #def ir_lobby(self):
        #self.gestor.pantalla_actual = pantalla_lobby.PantallaLobby(self.gestor)
