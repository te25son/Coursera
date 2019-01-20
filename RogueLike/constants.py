import pygame

pygame.init()

# Game Sizes
GAME_WIDTH = 800
GAME_HEIGHT = 600
CELL_WIDTH = 32  # because sprite imgs are 32x32
CELL_HEIGHT = 32  # because sprite imgs are 32x32

# Map Vars
MAP_WIDTH = 30
MAP_HEIGHT = 30

#   ____      _
#  / ___|___ | | ___  _ __ ___
# | |   / _ \| |/ _ \| '__/ __|
# | |__| (_) | | (_) | |  \__ \
#  \____\___/|_|\___/|_|  |___/

# Color Definitions
COLOR_BLACK = (0, 0, 0)  # RGB for black
COLOR_WHITE = (255, 255, 255)  # RGB for white
COLOR_GREY = (100, 100, 100)  # RGB for grey(ish)

# Game Colors
COLOR_DEFAULT_BG = COLOR_GREY

#  ____             _ _
# / ___| _ __  _ __(_) |_ ___  ___
# \___ \| '_ \| '__| | __/ _ \/ __|
#  ___) | |_) | |  | | ||  __/\__ \
# |____/| .__/|_|  |_|\__\___||___/
#       |_|

#character
S_PLAYER = pygame.image.load('data/python.png')
S_WALL = pygame.image.load('data/wall.png')
S_FLOOR = pygame.image.load('data/floor.jpg')
