import pygame
import pantallas
import text_input

background = (128, 128, 128)

class PantallaLogin(pantallas.Pantalla):
    input_usuario = text_input.InputBox(100, 100, 140, 32)
    def get_input(self):
        for event in pygame.event.get():
            self.input_usuario.handle_event(event)
    def update(self):
        self.input_usuario.update()
    def render(self):
        self.gestor.superficie.fill(background)
        self.gestor.pantalla.blit(self.gestor.superficie, (0,0))
        self.input_usuario.draw(self.gestor.pantalla)
        pygame.display.update()
    def ir_jugador(self):
        pass
    def ir_admin(self):
        pass
