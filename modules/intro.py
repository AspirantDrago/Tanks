import pygame
import time
from modules.functions import quit, check_quit_event, load_image
from modules.config import *

def intro(screen):
    image = load_image(FN_IMAGE_INTRO_BACK)
    screen.blit(image, (0, 0))
    pygame.display.flip()
    timer = time.time()
    while True:
        for event in pygame.event.get():
            check_quit_event(event)
            if event.type == pygame.KEYDOWN:
                return
        current_time = time.time()
        if current_time - timer >= TIMEOUT_INTRO:
            return
