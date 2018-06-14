import pygame, sys, boton
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((800,800))
pygame.display.set_caption("listapersonajes")
fondo = pygame.image.load("Imagenes/peru.jpg")
postX = 650
postY = 600


personaje1 = pygame.image.load("Imagenes/Otorongo.png")
posX_P1,posY_P1=150,100
personaje2 = pygame.image.load("Imagenes/Llamita2.png")
posX_P2,posY_P2=150,250
personaje3 = pygame.image.load("Imagenes/aguila.png")
posX_P3,posY_P3=150,400
personaje4 = pygame.image.load("Imagenes/cuy.png")
posX_P4,posY_P4=500,100
personaje5 = pygame.image.load("Imagenes/gallitorocas.png")
posX_P5,posY_P5=500,250
personaje6 = pygame.image.load("Imagenes/perroperuano.png")
posX_P6,posY_P6=500,400
situado = True
seleccionado = False

seleccionar = boton.Button(200,550,140,40, text = 'Seleccionar')
atras = boton.Button(500,550,100,40, text = 'Atras')
salir = boton.Button(600, 650, 100, 40, text = 'Salir')


while True:
    ventana.blit(fondo,(0,0))

    pygame.draw.rect(ventana,(0,100,205),(150,100,150,100))
    pygame.draw.rect(ventana,(210,40,50),(150,250,150,100))
    pygame.draw.rect(ventana,(0,100,205),(150,400,150,100))
    pygame.draw.rect(ventana,(210,40,50),(500,100,150,100))
    pygame.draw.rect(ventana,(0,100,205),(500,250,150,100))
    pygame.draw.rect(ventana,(210,40,50),(500,400,150,100))
    seleccionar.draw(ventana)
    atras.draw(ventana)
    salir.draw(ventana)

    if situado:
        ventana.blit(personaje1, (posX_P1, posY_P1))
        ventana.blit(personaje2, (posX_P2,posY_P2))
        ventana.blit(personaje3, (posX_P3,posY_P3))
        ventana.blit(personaje4, (posX_P4,posY_P4))
        ventana.blit(personaje5, (posX_P5,posY_P5))
        ventana.blit(personaje6, (posX_P6,posY_P6))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        seleccionar.handle_event(event)
        atras.handle_event(event)
        salir.handle_event(event)
    if seleccionar.active:
        pantalla_actual.ir_lobby()
    if atras.active:
        pantalla_actual.ir_jugador()
    if salir.active:
        pygame.quit()
        sys.exit()

    pygame.display.update()
