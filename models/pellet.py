import pygame

class Pellet:
    def __init__(self, position):
        self.position = list(position)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, 5)
