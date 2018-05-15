# Importar módulos de pantallas y más
import pygame

# Definir métodos

# Definir constantes
ancho = 700
alto = 700
dimensiones = (ancho, alto)
# Definir clases
def GestorPantallas:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode(dimensiones)
        self.superficie = pygame.Surface(self.pantalla.get_size())
        self.pantalla_actual = pantallas.Pantalla(self)

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

