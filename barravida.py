import pygame
import config

pygame.init()

class BarraVida:

    def __init__(self, x, y):

        self.rect1 = pygame.Rect(x, y, 100, 20)
        self.rect2 = pygame.Rect(x+3,y+3,self.vida,18)
        self.vida = 95
        self.colorrojo = pygame.Color(248,0,0)
        self.colornaranja = pygame.Color(255,164,032)
        self.colorverde = pygame.Color(0,247,0)

    def handle_event(self, event):
        pass
    def update(self):
        pass

    def draw(self,gestor):
        gestor.blit(self.rect1,(self.rect1.x,self.rect1.y))
        if self.vida <= 47:
            pygame.draw.rect2(gestor, self.colornaranja, self.rect2)
        elif self.vida <=23:
            pygame.draw.rect2(gestor, self.colorrojo,self.rect2)
        else:
            pygame.draw.rect2(gestor, self.colorverde,self.rect2)
