import pygame
import pantallas
import config
import boton
import sys
import pantalla_sala
import obtener_datos
import text_input
import sesion

class PantallaResultados(pantallas.Pantalla):
    def __init__(self,gestor):
        self.gestor = gestor
        pygame.display.set_caption("Pantalla Resultado")
        self.sesion = sesion.Sesion.get_instance()
        self.ganador = 'jugador' + str(self.sesion.ganador)
        self.perdedor = 'jugador' + str(1 - self.sesion.ganador)
        self.font_grande = pygame.font.Font(None, 64)
        self.font_chica = pygame.font.Font(None, 32)

        self.fondo = pygame.image.load(config.fondo[3])
        self.aceptar = boton.Button(330,400,100,40,"Aceptar")
    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.aceptar.handle_event(event)

    def update(self):
        if self.aceptar.active:
            self.gestor.pantalla_actual.ir_sala()
            self.aceptar.active = False

    def render(self):
        self.gestor.pantalla.blit(self.fondo,(0,0))


        titulo = self.font_grande.render("Tabla de Resultados", 1, (255, 255, 0))
        ganador = self.font_chica.render("Ganador", 1, (255, 255, 0))
        perdedor = self.font_chica.render("Perdedor", 1, (255, 255, 0))
        ganadorcito = self.font_chica.render(self.ganador, 1, (255, 0, 0))
        perdedorcito = self.font_chica.render(self.perdedor,1,(255, 0, 0))
        self.gestor.pantalla.blit(titulo, (200, 100))
        self.gestor.pantalla.blit(ganador, (230, 200))
        self.gestor.pantalla.blit(perdedor, (230, 300 ))
        self.gestor.pantalla.blit(ganadorcito, (350, 200 ))
        self.gestor.pantalla.blit(perdedorcito, (350, 300 ))

        self.aceptar.draw(self.gestor.pantalla)

        pygame.display.update()

    def ir_sala(self):
        self.gestor.pantalla_actual = pantalla_sala.PantallaSala(self.gestor)
