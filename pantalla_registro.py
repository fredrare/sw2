import pygame
import pantallas
import text_input
import config
import requests
import pantalla_lobby

class PantallaRegistro(pantallas.PantallaJugador):
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
    input_passwordconfirm = text_input.InputBox(
            (config.ANCHO - config.text_input_ancho) / 2,
            500,
            config.text_input_ancho,
            config.text_input_alto)
    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.input_password == self.input_passwordconfirm:
                        r = requests.get('http://165.227.76.18:3000/registrar?username=' +
                                         self.input_usuario.text +
                                         '&password=' +
                                         self.input_password.text)
                        print(self.input_usuario.text)
                        print(self.input_password.text)
                        print(r._content)
                        if r._content == 'true':
                            self.gestor.pantalla_actual.ir_login()
                        else:
                            self.input_password.text = ""
                            self.input_passwordconfirm.text = ""
                            self.input_usuario.text = ""
            self.input_usuario.handle_event(event)
            self.input_password.handle_event(event)
            self.input_passwordconfirm.handle_event(event)

    def update(self):
        self.input_usuario.update()
        self.input_password.update()
        self.input_passwordconfirm.update()
    def render(self):
        self.gestor.superficie.fill(config.BACKGROUND_COLOR)
        self.gestor.pantalla.blit(self.gestor.superficie, (0,0))
        self.input_usuario.draw(self.gestor.pantalla)
        self.input_password.draw(self.gestor.pantalla)
        pygame.display.update()
    def ir_login(self):
        self.gestor.pantalla_actual = pantalla_login.PantallaLogin(self.gestor)
    def ir_jugador(self):
        pass
    def ir_admin(self):
        pass
