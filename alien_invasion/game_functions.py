import sys
import pygame


def check_events():
    """ respond to key presses and mouse events"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen"""
    #redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # Make the most recently dran screen visible.abs
    pygame.display.flip()