import pygame
import random

class RandomStrategy:
    def move(self, ghost, pacman, maze):
        directions = {
            'up': (0, -5),
            'down': (0, 5),
            'left': (-5, 0),
            'right': (5, 0)
        }
        for _ in range(10):
            direction = random.choice(list(directions.keys()))
            new_position = (
                ghost.position[0] + directions[direction][0],
                ghost.position[1] + directions[direction][1]
            )
            new_rect = pygame.Rect(new_position[0], new_position[1], ghost.size, ghost.size)
            if not maze.collides(new_rect) and pygame.Rect(ghost.area).contains(new_rect):
                ghost.position = new_position
                break

        if not pygame.Rect(ghost.area).contains(new_rect):
            ghost.position = [ghost.area.x + ghost.area.width // 2, ghost.area.y + ghost.area.height // 2]
