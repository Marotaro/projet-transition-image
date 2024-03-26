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
from config import *

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



def main():
    # mise en place (affichage de l'image 1)
    def affichage():
        pygame.init()
        display = pygame.display.set_mode(Config.SCREEN_SIZE)
        try:
            imagefile1 = os.path.join('data', Config.image1)
            imagefile2 = os.path.join('data', Config.image1)
            surf1 = pygame.image.load(imagefile1)
            surf2 = pygame.image.load(imagefile2)
        except IOError as e:
            print(f"{str(e)}")
            quit()
            
        display.blit(surf1,(0,0))
        pygame.display.update()
        
    affichage(Config.SCREEN_SIZE)#données
    # première itération + en cas de crash: calcul du nbr de pixel par seconde par rapport au temps donné (nbr d'étape)
    def prepare():
        if S_time() < Config.start: #will change
            coords = [(x,y) for x in range(Config.SCREEN_WIDTH) for y in range(Config.SCREEN_HEIGHT)]
            random.shuffle(coords)
            befor_run(coords)
            etape = get_stage()
            rate, decimal, fps = speed()
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

    # lancer le programme au bon moment
    #   decimal à notfull (if notfull > 1: notfull -= 1, changement = True)
    #   ajouter les pixels + 1 if changement == True
    #   stoquer étape
    #   changement = False
