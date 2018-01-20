import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

'''In alien ivasion, the player controls a ship that appears at the bottom center of the screen. The player can move the ship right and left using the arrow keys and shoot bullets using the spacebar. When the game begins, a fleet of aliens fills the sky and moves across the and down the screen. the player shoots and destroys the aliens.if the player shoots all the aliens, a new fleet appears that moves faster than the previous fleet. if any alien hits the payers ship or reaches the bottom of the screen, the player loses a ship. if the player loses three ships, the game ends.'''

def run_game():
    # Initialze thr game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Dave Greene's Alien Invasion")

    # set the background color.
    bg_color = (230,230,230)

    # make a ship 
    ship = Ship(screen)
    # Start with the Main Loop for the game.
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

    

run_game()

        


    
