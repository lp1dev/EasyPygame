import pygame
import sys
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

class sprite(object):
    def __init__(self, path, x , y, colorkey):
        self.path = path;
        self.x = x;
        self.y = y;
        self.image = pygame.image.load(path).convert()
        self.colorkey = colorkey

    def show(self, Window):
        self.image.set_colorkey(self.colorkey)
        Window.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self, window, x, y):
        self.x = self.x + x;
        self.y = self.y + y;
        window.Window.blit(self.image, (self.x , self.y))
        pygame.display.flip()

class loop(object):
    def __init__(self, eventHandler, Window):
        self.eventHandler = eventHandler
        self.Window = Window
        go_on = 1
        while (go_on):
            for event in pygame.event.get():
                if (event.type == KEYDOWN):
                    self.eventHandler.handle(event.key, self)
                else:
                    self.eventHandler.handle(event.type, self)
            self.do_nothing()

    def do_nothing(self):
        self.go_on = 1
    
    def stop(self):
        sys.exit(0)

class window(object):
    def __init__(self, width, height, title, icon):
        self.sprites = []
        self.width = width
        self.height = height
        self.title = title
        self.icon = pygame.image.load(icon)
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption(self.title)

    def addSprite(self, sprite):
        self.sprites.append(sprite)
        sprite.show(self.Window)
        
    def setBackgroundColor(self, r, g ,b):
        self.background = pygame.Surface(self.Window.get_size())
        self.background = self.background.convert()
        self.background.fill((r, g, b))
        self.Window.blit(self.background, (0, 0))
        pygame.display.flip()

    def printText(self, Text, x , y):
        font = pygame.font.Font(None, 36)
        text = font.render(Text, 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        self.Window.blit(text, (x ,y))
        pygame.display.flip()
      
    def loop(self, eh):
        self.loop = loop(eh, self)

    def show(self):
        self.Window = pygame.display.set_mode((self.width, self.height))

    def setEventHandler(EventHandler):
        self.eventHandler = EventHandler

    def getWindow(self):
        return self
