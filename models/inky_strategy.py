import pygame
from .blinky_strategy import BlinkyStrategy

class InkyStrategy:
    def move(self, ghost, pacman, other_ghosts, maze):
        directions = {
            'up': (0, -5),
            'down': (0, 5),
            'left': (-5, 0),
            'right': (5, 0)
        }

        blinky = next(g for g in other_ghosts if isinstance(g.strategy, BlinkyStrategy))
        blinky_pos = blinky.position

        target_x = pacman.position[0] + directions[pacman.direction][0] * 2
        target_y = pacman.position[1] + directions[pacman.direction][1] * 2

        predict_x = blinky_pos[0] + (target_x - blinky_pos[0]) * 2
        predict_y = blinky_pos[1] + (target_y - blinky_pos[1]) * 2

        if predict_x < ghost.position[0]:
            direction_x = 'left'
        else:
            direction_x = 'right'

        if predict_y < ghost.position[1]:
            direction_y = 'up'
        else:
            direction_y = 'down'

        new_position = (
            ghost.position[0] + directions[direction_x][0],
            ghost.position[1] + directions[direction_y][1]
        )
        new_rect = pygame.Rect(new_position[0], new_position[1], ghost.size, ghost.size)
        if not maze.collides(new_rect):
            ghost.position = new_position