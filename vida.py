import pygame
import config

pygame.init()

class Vida:

    def __init__(self, x, y, width, height, limit):
        self.height = height
        self.width = width
        self.limit = limit
        self.frame = pygame.Rect(x, y, width, height)
        self.life = pygame.Rect(x + 5, y + 5, width - 2, height - 8)
        self.ammount = limit / 5
        self.life.w = self.ammount * (self.width - 2) / self.limit

    def update(self, hit):
        # Resize the box if the text is too long.
        self.ammount -= hit
        self.life.w = self.ammount * (self.width - 2) / self.limit

    def draw(self, screen):
        # Blit the rect.
        pygame.draw.rect(screen, pygame.Color(0, 0, 0), self.frame, 2)
        pygame.draw.rect(screen, pygame.Color(
            255 * (self.limit - self.ammount) / self.limit,
            255 * (1 - (self.limit - self.ammount) / self.limit),
            0), self.life, self.height / 2)

    def reset(self):
        self.load.w = 0

