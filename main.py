# Import modules
import pygame as pg
from sys import exit
from random import choice, randint


# Import module files
from entity import *
from settings import *

# Initialize pygame
pg.init()


# Initial setup
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Alien Run")
clock = pg.time.Clock()


# Backdrop elements
sky_surf = pg.image.load("./assets/images/sky.png").convert()
ground_surf = pg.image.load("./assets/images/ground.png").convert()

# Player and mobs element
player = pg.sprite.GroupSingle(Player())

mobs = pg.sprite.Group()


game_active = True

time = pg.time.get_ticks()
# Primary game loop
while True:
    now = pg.time.get_ticks()
    # Event listener loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit
            exit()

    if now - time >= randint(800, 1200):
        mobs.add(Mobs(choice(["fly", "snail", "snail", "snail"])))
        time = now

    print(now-time)

    if game_active:
        # Add backdrop to screen
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, GROUND_HEIGHT))

        mobs.draw(screen)
        mobs.update()

        player.draw(screen)
        player.update()

    # Game update frames
    pg.display.update()
    clock.tick(60)
