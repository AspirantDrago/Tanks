import pygame
from modules.config import *
from modules.functions import load_image


class Tank(pygame.sprite.Sprite):
    def __init__(self, screen, *groups):
        super().__init__(*groups)
        image = load_image('images/tank.png')
        image_h = image.get_height() * WIDTH_TANK // image.get_width()
        image = pygame.transform.scale(image, (WIDTH_TANK, image_h))
        self.image = image
        self.rect = self.image.get_rect()
        self.screen = screen


class TankLeft(Tank):
    pass


class TankRight(Tank):
    def __init__(self, screen, *groups):
        super().__init__(screen, *groups)
        self.image = pygame.transform.flip(self.image, True, False)
