# Import modules
import pygame as pg
from sys import exit
from random import choice

# Import module files
from entity import *
from settings import *


# Initialize pygame
pg.init()

# Initial setup
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Alien Runner")
clock = pg.time.Clock()

game_state = False


# Backdrop elements
sky_surf = pg.image.load("./assets/images/sky.png").convert()
ground_surf = pg.image.load("./assets/images/ground.png").convert()

# Player and mobs element
player = pg.sprite.GroupSingle(Player())
player_idle_surf = pg.image.load(
    "./assets/images/alien-player/alien_stand.png").convert_alpha()
player_idle_surf = pg.transform.rotozoom(player_idle_surf, 0, 2)
player_idle_rect = player_idle_surf.get_rect(
    center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

mobs = pg.sprite.Group()
mob_timer = pg.USEREVENT + 1
pg.time.set_timer(mob_timer, 1400)


# Text elements
score = 0

font = pg.font.Font("./assets/font/pixel_type.ttf", 50)
title_surf = font.render("Alien Runner", False, LIGHT_BLUE)
title_rect = title_surf.get_rect(midtop=(SCREEN_WIDTH/2, 50))

instruction_surf = font.render("Press space to run", False, LIGHT_BLUE)
instruction_rect = instruction_surf.get_rect(
    midbottom=(SCREEN_WIDTH/2, SCREEN_HEIGHT - 50))


score_surf = font.render(f"Score: {score}", False, "grey25")
score_rect = score_surf.get_rect(midtop=(SCREEN_WIDTH/2, 30))

# Primary game loop
while True:
    # Event listener loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit
            exit()

        if game_state:
            if event.type == mob_timer:
                mobs.add(Mobs(choice(["fly", "snail", "snail", "snail"])))
        else:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                game_state = True

    if game_state:
        # Add backdrop to screen
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, GROUND_HEIGHT))

        screen.blit(score_surf, score_rect)

        mobs.draw(screen)
        mobs.update()

        player.draw(screen)
        player.update()

    else:
        screen.fill((94, 129, 162))

        screen.blit(title_surf, title_rect)
        screen.blit(instruction_surf, instruction_rect)

        screen.blit(player_idle_surf, player_idle_rect)

    # Game update frames
    pg.display.update()
    clock.tick(60)
