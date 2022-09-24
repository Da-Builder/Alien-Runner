# Import modules
import pygame
from sys import exit


class Player(pygame.sprite.Sprite):
    """Player class"""

    def __init__(self):

        super().__init__()
        self.image = pygame.image.load(
            "./assets/images/alien-player/alien_stand.png"
        ).convert_alpha()

        self.rect = self.image.get_rect(midbottom=(50, ground_height))
        self.gravity = 0

    def user_input(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        if keys[pygame.K_SPACE] and self.rect.bottom >= ground_height or mouse[0] and self.rect.bottom >= ground_height:
            self.gravity = -15

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity

        if self.rect.bottom >= ground_height:
            self.rect.bottom = ground_height

    def animation():
        pass

    def update(self):
        self.user_input()
        self.apply_gravity()


        # Initialize pygame
pygame.init()

# Initial setup
screen_width, screen_height = 800, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Run")
clock = pygame.time.Clock()


# Backdrop elements
sky_surf = pygame.image.load("./assets/images/sky.png").convert()
ground_surf = pygame.image.load("./assets/images/ground.png").convert()
ground_height = 300


# Player elements
player = pygame.sprite.GroupSingle()
player.add(Player())

# Primary game loop
while True:
    # Event listener loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()

    # Add backdrop to screen
    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, ground_height))

    # Player
    player.draw(screen)
    player.update()

    # Game update frames
    pygame.display.update()
    clock.tick(60)
