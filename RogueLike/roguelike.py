#3rd party modules
import tcod as libtcod
import pygame

# game files
import constants

def draw_game():

    global SURFACE_MAIN

    # TODO clear the surface
    SURFACE_MAIN.fill()

    # TODO draw the map

    # TODO draw the character

    # update the display
    pygame.display.flip()



def game_main_loop():
    """
    Loops the main game
    """

    game_quit = False

    while not game_quit:

        #TODO get player input
        events_list = pygame.event.get()

        #TODO process input
        for event in events_list:
            if event.type == pygame.QUIT:
                game_quit = True

        #TODO draw the game

    # quit the game
    pygame.quit()
    exit()




def game_init():
    """
    Initializes the main window
    """
    global SURFACE_MAIN

    #initialize pygame
    pygame.init()

    # global variable (set height and width (800, 600))
    SURFACE_MAIN = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT))


if __name__ == "main":
    game_init()
    game_main_loop()
