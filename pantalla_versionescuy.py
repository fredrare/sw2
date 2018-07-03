#pantalla cuy versiones
import pygame, sys, boton
from pygame.locals import *
import pantallas
import pantalla_personajes
import boton
import config
import pantalla_sala
import sesion

class Cuy(pantallas.PantallaJugador):
    def __init__(self, gestor):
        self.gestor = gestor
        pygame.display.set_caption("personalizarcuy")

        self.fondo = pygame.image.load(config.fondo[0])
        self.postX = 650
        self.postY = 600
        self.ventana = pygame.display.set_mode((800,600))
        pygame.display.set_caption("listacuy")

#Personaje CUY
        self.personajeCuy = pygame.image.load("Imagenes/Personaje/CuyOriginal.png")
        self.posX_PC,self.posY_PC=150,100 #Posicion personaje cuy
        self.seleccionarCuy = boton.Button(150,200,140,40, text = 'CuyBase')

        self.personajeCuy1 = pygame.image.load("Imagenes/Personaje/cuy-v1.png")
        self.posX_PC1,self.posY_PC1=150,250
        self.seleccionarC1 = boton.Button(150,350,140,40, text = 'CuyV1')

        self.personajeCuy2 = pygame.image.load("Imagenes/Personaje/cuy-v2.png")
        self.posX_PC2,self.posY_PC2=500,100
        self.seleccionarC2 = boton.Button(500,200,140,40, text = 'CuyV2')

        self.personajeCuy3 = pygame.image.load("Imagenes/Personaje/cuy-v3.png")
        self.posX_PC3,self.posY_PC3=500,250
        self.seleccionarC3 = boton.Button(500,350,140,40, text = 'CuyV3')

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
            self.seleccionarCuy.handle_event(event)
            self.seleccionarC1.handle_event(event)
            self.seleccionarC2.handle_event(event)
            self.seleccionarC3.handle_event(event)

            self.definitivo.handle_event(event)
            self.reset.handle_event(event)
            self.atras.handle_event(event)
            self.salir.handle_event(event)

    def update(self):  #CAMBIA ESTO!
        if self.seleccionarC1.active: #si se selecciona la primera version
            self.personajeCuy = self.personajeCuy1 #el personaje cambia a primera version
            self.seleccionado = True
        elif self.seleccionarC2.active:
            self.personajeCuy = self.personajeCuy2
            self.seleccionado = True
        elif self.seleccionarC3.active:
            self.personajeCuy = self.personajeCuy3
            self.seleccionado = True

        if self.definitivo.active and self.seleccionado: #si lo selecciona definitivamente va para la sala.
            self.gestor.pantalla_actual.ir_sala()

    def render(self):

        self.ventana.blit(self.fondo,(0,0))

        pygame.draw.rect(self.ventana,(0,100,205),(150,100,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(150,250,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(500,250,150,100))
        pygame.draw.rect(self.ventana,(210,40,50),(500,100,150,100))

        self.seleccionarC1.draw(self.ventana)
        self.seleccionarC2.draw(self.ventana)
        self.seleccionarC3.draw(self.ventana)

        self.definitivo.draw(self.ventana)
        self.reset.draw(self.ventana)
        self.atras.draw(self.ventana)
        self.salir.draw(self.ventana)

        if self.situado:
            self.ventana.blit(self.personajeCuy1, (self.posX_PC1, self.posY_PC1))
            self.ventana.blit(self.personajeCuy2, (self.posX_PC2,self.posY_PC2))
            self.ventana.blit(self.personajeCuy3, (self.posX_PC3,self.posY_PC3))
            self.ventana.blit(self.personajeCuy, (self.posX_PC,self.posY_PC))

        if self.reset.active:
            self.personajeCuy = pygame.image.load("Imagenes/Personaje/CuyOriginal.png") #para que se resetee el personaje
            self.seleccionado = False
        if self.atras.active:
            self.gestor.pantalla_actual.ir_personajes() #si presiona atras va para escoger personajes
        if self.salir.active:
            pygame.quit()
            sys.exit()

        pygame.display.update()

    def ir_sala(self):
        self.sesion.avatar[self.sesion.personaje] = self.personaje #poner personaje como el personaje del jugador 1
        self.gestor.pantalla_actual = pantalla_sala.PantallaSala(self.gestor)

    def ir_personajes(self):
        self.gestor.pantalla_actual = pantalla_personajes.Personajes(self.gestor)
