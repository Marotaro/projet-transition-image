import pygame
import sys
import os
import random
import time
import random

from pygame.locals import *

class Config:
    SCREEN_WIDTH = 1595
    SCREEN_HEIGHT = 897
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
    desired_fps = 1
    saut = 100000
    
    
def quit():
    pygame.quit()
    sys.exit()

def main():
    # Create a clock object
    clock = pygame.time.Clock()
    pygame.init()
    display = pygame.display.set_mode(Config.SCREEN_SIZE)
    try:
        imagefile1 = os.path.join('data', 'image1.jpg')
        imagefile2 = os.path.join('data', 'image2.jpg')
        surf1 = pygame.image.load(imagefile1)
        surf2 = pygame.image.load(imagefile2)
    except IOError as e:
        print(f"{str(e)}")
        quit()
        
    nb_pixels = Config.SCREEN_HEIGHT * Config.SCREEN_WIDTH
    coords = [(x,y) for x in range(Config.SCREEN_WIDTH) for y in range(Config.SCREEN_HEIGHT)]
    random.shuffle(coords)
    print("nb pixels", nb_pixels)
        
    # Start the main loop
    while True:
        etape = 0
        # Get events from the event queue
        for event in pygame.event.get():
            # Check for the quit event
            if event.type == pygame.QUIT:
                quit()
            
            if event.type == pygame.KEYUP:
                # quit when Q is pressed
                if event.key == K_q:
                    quit()

        for coord in coords[(Config.saut*etape):Config.saut+(Config.saut*etape)]:            
            color = surf2.get_at(coord)
            surf1.set_at(coord, color)
        etape += 1 

        # Update the game state
        display.blit(surf1, (0, 0))
        
        # Draw the game screen
        pygame.display.update()

        # Limit the FPS by sleeping for the remainder of the frame time

        clock.tick(Config.desired_fps)
        
main()