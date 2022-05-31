import pygame
from modules.config import *
from modules.functions import load_image
from modules.panels import Panels
from modules.tank_shell import ExplosiveTankShell
import random


tank_group = pygame.sprite.Group()


class Tank(pygame.sprite.Sprite):
    def __init__(self, screen, *groups):
        super().__init__(*groups, tank_group)
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
        self.health = 100
        # Скорость
        self.speed = 0
        # Создание панели
        self.panel = Panels(self, *groups)
        # Время до конца перезарядки
        self.reload_cur_time = 2

    def get_health(self):
        if self.health < 0:
            return 0
        if self.health > 100:
            return 1
        return self.health / 100

    def update(self, *args, **kwargs):
        if self.is_alive():
            self.reload_cur_time -= 1 / FPS
            self.reload_cur_time = max(self.reload_cur_time, 0)

            if self.is_has_going():
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

            if self.is_has_fire():
                if pygame.key.get_pressed()[self._get_mey_key_fire()]:
                    ExplosiveTankShell(self, self.screen, self.groups())
                    self.reload_cur_time = self._get_time_reload()

    def _get_my_key_up(self):
        pass

    def _get_my_key_down(self):
        pass

    def _get_mey_key_fire(self):
        pass

    def get_my_muzzle(self):
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
        if not self.is_alive():
            return 0
        if self._get_time_reload() == 0:
            return 1
        return (self._get_time_reload() - self._get_cur_reload()) / \
               self._get_time_reload()

    def is_alive(self):
        return self.health > 0

    def is_has_going(self):
        return self.is_alive()

    def is_has_fire(self):
        if not self.is_alive():
            return False
        return self.reload_cur_time <= 0

    def shot_shell(self, shell):
        if self.is_alive():
            if self is not shell.get_tank():
                r = random.random()
                print(r, PROB_DAMAGE)
                if r < PROB_DAMAGE:
                    self.health -= shell.get_gamage()
                    return SHOOT_SUCCESSFUL
                else:
                    return SHOOT_RICOCHET
        return SHOOT_MISS



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

    def _get_mey_key_fire(self):
        return KeyControls.tank_left_fire

    def get_my_muzzle(self):
        x = self.rect.left + self.rect.w * (1 - SHELL_TANK_START_X)
        y = self.rect.y + self.rect.h * SHELL_TANK_START_Y
        return x, y


class TankRight(Tank):
    def __init__(self, screen, *groups):
        super().__init__(screen, *groups)
        self.rect.right = self.screen.get_width() - MARGIN_BACK_SCREEN_FOR_TANK
        self.panel.rect.left = self.rect.left

    def _get_my_key_up(self):
        return KeyControls.tank_right_up

    def _get_my_key_down(self):
        return KeyControls.tank_right_down

    def _get_mey_key_fire(self):
        return KeyControls.tank_right_fire

    def get_my_muzzle(self):
        x = self.rect.x + self.rect.w * SHELL_TANK_START_X
        y = self.rect.y + self.rect.h * SHELL_TANK_START_Y
        return x, y