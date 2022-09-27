# Import modules
import pygame as pg
from sys import exit
from random import choice


# Import module files
import entity
from global_var import ground_height, screen_width, screen_height


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

# Player and mobs element
player = pg.sprite.GroupSingle(entity.Player())

mobs = pg.sprite.Group()


game = True

time = pg.time.get_ticks()
# Primary game loop
while True:
    now = pg.time.get_ticks()
    # Event listener loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit
            exit()

        if now - time >= 1000:
            mobs.add(entity.Mobs(choice(["fly", "snail", "snail", "snail"])))
            time = now

    print(now - time)
    if game:
        # Add backdrop to screen
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, ground_height))

        mobs.draw(screen)
        mobs.update()

        player.draw(screen)
        player.update()

    # Game update frames
    pg.display.update()
    clock.tick(60)
