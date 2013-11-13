import sys
from easyPygame import *
from pygame.locals import *

def close(loop):
    loop.stop()

def jump(loop):
    print("Et Hop !")

def right(loop):
    sprite = loop.Window.findByName("mario")
    sprite.move(loop.Window , 10, 0)

def left(loop):
    sprite = loop.Window.findByName("mario")
    sprite.move(loop.Window , -10, 0)

def up(loop):
    sprite = loop.Window.findByName("mario")
    sprite.move(loop.Window , 0, -10)
   
def down(loop):
    sprite = loop.Window.findByName("mario")
    sprite.move(loop.Window , 0, 10)

def hide(loop):
    sprite = loop.Window.findByName("mario")
    sprite.visible = False
    loop.Window.update()

def unHide(loop):
    sprite = loop.Window.findByName("mario")
    sprite.visible = True
    loop.Window.update()

handler = eventHandler()
handler.addEvent(close, QUIT)
handler.addEvent(close, K_ESCAPE)
handler.addEvent(jump, K_SPACE)
handler.addEvent(up , K_UP)
handler.addEvent(down , K_DOWN)
handler.addEvent(left , K_LEFT)
handler.addEvent(right , K_RIGHT)
handler.addEvent(hide, K_h)
handler.addEvent(unHide, K_u)
