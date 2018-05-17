import pygame
import os
from animal import Llama
from disparo import Shot


pygame.init()

SCREEN_ANCHO = 800
SCREEN_ALTO = 600
SCREEN = pygame.display.set_mode((SCREEN_ANCHO, SCREEN_ALTO))
NEGRO = (0,0,0)
BLANCO = (255,255,255)

POSICION = [300,50]

def main():
	llama = Llama(POSICION[0], POSICION[1])
	os.environ['SDL_VIDEO_WINDOW_POS'] = (str(POSICION[0]) + "," + str(POSICION[1]))
	SCREEN.fill(NEGRO)
	llama.pintarLlama(SCREEN)
	pygame.display.flip()
	input()	

main()