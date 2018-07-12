import pygame
import pantallas
import config
import boton
import sys
import pantalla_admin_lobby
import obtener_datos
import text_input

class PantallaTiempo(pantallas.Pantalla):
    def __init__(self,gestor):
        self.gestor = gestor
        pygame.display.set_caption("Pantalla Tiempo")

        self.input_tiempo = text_input.InputBox(400,300,100,40,"")
        self.font_grande = pygame.font.Font(None, 64)
        self.font_chica = pygame.font.Font(None, 32)

        self.fondo = pygame.image.load(config.fondo[3])
        self.regresar = boton.Button(100,550,100,40,"Regresar")
        self.salir = boton.Button(700,550,100,40,"Salir")
        self.tiempo = boton.Button(400,200,80,80,obtener_datos.obtener_tiempo_actual(), font=80)
        self.aceptar = boton.Button(370,360,90,40,"Aceptar")
    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.regresar.handle_event(event)
            self.salir.handle_event(event)
            self.aceptar.handle_event(event)
            self.input_tiempo.handle_event(event)

    def update(self):
        self.input_tiempo.update()
        if self.salir.active:
            pygame.quit()
            sys.exit()
        if self.regresar.active:
            self.gestor.pantalla_actual.ir_adminlobby()
            self.regresar.active = False
        if self.aceptar.active:
            obtener_datos.nuevo_tiempo(self.input_tiempo.text)
            self.gestor.pantalla_actual.ir_adminlobby()
            self.aceptar.active = False

    def render(self):
        self.gestor.pantalla.blit(self.fondo,(0,0))


        titulo = self.font_grande.render("Cambiar Tiempo", 1, (255, 255, 0))
        tiempo_actual = self.font_chica.render("Tiempo Actual", 1, (255, 255, 0))
        tiempo_nuevo = self.font_chica.render("Tiempo Nuevo", 1, (255, 255, 0))
        self.gestor.pantalla.blit(titulo, (230, 100))
        self.gestor.pantalla.blit(tiempo_actual, (230, 200))
        self.gestor.pantalla.blit(tiempo_nuevo, (230, 300 ))

        self.regresar.draw(self.gestor.pantalla)
        self.salir.draw(self.gestor.pantalla)
        self.tiempo.draw(self.gestor.pantalla)
        self.input_tiempo.draw(self.gestor.pantalla)
        self.aceptar.draw(self.gestor.pantalla)
        pygame.display.update()

    def ir_adminlobby(self):
        self.gestor.pantalla_actual = pantalla_admin_lobby.PantallaAdmin(self.gestor)
