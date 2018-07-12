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

    def rads(self, angle):
        return angle * math.pi / 180

    def update(self, angle, x):
        # Update the angle
        self.angle = angle
        self.x = x

    def flip(self):
        self.flipped = not self.flipped

    def draw(self, screen):
        # Blit the components.
        if not self.flipped:
            pygame.draw.arc(screen, config.PURPLE, [self.x, self.y - 50, 100, 100],
                    0, self.rads(90), 4)
            pygame.draw.arc(screen, config.BLUE, [self.x, self.y - 50, 100, 100],
                    self.rads(self.angle - 10), self.rads(self.angle + 10), 4)
        else:
            pygame.draw.arc(screen, config.PURPLE, [self.x, self.y - 50, 100, 100],
                    self.rads(90), self.rads(180), 4)
            pygame.draw.arc(screen, config.BLUE, [self.x, self.y - 50, 100, 100],
                    self.rads(180 - (self.angle + 10)), self.rads(180 - (self.angle - 10)), 4)

    def reset(self):
        self.load.w = 0

