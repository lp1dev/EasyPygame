import sys
from classes import *
from pygame.locals import *

def close():
    sys.exit()

def jump():
    print("Et Hop !")

functs = [close, close, jump]
keys = [QUIT, K_ESCAPE, K_SPACE]

handler = eventHandler(functs, keys)
