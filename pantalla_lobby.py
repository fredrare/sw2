import pygame,sys
from pygame.locals import *


pygame.init()
ventana = pygame.display.set_mode((700,700))
pygame.display.set_caption("lobby")

fondo = pygame.image.load("Imagenes/peru.jpg")
ventana.blit(fondo,(0,0))
pygame.draw.rect(ventana,(130,70,70),(100,100,150,100))
pygame.draw.rect(ventana,(130,70,70),(100,250,150,100))
pygame.draw.rect(ventana,(130,70,70),(100,400,150,100))
pygame.draw.rect(ventana,(130,70,70),(450,100,150,100))
pygame.draw.rect(ventana,(130,70,70),(450,250,150,100))
pygame.draw.rect(ventana,(130,70,70),(450,400,150,100))



imagen_Otorongo = pygame.image.load("Imagenes/otorongo.png").convert_alpha()
posX_Oto,posY_Oto = 100,100
ventana.blit(imagen_Otorongo,(posX_Oto,posY_Oto))
imagen_Llamita = pygame.image.load("Imagenes/Llamita2.png").convert_alpha()
posX_Lla,posY_Lla = 100,250
ventana.blit(imagen_Llamita,(posX_Lla,posY_Lla))



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
