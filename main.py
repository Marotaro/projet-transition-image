import pygame
import sys
import os
import random
import time
import sched
import random
from t import *
from store import *

from pygame.locals import *

class Config:
    SCREEN_WIDTH = 1595
    SCREEN_HEIGHT = 897
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
    nb_pixels = SCREEN_HEIGHT * SCREEN_WIDTH
    start = to_stamp([2024,3,7,7,21])
    end = to_stamp([2024,3,7,7,30])

coords = []
etape = 0
saut = 0
notfull = 0
decimal = 0
fps = 0
restart = False


    
def quit():
    pygame.quit()
    sys.exit()


def prepar():
    global coords, etape, saut, notfull, decimal, fps, restart
    if S_time() < Config.start:
        coords = [(x,y) for x in range(Config.SCREEN_WIDTH) for y in range(Config.SCREEN_HEIGHT)]
        random.shuffle(coords)
        befor_run(coords)
        etape = get_stage()
        saut, decimal, fps = speed(len(coords), Config.start, Config.end)
        planificateur = sched.scheduler(time.time, time.sleep)
        planificateur.enterabs(Config.start,1,draw)
        print("ready")
        planificateur.run()
    else:
        coords = get_pixels()
        etape = get_stage()
        notfull = get_notfull()
        restart = True
        saut, decimal, fps = speed(len(coords), S_time(), Config.end)
        print("restarting")
        draw()

        

def draw():
    global coords, etape, saut, notfull, decimal, fps, restart
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
        

    display.blit(surf1,(0,0))
    pygame.display.update()


    print(restart)
    if restart:
        print(etape)
        for i in range(etape):
            color = surf2.get_at(coords[i])
            surf1.set_at(coords[i], color)
        display.blit(surf1, (0, 0))
        pygame.display.update()
        restart = False
        
    # Start the main loop
    while True:
        # Get events from the event queue
        for event in pygame.event.get():
            # Check for the quit event
            if event.type == pygame.QUIT:
                quit()
            
            if event.type == pygame.KEYUP:
                # quit when Q is pressed
                if event.key == K_q:
                    quit()




        notfull += decimal
        try:
            for i in range(saut + add_pixel(notfull, decimal)):
                color = surf2.get_at(coords[etape])
                surf1.set_at(coords[etape], color)
                etape += 1
                store_stage(etape)
        except:
            for coord in coords[etape:]:
                color = surf2.get_at(coords[etape])
                surf1.set_at(coords[etape], color)
        print(round(etape/Config.nb_pixels, 2)*100)
        if notfull > 1:
            notfull -= 1
        store_notfull(notfull)

        # Update the game state
        display.blit(surf1, (0, 0))
        
        # Draw the game screen
        pygame.display.update()

        # Limit the FPS by sleeping for the remainder of the frame time

        clock.tick(fps)
        
prepar()