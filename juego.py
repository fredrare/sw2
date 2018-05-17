# -*- coding: utf-8 -*-
# Importar módulos de pantallas y más
import pygame
import pantalla_login
import config

# Definir métodos

# Definir constantes
dimensiones = (config.ANCHO, config.ALTO)
# Definir clases
class GestorPantallas:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode(dimensiones)
        self.superficie = pygame.Surface(self.pantalla.get_size())
        self.pantalla_actual = pantalla_login.PantallaLogin(self)

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

