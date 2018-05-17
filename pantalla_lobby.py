import pygame,sys,boton

from pygame.locals import *


pygame.init()
ventana = pygame.display.set_mode((800,800))
pygame.display.set_caption("lobby")

fondo = pygame.image.load("Imagenes/peru.jpg")





imagen_Otorongo = pygame.image.load("Imagenes/otorongo.png").convert_alpha()
posX_Oto,posY_Oto = 150,100
is_ready = False
derecha = True
dere = True
imagen_ready = pygame.image.load("Imagenes/ready.png")
imagen_peru = pygame.image.load("Imagenes/peru.png")
postX = 650
postY = 600
cambiar_Equipo = boton.Button(400, 550, 100, 40, text = 'Cambiar')
ready = boton.Button(300, 550, 100, 40, text = 'Ready')
iniciar = boton.Button(360, 500, 100, 40, text = 'Iniciar')
salir = boton.Button(650, 650, 100, 40, text = 'Salir')
velocidad = 2

while True:
    ventana.blit(fondo,(0,0))
    pygame.draw.rect(ventana,(130,70,70),(150,100,150,100))
    pygame.draw.rect(ventana,(130,70,70),(150,250,150,100))
    pygame.draw.rect(ventana,(130,70,70),(150,400,150,100))
    pygame.draw.rect(ventana,(130,70,70),(500,100,150,100))
    pygame.draw.rect(ventana,(130,70,70),(500,250,150,100))
    pygame.draw.rect(ventana,(130,70,70),(500,400,150,100))
    cambiar_Equipo.draw(ventana)
    ready.draw(ventana)
    salir.draw(ventana)
    ventana.blit(imagen_peru,(postX,postY))
    if derecha:
        ventana.blit(imagen_Otorongo, (posX_Oto, posY_Oto))
    else:
        ventana.blit(pygame.transform.flip(imagen_Otorongo, True, False),(550, 100))
    if is_ready:
        ventana.blit(imagen_ready,(330,200))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        cambiar_Equipo.handle_event(event)
        ready.handle_event(event)
        salir.handle_event(event)
    if cambiar_Equipo.active:
        derecha = not derecha
        ventana.blit(imagen_Otorongo,(posX_Oto,posY_Oto))
        cambiar_Equipo.active = False
    if ready.active:
        is_ready = not is_ready
        ready.active = False
    if salir.active:
        pygame.quit()
        sys.exit()
    if dere == True:
        if postX<800:
                postX+=velocidad
        else:
            dere = False
    else:
        if postX>1:
            postX-=velocidad
        else:
            dere = True
    pygame.display.update()
