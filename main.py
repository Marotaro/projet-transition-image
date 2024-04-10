import pygame
import sys
import os
import random
import random
from t import *
from store import *
from pygame.locals import *
from config import *


def quit():
    pygame.quit()
    sys.exit()


def main():
    # initialisation de pygame
    # affichage de la premier image (intacte)
    clock = pygame.time.Clock()
    pygame.init()
    display = pygame.display.set_mode(Config.SCREEN_SIZE)
    try:
        imagefile1 = os.path.join("data", Config.image1)
        imagefile2 = os.path.join("data", Config.image2)
        surf1 = pygame.image.load(imagefile1)
        surf2 = pygame.image.load(imagefile2)
    except IOError as e:
        print(f"{str(e)}")
        quit()

    display.blit(surf1, (0, 0))
    pygame.display.update()

    # définition variables "global"
    coords = []
    etape = 0
    rate = 0
    decimal = 0

    # Lea
    # permet de choisir ce que le programme doit effectuer en fonction du temps qu'il est
    ## si le temps est inférieur à celui de départ de la config le programme doit préparer
    ## les fichiers nécessaire à son fonctionnement et attend jusqu'au départ en rafraîchissant
    ## l'écran afin d'éviter que windows considère que le programme crash
    #
    ## si le temps est dépassé, le programme a crash, il rattrape la dernière étape enregistrée,
    ## recalcule la vitesse à la quelle il doit aller et recommence.
    def prepare():
        nonlocal rate, decimal, etape, coords
        if S_time() < to_stamp(Config.start):
            remove_unnecessary_files()
            coords = [
                (x, y)
                for x in range(Config.SCREEN_WIDTH)
                for y in range(Config.SCREEN_HEIGHT)
            ]
            random.shuffle(coords)
            store_in_file(coords, "coordonnees")
            etape = 0
            store_in_file(etape, "etape")
            rate, decimal, fps = speed(to_stamp(Config.start), etape)
            print("waiting")
            while S_time() < to_stamp(Config.start):
                print(f"t+{round(to_stamp(Config.start)-S_time())}")
                # Get events from the event queue
                for event in pygame.event.get():
                    # Check for the quit event
                    if event.type == pygame.QUIT:
                        quit()

                    if event.type == pygame.KEYUP:
                        # quit when Q is pressed
                        if event.key == K_q:
                            quit()
                pygame.display.update()
                clock.tick(1)
            print(f"starting at {rate} pixels per second")
            draw()
        else:
            coords = get_content("coordonnees")
            etape = get_content("etape")
            catchup()
            rate, decimal, fps = speed(S_time(), etape)
            print(f"restarting at {rate} pixels per second")
            draw()

    # Joana
    # permet d'affichier l'écran à l'étape donnée
    def catchup():
        for i in range(etape):
            color = surf2.get_at(coords[i])
            surf1.set_at(coords[i], color)
        display.blit(surf1, (0, 0))
        pygame.display.update()

    # Joana
    # permet de changer le nombre de pixels donnés de l'écran
    ## si le nombre n'est pas un nombre complet le programme attend
    ## de pouvoir changer un pixel de plus
    #
    ## si la liste des pixels a été parcouru et dépassé le programme change
    ## les pixels de la dernière étape réussite jusqu'à l'étape possible de fin
    def draw():
        nonlocal rate, decimal, etape, coords
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
            fl = 0
            extra = 0
            fl += decimal
            if fl > 1:
                fl -= 1
                extra = 1

            try:
                for i in range(rate + extra):
                    color = surf2.get_at(coords[etape + i])
                    surf1.set_at(coords[etape + i], color)
                etape += rate + extra
                store_in_file(etape, "etape")
                extra = 0
            except:
                for coord in coords[etape:]:
                    color = surf2.get_at(coords[etape])
                    surf1.set_at(coords[etape], color)
            # Update the game state
            display.blit(surf1, (0, 0))

            # Draw the game screen
            pygame.display.update()

            print(f"{round(etape/(Config.SCREEN_HEIGHT*Config.SCREEN_WIDTH)*100)}%")
            clock.tick(Config.desired_fps)

    prepare()


main()
