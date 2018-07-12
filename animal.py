import pygame
from armas import Arma

class Llama:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.arma = Arma(x,y)
		self.powerup = None
		self.sprite = pygame.image.load('llamita.png')
		self.sprite.set_colorkey((0,0,0))

	def mover(self, cambio):
		self.x += cambio
		self.arma.mover(cambio)

	def getPosicion(self):
		return (self.x, self.y)

	def disparar(self):
		self.arma.crear_disparo(self.powerup)

	def pintarLlama(self, fondo):
		fondo.blit(self.sprite, (self.x, self.y))