import pygame as pg
from random import randint

from settings import *


class Player(pg.sprite.Sprite):
    """Player class"""

    def __init__(self):
        super().__init__()

        # Import all frames
        frame_walk_1 = pg.image.load(
            "./assets/images/alien-player/alien_walk_1.png").convert_alpha()
        frame_walk_2 = pg.image.load(
            "./assets/images/alien-player/alien_walk_2.png").convert_alpha()
        frame_jump = pg.image.load(
            "./assets/images/alien-player/alien_jump.png").convert_alpha()

        # Store frames
        self.frames = {
            "walk": [frame_walk_1, frame_walk_2],
            "jump": frame_jump,
        }
        self.frame_index = 0

        # Images and rectangles
        self.image = self.frames["walk"][self.frame_index]
        self.rect = self.image.get_rect(midbottom=(80, GROUND_HEIGHT - 100))

        # Other properties
        self.gravity = 0
        self.jump_sound = pg.mixer.Sound("./assets/audio/jump.mp3")
        self.jump_sound.set_volume(0.1)

    def user_input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_SPACE] and self.rect.bottom >= GROUND_HEIGHT:
            self.gravity = -15
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity

        if self.rect.bottom >= GROUND_HEIGHT:
            self.rect.bottom = GROUND_HEIGHT

    def animation(self):
        if self.rect.bottom < GROUND_HEIGHT:
            self.image = self.frames["jump"]
        else:
            self.frame_index += 0.1

            if self.frame_index >= len(self.frames["walk"]):
                self.frame_index = 0

            self.image = self.frames["walk"][int(self.frame_index)]

    def update(self):
        self.user_input()
        self.apply_gravity()
        self.animation()


class Mobs(pg.sprite.Sprite):
    """Mobs class for snail, flies and potential mobs"""

    def __init__(self, type):
        super().__init__()

        y_pos = GROUND_HEIGHT

        if type == "fly":
            frame_1 = pg.image.load(
                "./assets/images/fly-mob/fly_1.png").convert_alpha()
            frame_2 = pg.image.load(
                "./assets/images/fly-mob/fly_2.png").convert_alpha()

            y_pos = GROUND_HEIGHT - 100

        elif type == "snail":
            frame_1 = pg.image.load(
                "./assets/images/snail-mob/snail_1.png").convert_alpha()
            frame_2 = pg.image.load(
                "./assets/images/snail-mob/snail_2.png").convert_alpha()

        else:
            frame_1 = pg.Surface((80, 80))
            frame_1.fill("grey_10")
            frame_2 = pg.Surface((80, 80))
            frame_2.fill("grey_12")

        self.frames = [frame_1, frame_2]
        self.frame_index = 0

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(
            midbottom=(randint(SCREEN_WIDTH, SCREEN_WIDTH + 400), y_pos))

    def movement(self):
        self.rect.x -= 8

        if self.rect.right <= 0:
            self.kill()

    def animation(self):
        self.frame_index += 0.2

        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.movement()
        self.animation()
