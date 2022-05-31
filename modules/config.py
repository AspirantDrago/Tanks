import pygame
from modules.controls import KeyControls

# НАСТРОЙКИ ГЛОБАЛЬНЫЕ
NAME = 'Танки'
SIZE = WIDTH, HEIGHT = 800, 600
FN_ICON = 'icon.ico'

# НАСТРОЙКИ ЗАСТАВКИ
FN_IMAGE_INTRO_BACK = 'images/intro_back.jpg'
TIMEOUT_INTRO = 2       # Задержка в секундах

# НАСТРОЙКИ МЕНЮ
FN_IMAGE_MENU_BACK = 'images/menu_back.jpg'

# НАСТРОЙКИ ИГРЫ
FN_IMAGE_GAME_BACK = 'images/game_back.jpg'
FN_IMAGE_TANK = 'images/tank.png'
FN_IMAGE_SHELL = 'images/shell.png'
WIDTH_TANK = 200
FPS = 60
MARGIN_TOP_SCREEN_FOR_TANK = 50 # Зазор между экраном и танком сверху
MARGIN_BOTTOM_SCREEN_FOR_TANK = 10 # Зазор между экраном и танком снизу
MARGIN_BACK_SCREEN_FOR_TANK = 10 # Зазор между экраном и танком сбоку
SPEED_BOOST_TANK = 7 # Ускорение танка
BREAK_SPEED_TANK = 0.3 # Кооэффициент торможения танка
WALL_COEFF_FOR_TANK = 0.6 # Коэффициент упругого отскока танка от края экрана
PROB_DAMAGE = 0.75  # Вероятность урона

# Настройки панелей
PANEL_HEIGHT = 8 # Высота одной панели
PANEL_MARGIN = 10 # Расстояние от панелей до танков
PANEL_WIDTH_BORDER = 1
PANEL_COLOR_BORDER = 'black'
PANEL_COLOR_HEALTH = 'red'
PANEL_COLOR_TIME = 'blue'

# Настройка снарядов
SHELL_LENGTH = 50
SHELL_SPEED = 600
RICOCHET_ANGLE = 60 # Угол рекошета
# Координаты танка, откуда вылетают снаряды (в долях единицы)
SHELL_TANK_START_X = 0
SHELL_TANK_START_Y = 74 / 265
# Фугасные
SHELL_EXPLOSIVE_DAMAGE_MIN = 20
SHELL_EXPLOSIVE_DAMAGE_MAX = 40

# РЕЗУЛЬТАТЫ СТРЕЛЬБЫ
SHOOT_SUCCESSFUL = 1
SHOOT_RICOCHET = 0
SHOOT_MISS = -1
