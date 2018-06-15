import pygame 

class Shot:
	def __init__(self,x,y):
		self.posicion = [x,y]
		self.velocidad = -5
		self.sprite = pygame.image.load('bullet.gif').convert()
	def mover(self):
		self.posicion[1] += self.velocidad
	def getposicion(self):
		return self.posicion
	def pintar(self, fondo):
		fondo.blit(self.sprite, (self.posicion[0], self.posicion[1]))