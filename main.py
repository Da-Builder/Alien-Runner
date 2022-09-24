# Import modules
import pygame
from sys import exit

# Initial setup
pygame.init
screen_size = (800, 400)
screen = pygame.display.set_mode((screen_size))
clock = pygame.time.Clock()
pygame.display.set_caption("Alien Run")

# Primary game loop
while True:
    # Event listener loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()

    # Game update frames
    pygame.display.update()
    clock.tick(60)
