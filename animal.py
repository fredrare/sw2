import pygame
from armas import Arma

class Llama:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.arma = Arma(x,y)
		self.powerup = None
		self.sprite = pygame.image.load('llamita.png')

	def mover(self, cambio):
		self.x += cambio

	def getPosicion(self):
		return (self.x, self.y)

	def disparar(self):
		self.canon.crear_disparo(self.powerup)

	def pintarLlama(self, screen):
		screen.blit(self.sprite, (self.x, self.y))