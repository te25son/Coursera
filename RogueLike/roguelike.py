# 3rd Party Modules
import pygame
import tcod as libtcod

# game files
import constants

def draw_game():
    global SURFACE_MAIN

    # clear the surface
    SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)

    # TODO: draw the map

    # draw the character
    SURFACE_MAIN.blit(constants.S_PLAYER, (200, 200))

    # update the display
    pygame.display.flip()


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
    global SURFACE_MAIN

    # initialize pygame
    pygame.init()

    # set surface dimensions
    # a resizeable game screen will have to be ammended later
    SURFACE_MAIN = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT))


# start game
if __name__ == '__main__':
    game_init()
    game_main_loop()
