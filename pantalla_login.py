import pygame
import pantallas
import text_input
import config

class PantallaLogin(pantallas.Pantalla):
    input_usuario = text_input.InputBox(
            (config.ANCHO - config.text_input_ancho) / 2,
            300,
            config.text_input_ancho,
            config.text_input_alto)
    input_password = text_input.InputBox(
            (config.ANCHO - config.text_input_ancho) / 2,
            500,
            config.text_input_ancho,
            config.text_input_alto)
    def get_input(self):
        for event in pygame.event.get():
            self.input_usuario.handle_event(event)
            self.input_password.handle_event(event)
    def update(self):
        self.input_usuario.update()
        self.input_password.update()
    def render(self):
        self.gestor.superficie.fill(config.BACKGROUND_COLOR)
        self.gestor.pantalla.blit(self.gestor.superficie, (0,0))
        self.input_usuario.draw(self.gestor.pantalla)
        self.input_password.draw(self.gestor.pantalla)
        pygame.display.update()
    def ir_jugador(self):
        pass
    def ir_admin(self):
        pass
