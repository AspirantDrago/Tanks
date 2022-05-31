from modules.config import *
import pygame
from modules.functions import load_image
import random
import numpy as np
import math

shell_group = pygame.sprite.Group()


class TankShell(pygame.sprite.Sprite):
    # orig_image = load_image(FN_IMAGE_SHELL)
    orig_image = None

    @staticmethod
    def initial():
        TankShell.orig_image = load_image(FN_IMAGE_SHELL, -1)

    def __init__(self, tank, screen, *groups):
        from modules.game import all_sprites
        super().__init__(all_sprites, shell_group)
        from modules.tank import TankRight, TankLeft
        self.screen = screen
        self.tank = tank
        image_h = self.orig_image.get_height() * \
                  SHELL_LENGTH // self.orig_image.get_width()
        self.image = pygame.transform.scale(self.orig_image, (SHELL_LENGTH, image_h))
        self.rect = self.image.get_rect()
        self.speed_x = SHELL_SPEED
        self.speed_y = 0
        muzzle_coord = self.tank.get_my_muzzle()
        if isinstance(self.tank, TankRight):
            self.image = pygame.transform.flip(self.image, True, False)
            self.speed_x *= -1
            self.rect.right = muzzle_coord[0]
        if isinstance(self.tank, TankLeft):
            self.rect.left = muzzle_coord[0]
        self.rect.centery = muzzle_coord[1]
        self.x = self.rect.centerx
        self.y = self.rect.centery

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, -angle)
        new_rect = self.image.get_rect()
        new_rect.move_ip(self.rect.center)
        new_rect.move_ip(
            - (new_rect.width - self.rect.width) / 2,
            - (new_rect.height - self.rect.height) / 2,
        )
        self.rect = new_rect
        r = math.radians(angle)
        self.speed_x, self.speed_y = (
            self.speed_x * math.cos(r) - self.speed_y * math.sin(r),
            self.speed_x * math.sin(r) + self.speed_y * math.cos(r)
        )

    def update(self, *args, **kwargs):
        self.x += self.speed_x / FPS
        self.y += self.speed_y / FPS
        self.rect.center = self.x, self.y

        from modules.tank import tank_group
        target = pygame.sprite.spritecollideany(self, tank_group, pygame.sprite.collide_mask)
        if target:
            result = target.shot_shell(self)
            if result == SHOOT_SUCCESSFUL:
                self.kill()
            elif result == SHOOT_RICOCHET:
                self.tank = target
                self.set_ricochet()
        if not self.rect.colliderect(self.screen.get_rect()):
            self.kill()

    def set_ricochet(self):
        r = random.randint(-RICOCHET_ANGLE, RICOCHET_ANGLE)
        self.rotate(180 + r)

    def get_tank(self):
        return self.tank

    def get_gamage(self):
        return 0


class ExplosiveTankShell(TankShell):
    def get_gamage(self):
        return random.randint(SHELL_EXPLOSIVE_DAMAGE_MIN, SHELL_EXPLOSIVE_DAMAGE_MAX)

