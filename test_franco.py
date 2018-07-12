# -*- coding: utf-8 -*-
# Importar módulos de pantallas y más
import pygame
import config
import bala
import random
# Definir métodos

# Definir constantes
dimensiones = (config.ANCHO, config.ALTO)
# Definir clases

class GestorPantallas:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode(dimensiones)
        self.superficie = pygame.Surface(self.pantalla.get_size())
<<<<<<< HEAD:test_franco.py
        self.pantalla_actual = bala.Bala(self)
=======
        self.pantalla_actual = bala.Bala(self,random.randint(0,config.ANCHO),config.ALTO)
>>>>>>> ec347ad4fcdf3d822d9a7f0c78eb5a8bc4844326:test.py

    def comenzar(self):
        while True:
            # Obtener la entrada
            self.pantalla_actual.get_input()
            # Actualizar los datos
            self.pantalla_actual.update()
            # Render
            self.pantalla_actual.render()

# Definir main
def main():
    gestorPantallas = GestorPantallas()
    gestorPantallas.comenzar()

if __name__ == '__main__':
    main()
