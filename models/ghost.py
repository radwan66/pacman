import pygame

class Ghost:
    def __init__(self, position, strategy, color):
        self.position = position
        self.size = 20
        self.strategy = strategy
        self.color = color
        self.is_eaten = False
        self.normal_color = color
        self.blue_color = (0, 0, 255)
        self.speed = 2

    def move(self, pacman, other_ghosts, maze):
        self.strategy.move(self, pacman, other_ghosts, maze)

    def draw(self, screen):
        color = self.blue_color if self.is_eaten else self.color
        pygame.draw.circle(screen, color, self.position, self.size // 2)

    def turn_blue(self):
        self.color = self.blue_color

    def turn_normal(self):
        self.color = self.normal_color
        self.is_eaten = False
