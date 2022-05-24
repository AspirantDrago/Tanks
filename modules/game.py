import pygame
from modules.functions import quit, check_quit_event, load_image
from modules.config import *
from modules.tank import TankLeft, TankRight

def game(screen):
    image = load_image(FN_IMAGE_GAME_BACK)
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    tank_l = TankLeft(screen, all_sprites)
    tank_r = TankRight(screen, all_sprites)
    while True:
        for event in pygame.event.get():
            check_quit_event(event)
        screen.blit(image, (0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


