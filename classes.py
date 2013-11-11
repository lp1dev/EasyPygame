import pygame
import sys
from pygame.locals import *

class eventHandler():
    def __init__(self, functions, keys):
        self.functions = functions
        self.keys = keys

    def handle(self, key):
        print(key)
        if key in self.keys:
            self.functions[self.keys.index(key)]()

class loop(object):
    def __init__(self, eventHandler):
        self.eventHandler = eventHandler
        go_on = 1
        while (go_on):
            for event in pygame.event.get():
                if (event.type == KEYDOWN):
                    self.eventHandler.handle(event.key)
                else:
                    self.eventHandler.handle(event.type)
            self.do_nothing()

    def do_nothing(self):
        self.go_on = 1

    def stop(self):
        sys.exit(0)

class window(object):
    def __init__(self, width, height, title, icon):
        self.width = width
        self.height = height
        self.title = title
        self.icon = pygame.image.load(icon)
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption(self.title)

    def reload(self):
        self.Window.blit(self.background, (0, 0))
        pygame.display.flip()

    def setBackgroundColor(self, r, g ,b):
        self.background = pygame.Surface(self.Window.get_size())
        self.background = self.background.convert()
        self.background.fill((r, g, b))
        self.reload()

    def printText(self, Text):
        font = pygame.font.Font(None, 36)
        text = font.render(Text, 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        self.background.blit(text, (0,0))
      
    def loop(self, eh):
        self.loop = loop(eh)

    def show(self):
        self.Window = pygame.display.set_mode((self.width, self.height))

    def setEventHandler(EventHandler):
        self.eventHandler = EventHandler
