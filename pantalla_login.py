import pygame
import pantallas
import text_input
import config
import requests
import pantalla_registro
import boton

class PantallaLogin(pantallas.Pantalla):
    fondo = pygame.image.load("Imagenes/peru.jpg")
    input_usuario = text_input.InputBox(
            (config.ANCHO - config.text_input_ancho) / 2,
            300,
            config.text_input_ancho,
            config.text_input_alto)
    input_password = text_input.InputBox(
            (config.ANCHO - config.text_input_ancho) / 2,
            400,
            config.text_input_ancho,
            config.text_input_alto)
    font_grande = pygame.font.Font(None, 64)
    font_chica = pygame.font.Font(None, 32)
    login = boton.Button(370, 480, 100, 40, text = 'Ingreso')
    registrar = boton.Button(370, 550, 100, 40, text = 'Registro')
    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.login.active = True
            self.input_usuario.handle_event(event)
            self.input_password.handle_event(event)
            self.registrar.handle_event(event)
            self.login.handle_event(event)

    def update(self):
        self.input_usuario.update()
        self.input_password.update()
        if self.registrar.active:
            self.registrar.active = False
            self.gestor.pantalla_actual.ir_registro()
        if self.login.active:
            self.login.active = False
            r = requests.get('http://165.227.76.18:3000/login?username=' +
                             self.input_usuario.text +
                             '&password=' +
                             self.input_password.text)
            print(self.input_usuario.text)
            print(self.input_password.text)
            print(r._content)
            result = r.content.split('/')
            if result[0] == 'true':
                if result[1] == 'admin':
                    self.gestor.pantalla_actual.ir_lobby_admin()
                elif result[1] == 'user':
                    self.gestor.pantalla_actual.ir_lobby()
            else:
                self.input_password.text = ""
                self.input_usuario.text = ""

    def render(self):
        self.gestor.pantalla.blit(self.gestor.superficie, (0,0))
        self.gestor.pantalla.blit(self.fondo, (0, 0))
        self.input_usuario.draw(self.gestor.pantalla)
        self.input_password.draw(self.gestor.pantalla)
        self.login.draw(self.gestor.pantalla)
        self.registrar.draw(self.gestor.pantalla)
        titulo = self.font_grande.render("Login", 1, (255, 255, 0))
        nombre_usuario = self.font_chica.render("Nombre de usuario", 1, (255, 255, 0))
        password = self.font_chica.render("Password", 1, (255, 255, 0))
        self.gestor.pantalla.blit(titulo, (370, 200))
        self.gestor.pantalla.blit(nombre_usuario, (330, 270))
        self.gestor.pantalla.blit(password, (380, 370))
        pygame.display.update()
    def ir_lobby(self):
        print("Se va al Lobby")
        #self.gestor.pantalla_actual = pantalla_lobby.PantallaLobby(self.gestor)
        pass
    def ir_registro(self):
        self.gestor.pantalla_actual = pantalla_registro.PantallaRegistro(self.gestor)
    def ir_jugador(self):
        pass
    def ir_admin(self):
        pass
