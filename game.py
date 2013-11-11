#!/usr/bin/python

import pygame
import basicHandler
from classes import *
from pygame.locals import *


pygame.init()

def main():
    w = window(300, 300, "EasyPygame", "res/icon.png")
    w.show()
    w.setBackgroundColor(187, 210, 225);
    w.printText("coucou")
    w.loop(basicHandler.handler)

main();
