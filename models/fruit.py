import pygame

class Fruit:
    def __init__(self, position, fruit_type):
        self.position = list(position)
        self.fruit_type = fruit_type
        self.size = 20

    def draw(self, screen):
        color = (0, 255, 0) if self.fruit_type == "apple" else (255, 0, 0)
        pygame.draw.circle(screen, color, self.position, self.size)
