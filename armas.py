import pygame
from disparo import Shot

class Arma:
	def __init__(self, x, y):
		self.posicion = [x,y]
		self.listaDisparos = []

	def mover(self, x):
		self.posicion[0] += x
	def crear_disparo(self, powerup = None):
		disparo = Shot(self.posicion[0], self.posicion[1])
		self.listaDisparos.append(disparo)
	def mover_disparo(self, fondo):
		for disparo in self.listaDisparos:
			disparo.mover()
			self.pintar_disparo(fondo);
	def eliminar_disparo(self):
		pass
	def pintar_disparo(self, fondo):
		for disparo in self.listaDisparos:
			disparo.pintar(fondo)
