import pygame
import pygame_menu
from random import randint
import math
import time
import sys
a = randint(1, 100)
pygame.init()
surface = pygame.display.set_mode((600, 400))
difficultgame = 0
def set_difficulty(value, difficulty):
    pass

def start_the_game():
    loop = 1
    difficultgame = 10
    while loop <= difficultgame:
        print('Question numéro : ' + str(loop))
        theinput = int(input('Entrez un nombre : '))
        if a == theinput:
            print('Vous avez gagné')
            print('Le nombre a deviner a été ' + str(a) + ' avec ' + str(loop) + ' chances !')
            time.sleep(6)
            break
            
        if theinput > a:
            print('Votre nombre est trop grand')
        elif theinput < a:
            print('Votre nombre est trop petit')
        if loop == difficultgame :
                print('Vous avez perdu')
                print('Le nombre a deviner a été ' + str(a) )
                time.sleep(6)
        loop += 1
    print('Veillez retourner sur le menu!') 

    pass

menu = pygame_menu.Menu(300, 400, 'Welcome',
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add_button('Jouer', start_the_game)
menu.add_button('Quiter', pygame_menu.events.EXIT)
menu.mainloop(surface)
