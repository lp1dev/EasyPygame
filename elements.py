import pygame
from pygame.locals import *

class text(object):
    def __init__(self, text, x, y, color, size):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.font = pygame.font.Font(None, self.size)
        self.surface = self.font.render(text, 1, (color))
        self.visible = True

class sprite(object):
    def __init__(self, path, x , y, colorkey):
        self.path = path;
        self.x = x;
        self.y = y;
        self.image = pygame.image.load(path).convert()
        self.colorkey = colorkey
        self.image.set_colorkey(colorkey)
        self.visible = True

    def move(self, window, x, y):
        self.x = self.x + x;
        self.y = self.y + y;
        window.update()
