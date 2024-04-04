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
        if S_time() < to_stamp(Config.start): 
            remove_unnecessary_files()
            coords = [(x,y) for x in range(Config.SCREEN_WIDTH) for y in range(Config.SCREEN_HEIGHT)]
            random.shuffle(coords)
            store_in_file(coords, "coordonnees")
            store_in_file(0, "etape")
            rate, decimal, fps = speed()
            planificateur = sched.scheduler(time.time, time.sleep)
            planificateur.enterabs(Config.start, 1, draw)
            print("ready")
            planificateur.run()
        else:
            coords = get_content("coordonnees")
            etape = get_content("etape")
            #afficher draw2.0
            rate, decimal, fps = speed()
            print("restarting")
            draw()

    def draw():
        global notfull, etape
        if S_time() >= to_stamp(Config.start) and S_time() <= to_stamp (Config.end): 
            coords = get_content("coordonnees")
            etape =  get_content("etape")
            if etape >= len(coords) : 
                quit()
            x, y = coords[etape]
            try:
                imagefile2 = os.path.join('data', Config.image2)
                surf2 = pygame.image.load(imagefile2)
            except IOError as e:
                print(f"{str(e)}")
                quit()
            display.blit(surf2, (x,y))
            pygame.display.update()
            notfull += decimal 
            if add_pixel(notfull, decimal): 
                etape += 1 
                store_in_file (etape, "etape")
                notfull -= 1
            store_in_file (notfull, "notfull")
            time.sleep(1/ Config.desired_fps)
            draw()

    # lancer le programme au bon moment
    #   decimal à notfull (if notfull > 1: notfull -= 1, changement = True)
    #   ajouter les pixels + 1 if changement == True
    #   stoquer étape (store in file)
    #   changement = False
