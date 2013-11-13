import pygame
import sys
import colors
from elements import *
from pygame.locals import *

class eventHandler():
    def __init__(self):
        self.functions = []
        self.keys = []
        self.mouseFunctions = []
      
    def addEvent(self, function, key):
        self.keys.append(key)
        self.functions.append(function)

    def handle(self, key, loop):
        self.loop = loop
        if key in self.keys:
            self.functions[self.keys.index(key)](loop)
            
    def handleMouse(self, button, pos, loop):
        self.loop = loop
        for elem in loop.Window.elems:
            if elem.surface.get_rect().collidepoint(pos) and button == 1:
                elem.onClick(loop.Window)
        
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
                if (event.type == MOUSEBUTTONDOWN):
                    self.eventHandler.handleMouse(event.button, pygame.mouse.get_pos(), self)
                else:
                    self.eventHandler.handle(event.type, self)

    def stop(self):
        self.go_on = 0

class window(object):
    def __init__(self, width, height, title, icon):
        self.elems = []
        self.width = width
        self.height = height
        self.title = title
        self.icon = pygame.image.load(icon)
        self.size = (width, height)
        self.background = pygame.Surface(self.size)
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption(self.title)

    def findByName(self, name):
        for elem in self.elems:
            if elem.name == name:
                return elem

    def addButton(self, button):
        self.elems.append(button)
        self.update()

    def addSprite(self, sprite):
        self.elems.append(sprite)
        self.update()
        
    def addText(self, text):
        self.elems.append(text)
        self.update()
      
    def update(self):
        self.Window.blit(self.background, (0, 0))
        for elem in self.elems:
            if (elem.visible == True):
                self.Window.blit(elem.surface, elem.pos)
        pygame.display.flip()

    def setBackgroundColor(self, color):
        self.background = pygame.Surface(self.Window.get_size())
        self.background = self.background.convert()
        self.background.fill(color)
        self.update()
      
    def loop(self, handler):
        self.loop = loop(handler, self)

    def show(self):
        self.Window = pygame.display.set_mode((self.width, self.height))
