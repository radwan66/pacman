import pygame

class PowerPellet:
    def __init__(self, position):
        self.position = list(position)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, 8)
