# -*- coding: utf-8 -*-
# Importar módulos de pantallas y más
import pygame
import config
<<<<<<< HEAD
import pantalla_sala

=======
import pantalla_registro
#import pantalla_personajes
>>>>>>> 2457de70467621a4e2560f9eb261f8dcf66342ea
# Definir métodos

# Definir constantes
dimensiones = (config.ANCHO, config.ALTO)
# Definir clases
class GestorPantallas:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode(dimensiones)
        self.superficie = pygame.Surface(self.pantalla.get_size())
<<<<<<< HEAD
        self.pantalla_actual = pantalla_sala.PantallaSala(self)
=======
        self.pantalla_actual = pantalla_registro.PantallaRegistro(self)
>>>>>>> 2457de70467621a4e2560f9eb261f8dcf66342ea

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
