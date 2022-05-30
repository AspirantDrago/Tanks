import pygame
from modules.config import *
from modules.functions import load_image
from modules.panels import Panels


class Tank(pygame.sprite.Sprite):
    def __init__(self, screen, *groups):
        super().__init__(*groups)
        image = load_image('images/tank.png')
        image_h = image.get_height() * WIDTH_TANK // image.get_width()
        image = pygame.transform.scale(image, (WIDTH_TANK, image_h))
        self.image = image
        self.rect = self.image.get_rect()
        self.screen = screen
        h = screen.get_height() - MARGIN_TOP_SCREEN_FOR_TANK - MARGIN_BOTTOM_SCREEN_FOR_TANK
        # Координата по y
        self.y = h // 2 + MARGIN_TOP_SCREEN_FOR_TANK
        self.rect.centery = self.y
        # Здоровье
        self.healf = 70
        # Скорость
        self.speed = 0
        # Создание панели
        self.panel = Panels(self, *groups)
        # Время до конца перезарядки
        self.reload_cur_time = 2

    def get_healf(self):
        if self.healf < 0:
            return 0
        if self.healf > 100:
            return 1
        return self.healf / 100

    def update(self, *args, **kwargs):
        self.reload_cur_time -= 1 / FPS
        self.reload_cur_time = max(self.reload_cur_time, 0)

        if pygame.key.get_pressed()[self._get_my_key_up()]:
            self.speed -= SPEED_BOOST_TANK
        if pygame.key.get_pressed()[self._get_my_key_down()]:
            self.speed += SPEED_BOOST_TANK

        self.speed *= (1 - BREAK_SPEED_TANK / FPS)
        self.y += self.speed / FPS
        self.rect.centery = int(round(self.y))
        if self.rect.bottom > self.screen.get_height() - MARGIN_BACK_SCREEN_FOR_TANK:
            self.rect.bottom = self.screen.get_height() - MARGIN_BACK_SCREEN_FOR_TANK
            self.y = self.rect.centery
            if self.speed > 0:
                self.speed *= - WALL_COEFF_FOR_TANK
        if self.rect.top < MARGIN_TOP_SCREEN_FOR_TANK:
            self.rect.top = MARGIN_TOP_SCREEN_FOR_TANK
            self.y = self.rect.centery
            if self.speed < 0:
                self.speed *= - WALL_COEFF_FOR_TANK

    def _get_my_key_up(self):
        pass

    def _get_my_key_down(self):
        pass

    def _get_time_reload(self):
        '''
        Время (в секундах) на полную перезарядку
        '''
        return 2

    def _get_cur_reload(self):
        '''
        Время (в секундах) до конца перезарядки
        '''
        return self.reload_cur_time

    def get_reload(self):
        if self._get_time_reload() == 0:
            return 1
        return (self._get_time_reload() - self._get_cur_reload()) / \
               self._get_time_reload()


class TankLeft(Tank):
    def __init__(self, screen, *groups):
        super().__init__(screen, *groups)
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect.left = MARGIN_BACK_SCREEN_FOR_TANK
        self.panel.rect.left = self.rect.left

    def _get_my_key_up(self):
        return KeyControls.tank_left_up

    def _get_my_key_down(self):
        return KeyControls.tank_left_down


class TankRight(Tank):
    def __init__(self, screen, *groups):
        super().__init__(screen, *groups)
        self.rect.right = self.screen.get_width() - MARGIN_BACK_SCREEN_FOR_TANK
        self.panel.rect.left = self.rect.left

    def _get_my_key_up(self):
        return KeyControls.tank_right_up

    def _get_my_key_down(self):
        return KeyControls.tank_right_down
