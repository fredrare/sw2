import pygame
import config

pygame.init()

class Power:

    def __init__(self, x, y, width, height, limit):
        self.height = height
        self.width = width
        self.limit = limit
        self.frame = pygame.Rect(x, y, width, height)
        self.load = pygame.Rect(x + 5, y + 5, width - 2, height - 8)
        self.load.w = 0

    def update(self, power):
        # Resize the box if the text is too long.
        self.load.w = power * (self.width - 2) / self.limit

    def draw(self, screen):
        # Blit the rect.
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), self.frame, 2)
        pygame.draw.rect(screen, pygame.Color(255, 255, 50), self.load, self.height / 2 + 1)

    def reset(self):
        self.load.w = 0

