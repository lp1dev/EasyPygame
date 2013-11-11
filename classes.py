import pygame
from pygame.locals import *

class loop(object):
    def do_nothing(self):
        self.go_on = 1
    def __init__(self):
        go_on = 1
        while (go_on):
            self.do_nothing()

class window(object):
    def __init__(self, width, height, title, icon):
        self.width = width
        self.height = height
        self.title = title
        self.icon = pygame.image.load(icon)
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption(self.title)

    def loop(self):
        self.loop = loop()

    def show(self):
        Window = pygame.display.set_mode((self.width, self.height))
