import pygame
import pantallas
import config
import boton
import sys
import pantalla_admin_lobby
import obtener_datos
import text_input
class PantallaBaneo(pantallas.Pantalla):
    def __init__(self,gestor):
        self.gestor = gestor
        pygame.display.set_caption("Pantalla Baneo")

        self.input_usuario = text_input.InputBox(420,200,100,40,"")
        self.font_grande = pygame.font.Font(None, 64)
        self.font_chica = pygame.font.Font(None, 32)

        self.fondo = pygame.image.load(config.fondo[3])
        self.regresar = boton.Button(100,550,100,40,"Regresar")
        self.salir = boton.Button(700,550,100,40,"Salir")
        self.banear = boton.Button(370,300,90,40,"Banear")

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.regresar.handle_event(event)
            self.salir.handle_event(event)
            self.banear.handle_event(event)
            self.input_usuario.handle_event(event)
    def update(self):
        self.input_usuario.update()
        if self.salir.active:
            pygame.quit()
            sys.exit()
        if self.regresar.active:
            self.gestor.pantalla_actual.ir_adminlobby()
            self.regresar.active = False
        if self.banear.active:
            self.gestor.pantalla_actual.ir_adminlobby()
            self.banear.active = False


    def render(self):
        self.gestor.pantalla.blit(self.fondo,(0,0))

        titulo = self.font_grande.render("Banear Usuario", 1, (255, 255, 0))
        ingresar_usuario = self.font_chica.render("Ingresar Usuario", 1, (255, 255, 0))
        self.gestor.pantalla.blit(titulo, (230, 100))
        self.gestor.pantalla.blit(ingresar_usuario, (230, 200))
        self.banear.draw(self.gestor.pantalla)
        self.input_usuario.draw(self.gestor.pantalla)
        self.regresar.draw(self.gestor.pantalla)
        self.salir.draw(self.gestor.pantalla)
        pygame.display.update()

    def ir_adminlobby(self):
        self.gestor.pantalla_actual = pantalla_admin_lobby.PantallaAdmin(self.gestor)
