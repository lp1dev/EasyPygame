#!/usr/bin/python

import pygame
from classes import *
from pygame.locals import *

pygame.init()

def main():
    w = window(300, 300, "pyGameEditor", "icon.bmp")
    w.show()
    w.loop()
main();
