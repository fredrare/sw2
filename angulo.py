import pygame
import config
import math

pygame.init()

class Angle:

    def __init__(self, x, y, angle = 45):
        # Set the initial angle
        self.angle = angle * math.pi / 180
        self.x = x
        self.y = y
        self.flipped = False

    def update(self, angle, x):
        # Update the angle
        self.angle = angle * math.pi / 180
        self.x = x

    def flip(self):
        self.flipped = not self.flipped

    def draw(self, screen):
        # Blit the components.
        if not self.flipped:
            pygame.draw.arc(screen, config.PURPLE, [self.x, self.y - 50, 100, 100], 0, math.pi / 2, 4)
        else:
            pygame.draw.arc(screen, config.PURPLE, [self.x, self.y - 50, 100, 100], math.pi / 2, math.pi, 4)

    def reset(self):
        self.load.w = 0

