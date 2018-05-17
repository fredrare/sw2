import pygame
import pantallas
import text_input
import config
import requests
import pantalla_lobby

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    r = requests.get('http://165.227.76.18:3000/login?username=' +
                                     self.input_usuario.text +
                                     '&password=' +
                                     self.input_password.text)
                    print(self.input_usuario.text)
                    print(self.input_password.text)
                    print(r._content)
                    if r._content == 'true':
                        self.gestor.pantalla_actual.ir_lobby()
                    else:
                        self.input_password.text = ""
                        self.input_usuario.text = ""
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
    def ir_lobby(self):
        self.gestor.pantalla_actual = pantalla_lobby.PantallaLobby(self.gestor)
    def ir_jugador(self):
        pass
    def ir_admin(self):
        pass
