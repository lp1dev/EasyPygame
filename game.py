#!/usr/bin/python

import pygame
import basicHandler
from classes import *
from pygame.locals import *

pygame.init()

def main():
    w = window(1000, 1000, "EasyPygame", "res/icon.png")
    w.show()
    w.setBackgroundColor(187, 210, 225);
    w.printText("coucou", 10 , 10)
    w.addSprite(sprite("res/sprite.png", 40, 70))
    w.loop(basicHandler.handler)
main();
