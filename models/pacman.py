import pygame

class Pacman:
    def __init__(self, position):
        self.position = position
        self.size = 20
        self.direction = 'right'

    def move(self, direction, maze):
        directions = {
            'up': (0, -5),
            'down': (0, 5),
            'left': (-5, 0),
            'right': (5, 0)
        }
        self.direction = direction
        new_position = (
            self.position[0] + directions[direction][0],
            self.position[1] + directions[direction][1]
        )
        new_rect = pygame.Rect(new_position[0], new_position[1], self.size, self.size)
        if not maze.collides(new_rect):
            self.position = new_position
