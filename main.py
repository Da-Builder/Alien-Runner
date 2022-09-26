# Import modules
import pygame as pg
from sys import exit
from random import randint


class Player(pg.sprite.Sprite):
    """Player class"""

    def __init__(self):

        super().__init__()
        self.image = pg.image.load(
            "./assets/images/alien-player/alien_stand.png"
        ).convert_alpha()

        self.rect = self.image.get_rect(midbottom=(80, ground_height))
        self.gravity = 0

    def user_input(self):
        keys = pg.key.get_pressed()
        mouse = pg.mouse.get_pressed()

        if keys[pg.K_SPACE] and self.rect.bottom >= ground_height or mouse[0] and self.rect.bottom >= ground_height:
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


class Mobs(pg.sprite.Sprite):
    """Mobs class fro all enemy"""

    def __init__(self, image, speed=(5, 10), height=0):

        super().__init__()
        self.image = pg.image.load(
            "./assets/images/snail-mob/snail_1.png").convert_alpha()
        self.rect = self.image.get_rect(
            bottomleft=(800, ground_height + height)
        )

        self.speed = randint(speed[0], speed[1])

    def travel(self):
        self.rect.x += self.speed

        if self.rect.right <= 0:
            self.rect.x = screen_width

    def animation(self):
        pass

    def update(self):
        self.travel()


# Initialize pygame
pg.init()

# Initial setup
screen_width, screen_height = 800, 400
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Alien Run")
clock = pg.time.Clock()


# Backdrop elements
sky_surf = pg.image.load("./assets/images/sky.png").convert()
ground_surf = pg.image.load("./assets/images/ground.png").convert()
ground_height = 300


# Player elements
player = pg.sprite.GroupSingle()
player.add(Player())


# Mob elements
snail = pg.sprite.GroupSingle()
snail.add(Mobs(
    image=pg.image.load(
        "./assets/images/snail-mob/snail_1.png").convert_alpha()
))


# Primary game loop
while True:
    # Event listener loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit
            exit()

    # Add backdrop to screen
    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, ground_height))

    # Snail
    snail.draw(screen)
    snail.update()

    # Player
    player.draw(screen)
    player.update()

    # Game update frames
    pg.display.update()
    clock.tick(60)
