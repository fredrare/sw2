import pygame
import os
from animal import Llama

pygame.init()

SCREEN_ANCHO = 800
SCREEN_ALTO = 600
SCREEN = pygame.display.set_mode((SCREEN_ANCHO, SCREEN_ALTO))
NEGRO = (0,0,0)
BLANCO = (255,255,255)
FONDO = pygame.Surface(SCREEN.get_size())
POSICION = [300,450]
FPS = 60
def main():
	juego = True
	llama = Llama(POSICION[0], POSICION[1])
	os.environ['SDL_VIDEO_WINDOW_POS'] = (str(POSICION[0]) + "," + str(POSICION[1]))
	cambio = 0
	movimiento = None
	disparar = None
	reloj = pygame.time.Clock()
	while juego:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_LEFT:					
					movimiento = 'izquierda'
				elif evento.key == pygame.K_RIGHT:					
					movimiento = 'derecha'
				elif evento.key == pygame.K_LEFT and evento.key == pygame.K_RIGHT:
					movimiento = None
				elif evento.key == pygame.K_SPACE:
					disparar = True
			elif evento.type == pygame.KEYUP:
				if evento.key == pygame.K_LEFT:					
					movimiento = None
				elif evento.key == pygame.K_RIGHT:					
					movimiento = None
				elif evento.key == pygame.K_SPACE:
					disparar = False


		if movimiento == 'izquierda':
			cambio = -5
		elif movimiento == 'derecha':
			cambio = 5
		else:
			cambio = 0
		if disparar == True:
			llama.disparar()

			
		llama.mover(cambio)
		FONDO.fill(NEGRO)
		llama.pintarLlama(FONDO)
		llama.arma.mover_disparo(FONDO)

		SCREEN.blit(FONDO, (0,0))
		reloj.tick(FPS)
		pygame.display.flip()
	
	input()	

main()