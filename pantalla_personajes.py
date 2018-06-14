import pygame, sys, boton
from pygame.locals import *
import pantallas



class Personajes(pantallas.PantallaJugador):
    def __init__(self):
    pygame.init()
    fondo = pygame.image.load("Imagenes/peru.jpg")
    postX = 650
    postY = 600
    ventana = pygame.display.set_mode((800,800))
    pygame.display.set_caption("listapersonajes")

    pantalla_actual = pantalla_personajes.Personajes(self.gestor)

    personaje1 = pygame.image.load("Imagenes/Otorongo.png")
    posX_P1,posY_P1=150,100
    seleccionar1 = boton.Button(150,200,140,40, text = 'Otorongo')

    personaje2 = pygame.image.load("Imagenes/Llamita2.png")
    posX_P2,posY_P2=150,250
    seleccionar2 = boton.Button(150,350,140,40, text = 'Llama')

    personaje3 = pygame.image.load("Imagenes/aguila.png")
    posX_P3,posY_P3=150,400
    seleccionar3 = boton.Button(150,500,140,40, text = 'Aguila')

    personaje4 = pygame.image.load("Imagenes/cuy.png")
    posX_P4,posY_P4=500,100
    seleccionar4 = boton.Button(500,200,140,40, text = 'Cuy')

    personaje5 = pygame.image.load("Imagenes/gallitorocas.png")
    posX_P5,posY_P5=500,250
    seleccionar5 = boton.Button(500,350,140,40, text = 'Gallito')

    personaje6 = pygame.image.load("Imagenes/perroperuano.png")
    posX_P6,posY_P6=500,400
    seleccionar6 = boton.Button(500,500,140,40, text = 'Perro')

    atras = boton.Button(350,600,100,40, text = 'Atras')
    salir = boton.Button(600, 650, 100, 40, text = 'Salir')

    situado = True
    seleccionado = False

    while True:
        ventana.blit(fondo,(0,0))

        pygame.draw.rect(ventana,(0,100,205),(150,100,150,100))
        pygame.draw.rect(ventana,(210,40,50),(150,250,150,100))
        pygame.draw.rect(ventana,(0,100,205),(150,400,150,100))
        pygame.draw.rect(ventana,(210,40,50),(500,100,150,100))
        pygame.draw.rect(ventana,(0,100,205),(500,250,150,100))
        pygame.draw.rect(ventana,(210,40,50),(500,400,150,100))
        seleccionar1.draw(ventana)
        seleccionar2.draw(ventana)
        seleccionar3.draw(ventana)
        seleccionar4.draw(ventana)
        seleccionar5.draw(ventana)
        seleccionar6.draw(ventana)
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
            seleccionar1.handle_event(event)
            seleccionar2.handle_event(event)
            seleccionar3.handle_event(event)
            seleccionar4.handle_event(event)
            seleccionar5.handle_event(event)
            seleccionar6.handle_event(event)

            atras.handle_event(event)
            salir.handle_event(event)


        if seleccionar1.active:
            pantalla_actual.ir_sala()
        else:
            if seleccionar2.active:
                pantalla_actual.ir_sala()
            else:
                if seleccionar3.active:
                    pantalla_actual.ir_sala()
                else:
                    if seleccionar4.active:
                        pantalla_actual.ir_sala()
                    else:
                        if seleccionar5.active:
                            pantalla_actual.ir_sala()
                        else:
                            if seleccionar6.active:
                                pantalla_actual.ir_sala()

        if atras.active:
            gestor.pantalla_actual.ir_lobby() #si presiona atras va para el lobby
        if salir.active:
            pygame.quit()
            sys.exit()

        pygame.display.update()

    def ir_sala(self):
        print("Se va a la sala")
        pass
