#!/usr/bin/python2

import sys
sys.path.append("easyPygame")
sys.path.append("handlers")
import pygame
import basicHandler
import menuHandler
from easyPygame import *
from pygame.locals import *

def stop(loop):
    loop.stop()

def play(loop):
    stop(loop)
    w = window(640, 480, "sampleGame", "res/icon.png")
    w.addSprite(sprite("back", "res/level.png", -150, 0, colors.blue))
    w.addSprite(sprite("pikachu", "res/sprite.png", 100, 355, colors.white))
    loop.setKeyRepeat(70, 70)
    w.loop(basicHandler.handler)

def menu():
    w = window(640, 480, "sampleGame", "res/icon.png")
    w.addSprite(sprite("back" ,"res/back.png", 0, 0, colors.blue))
    w.addText(text("title", "sampleGame 0.1", 0, 0, colors.white, 42))
    w.addButton(button("play", "play", "res/buttonbg.png", 55,100, colors.white))
    w.addButton(button("exit", "exit", "res/buttonbg.png", 55,250, colors.white))
    w.findByName("play").onClick = play
    w.findByName("exit").onClick = stop
    w.input = True
    w.setKeyRepeat(70, 70)
    w.addText(text("buffer", "",0,400, colors.black, 34))
    w.loop(menuHandler.handler)

def main():
    pygame.init()
    menu();

main()
