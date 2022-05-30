import sys
import os
import pygame
from modules.config import *


def check_quit_event(event):
    if event.type == pygame.QUIT or \
            event.type == pygame.KEYDOWN and event.key == KeyControls.exit:
        quit()


def quit():
    try:
        pygame.quit()
    except BaseException as e:
        pass
    sys.exit(0)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {name} отсутствует')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image