import pygame as pg
from random import randint

from global_var import ground_height, screen_width, screen_height


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
        frame_idle = pg.image.load(
            "./assets/images/alien-player/alien_stand.png").convert_alpha()

        # Store frames
        self.frames = {
            "walk": [frame_walk_1, frame_walk_2],
            "jump": frame_jump,
            "idle": frame_idle
        }
        self.frame_index = 0

        # Images and rectangles
        self.image = self.frames["walk"][self.frame_index]
        self.rect = self.image.get_rect(midbottom=(80, ground_height))

        # Other properties
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

    def animation(self):
        if self.rect.bottom < ground_height:
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

        y_pos = ground_height

        if type == "fly":
            frame_1 = pg.image.load(
                "./assets/images/fly-mob/fly_1.png").convert_alpha()
            frame_2 = pg.image.load(
                "./assets/images/fly-mob/fly_2.png").convert_alpha()

            y_pos = ground_height - 100

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
            midbottom=(randint(screen_width, screen_width + 200), y_pos))

    def movement(self):
        self.rect.x -= 8

        if self.rect.right <= 0:
            self.kill()

    def animation(self):
        self.frame_index += 0.05

        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.movement()
        self.animation()
