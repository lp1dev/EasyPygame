import sys
sys.path.append("../easyPygame")
from easyPygame import *
from pygame.locals import *

def close(loop):
    loop.stop()

def right(loop):
    sprite = loop.Window.findByName("pikachu")
    sprite.move(loop.Window , 10, 0)

def left(loop):
    sprite = loop.Window.findByName("pikachu")
    sprite.move(loop.Window , -10, 0)

def jump(loop):
    sprite = loop.Window.findByName("pikachu")
    i = 0
    while (i < 30):
        sprite.move(loop.Window , 0, -5)
        i = i + 1
    while (i > 0):
        sprite.move(loop.Window , 0, 5)
        i = i - 1
   
def hide(loop):
    sprite = loop.Window.findByName("pikachu")
    sprite.visible = False
    loop.Window.update()

def unHide(loop):
    sprite = loop.Window.findByName("pikachu")
    sprite.visible = True
    loop.Window.update()

handler = eventHandler()
handler.addEvent(close, QUIT)
handler.addEvent(close, K_ESCAPE)
handler.addEvent(jump , K_UP)
handler.addEvent(left , K_LEFT)
handler.addEvent(right , K_RIGHT)
handler.addEvent(hide, K_h)
handler.addEvent(unHide, K_u)
