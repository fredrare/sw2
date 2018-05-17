import pygame
from disparo import Shot

class Arma:
	def __init__(self, x, y):
		self.posicion = [x,y]
		self.listaDisparos = []
	def mover(self, cambio):
		self.posicion[0] += x
	def crear_disparo(self, powerup):
		shot = None
		self.listaDisparos.append(shot)
	def mover_disparo(self):
		for shot in self.listaDisparos:
			pass
	def eliminar_disparo(self):
		pass
	def pintar_disparo(self):
		for shot in self.listaDisparos:
			pass
