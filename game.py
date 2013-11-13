#!/usr/bin/python2

import pygame
import basicHandler
from easyPygame import *
from pygame.locals import *

def clickHandle(w):
    w.findByName("mario").visible = False
    w.update()

def main():
    pygame.init()
    w = window(1000, 1000, "EasyPygame", "res/icon.png")
    w.show()
    w.addSprite(sprite("back" ,"res/back.png", 0, 0, colors.blue))
    w.addSprite(sprite("mario", "res/sprite.png", 40, 70, colors.black))
    w.addButton(button("button1", "Selection 1", "res/buttonbg.png", 100,100, colors.white))
    w.addText(text("coucou", "Coucou", 0, 0, colors.white, 42))
    w.findByName("mario").onClick = clickHandle
    w.loop(basicHandler.handler)
main();
