import pygame

class GameView:
    def __init__(self, screen, maze, pacman, ghosts, pellets, power_pellets):
        self.screen = screen
        self.maze = maze
        self.pacman = pacman
        self.ghosts = ghosts
        self.pellets = pellets
        self.power_pellets = power_pellets

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.maze.draw(self.screen)
        pygame.draw.circle(self.screen, (255, 255, 0), self.pacman.position, 10)
        for ghost in self.ghosts:
            if not ghost.is_eaten:
                ghost.draw(self.screen)
        for pellet in self.pellets:
            pellet.draw(self.screen)
        for power_pellet in self.power_pellets:
            power_pellet.draw(self.screen)
