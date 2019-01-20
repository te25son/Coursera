# 3rd Party Modules
import pygame
import tcod as libtcod

# game files
import constants

#  ____  _                   _
# / ___|| |_ _ __ _   _  ___| |_ ___
# \___ \| __| '__| | | |/ __| __/ __|
#  ___) | |_| |  | |_| | (__| |_\__ \
# |____/ \__|_|   \__,_|\___|\__|___/

class struct_tile:
    def __init__(self, block_path):
        self.block_path = block_path


#  __  __
# |  \/  | __ _ _ __
# | |\/| |/ _` | '_ \
# | |  | | (_| | |_) |
# |_|  |_|\__,_| .__/
#              |_|

def map_create():
    new_map = [[struct_tile(False) for y in range(0, constants.MAP_HEIGHT)] for x in range(0, constants.MAP_WIDTH)]

    new_map[10][10].block_path = True
    new_map[10][15].block_path = True

    return new_map


#  ____                     _
# |  _ \ _ __ __ ___      _(_)_ __   __ _
# | | | | '__/ _` \ \ /\ / / | '_ \ / _` |
# | |_| | | | (_| |\ V  V /| | | | | (_| |
# |____/|_|  \__,_| \_/\_/ |_|_| |_|\__, |
#                                   |___/

def draw_game():
    global SURFACE_MAIN

    # clear the surface
    SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)

    # draw the map
    draw_map(GAME_MAP)

    # draw the character
    SURFACE_MAIN.blit(constants.S_PLAYER, (200, 200))

    # update the display
    pygame.display.flip()


def draw_map(map_to_draw):

    for x in range(0, constants.MAP_WIDTH):
        for y in range(0, constants.MAP_HEIGHT):
            if map_to_draw[x][y].block_path:
                # draw a wall
                SURFACE_MAIN.blit(constants.S_WALL, (x * constants.CELL_WIDTH, y * constants.CELL_HEIGHT))  # multiply x and y by cell width to get visual location
            else:
                #draw a floor
                SURFACE_MAIN.blit(constants.S_FLOOR, (x * constants.CELL_WIDTH, y * constants.CELL_HEIGHT))  # same as wall


#   ____
#  / ___| __ _ _ __ ___   ___
# | |  _ / _` | '_ ` _ \ / _ \
# | |_| | (_| | | | | | |  __/
#  \____|\__,_|_| |_| |_|\___|

def game_main_loop():
    """
    Loop the main game
    """
    game_quit = False

    while not game_quit:
        # get player input
        events_list = pygame.event.get()

        for event in events_list:  # loop through all events
            if event.type == pygame.QUIT:  # check if user closed window
                game_quit = True

        # draw the game
        draw_game()

    pygame.quit()
    exit()


def game_init():
    """
    Initialize the main game
    """
    global SURFACE_MAIN, GAME_MAP

    # initialize pygame
    pygame.init()

    # set surface dimensions
    # a resizeable game screen will have to be ammended later
    SURFACE_MAIN = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT))

    GAME_MAP = map_create()


#  _____                     _
# | ____|_  _____  ___ _   _| |_ ___
# |  _| \ \/ / _ \/ __| | | | __/ _ \
# | |___ >  <  __/ (__| |_| | ||  __/
# |_____/_/\_\___|\___|\__,_|\__\___|

if __name__ == '__main__':
    game_init()
    game_main_loop()
