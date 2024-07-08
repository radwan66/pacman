import pygame

class Maze:
    def __init__(self):
        self.walls = [
            pygame.Rect(0, 0, 800, 20),
            pygame.Rect(0, 580, 800, 20),
            pygame.Rect(0, 0, 20, 600),
            pygame.Rect(780, 0, 20, 600)
        ]
        self.create_internal_walls()

    def create_internal_walls(self):
        walls_positions = [
            (100, 100, 20, 400),
            (200, 100, 20, 400),
            (300, 0, 20, 300),
            (400, 300, 20, 300),
            (500, 100, 20, 400),
            (600, 50, 20, 500),
            (250, 50, 300, 20),
            (100, 400, 300, 20),
            (500, 200, 200, 20),
            (150, 150, 20, 200),
            (650, 100, 20, 200)
        ]
        for pos in walls_positions:
            self.walls.append(pygame.Rect(*pos))

    def draw(self, screen):
        for wall in self.walls:
            pygame.draw.rect(screen, (0, 0, 255), wall)

    def collides(self, rect):
        return any(wall.colliderect(rect) for wall in self.walls)
