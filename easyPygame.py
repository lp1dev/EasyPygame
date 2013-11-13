import pygame
import sys
from elements import *
from pygame.locals import *

class eventHandler():
    def __init__(self):
        self.functions = []
        self.keys = []

    def addEvent(self, function, key):
        self.keys.append(key)
        self.functions.append(function)

    def handle(self, key, loop):
        self.loop = loop
#       print(key)
        if key in self.keys:
            self.functions[self.keys.index(key)](loop)

class loop(object):
    def __init__(self, eventHandler, Window):
        pygame.key.set_repeat(100, 100)
        self.eventHandler = eventHandler
        self.Window = Window
        self.go_on = 1
        while (self.go_on):
            for event in pygame.event.get():
                if (event.type == KEYDOWN):
                    self.eventHandler.handle(event.key, self)
                else:
                    self.eventHandler.handle(event.type, self)

    def stop(self):
        self.go_on = 0

class window(object):
    def __init__(self, width, height, title, icon):
        self.sprites = []
        self.texts = []
        self.width = width
        self.height = height
        self.title = title
        self.icon = pygame.image.load(icon)
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption(self.title)

    def addSprite(self, sprite):
        self.sprites.append(sprite)
        self.update()
        
    def addText(self, text):
        self.texts.append(text)
        self.update()
      
    def update(self):
        self.Window.blit(self.background, (0, 0))
        for text in self.texts:
            if (text.visible == True):
                self.Window.blit(text.surface, (text.x, text.y))
        for sprite in self.sprites:
            if (sprite.visible == True):
                self.Window.blit(sprite.image, (sprite.x, sprite.y))
        pygame.display.flip()

    def setBackgroundColor(self, r, g ,b):
        self.background = pygame.Surface(self.Window.get_size())
        self.background = self.background.convert()
        self.background.fill((r, g, b))
        self.update()
      
    def loop(self, eh):
        self.loop = loop(eh, self)

    def show(self):
        self.Window = pygame.display.set_mode((self.width, self.height))

    def setEventHandler(EventHandler):
        self.eventHandler = EventHandler

    def getWindow(self):
        return self
