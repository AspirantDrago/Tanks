import pygame
from modules.config import *


class Panels(pygame.sprite.Sprite):
    def __init__(self, tank, *groups):
        super().__init__(*groups)
        self.tank = tank
        self.count_panels = 2
        self.clear()
        self.rect = self.image.get_rect()

    def update(self, *args, **kwargs):
        self.rect.bottom = self.tank.rect.top - PANEL_MARGIN
        self.clear()
        self._draw_health(0)

    def clear(self):
        self.image = pygame.Surface(
            (WIDTH_TANK, PANEL_HEIGHT * self.count_panels),
            pygame.SRCALPHA, 32
        )
        self.image = self.image.convert_alpha()

    def _draw_panel(self, pos, color, method):
        rect = pygame.Rect(0, PANEL_HEIGHT * pos, WIDTH_TANK, PANEL_HEIGHT)
        new_rect = rect.copy()
        new_rect.width *= method()
        pygame.draw.rect(self.image, color, new_rect)
        pygame.draw.rect(self.image, PANEL_COLOR_BORDER, rect,
                         width=PANEL_WIDTH_BORDER)

    def _draw_health(self, pos):
        self._draw_panel(0, PANEL_COLOR_HEALTH, self.tank.get_health)
        self._draw_panel(1, PANEL_COLOR_TIME, self.tank.get_reload)





