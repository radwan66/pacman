import pygame
from models.pacman import Pacman
from models.ghost import Ghost
from models.pellet import Pellet
from models.power_pellet import PowerPellet
from models.maze import Maze
from models.blinky_strategy import BlinkyStrategy
from models.pinky_strategy import PinkyStrategy
from models.inky_strategy import InkyStrategy
from models.clyde_strategy import ClydeStrategy

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pacman")
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.pacman = Pacman((50, 50))
        self.maze = Maze()
        self.ghosts = [
            Ghost((240, 200), BlinkyStrategy(), (255, 0, 0)),
            Ghost((280, 200), PinkyStrategy(), (255, 182, 193)),
            Ghost((320, 200), InkyStrategy(), (0, 255, 255)),
            Ghost((360, 200), ClydeStrategy(), (255, 165, 0))
        ]
        self.pellets = [Pellet((x * 40 + 30, y * 40 + 30)) for x in range(1, 19) for y in range(1, 14)]
        self.power_pellets = [
            PowerPellet((100, 100)),
            PowerPellet((700, 100)),
            PowerPellet((100, 500)),
            PowerPellet((700, 500))
        ]
        self.score = 0
        self.power_mode = False
        self.power_mode_time = 0
        self.direction = None

    def start_game(self):
        self.is_running = True
        while self.is_running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.direction = 'up'
                elif event.key == pygame.K_DOWN:
                    self.direction = 'down'
                elif event.key == pygame.K_LEFT:
                    self.direction = 'left'
                elif event.key == pygame.K_RIGHT:
                    self.direction = 'right'

    def update(self):
        if self.direction:
            self.pacman.move(self.direction, self.maze)

        pacman_rect = pygame.Rect(self.pacman.position[0], self.pacman.position[1], 20, 20)

        for pellet in self.pellets[:]:
            if pacman_rect.colliderect(pygame.Rect(pellet.position[0], pellet.position[1], 5, 5)):
                self.pellets.remove(pellet)
                self.score += 10

        for power_pellet in self.power_pellets[:]:
            if pacman_rect.colliderect(pygame.Rect(power_pellet.position[0], power_pellet.position[1], 8, 8)):
                self.power_pellets.remove(power_pellet)
                self.score += 50
                self.activate_power_mode()

        for ghost in self.ghosts:
            ghost_rect = pygame.Rect(ghost.position[0], ghost.position[1], 20, 20)
            if pacman_rect.colliderect(ghost_rect):
                if self.power_mode and not ghost.is_eaten:
                    ghost.is_eaten = True
                    self.score += 200
                elif not self.power_mode:
                    self.is_running = False

        for ghost in self.ghosts:
            if not ghost.is_eaten:
                ghost.move(self.pacman, self.ghosts, self.maze)

        if self.power_mode:
            self.power_mode_time -= 1
            if self.power_mode_time <= 0:
                self.deactivate_power_mode()

    def activate_power_mode(self):
        self.power_mode = True
        self.power_mode_time = 600  # 600 frames (approximately 20 seconds)
        for ghost in self.ghosts:
            ghost.turn_blue()

    def deactivate_power_mode(self):
        self.power_mode = False
        for ghost in self.ghosts:
            ghost.turn_normal()

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

    def stop_game(self):
        self.is_running = False
        pygame.quit()
