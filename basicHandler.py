import sys
from classes import *
from pygame.locals import *

def close(loop):
    sys.exit()

def jump(loop):
    print("Et Hop !")

def right(loop):
    loop.Window.sprites[0].move(loop.Window , 10, 0)

def left(loop):
    loop.Window.sprites[0].move(loop.Window , -10, 0)

def up(loop):
    loop.Window.sprites[0].move(loop.Window , 0, -10)
    
def down(loop):
    print("let's go!")
    loop.Window.sprites[0].move(loop.Window , 0, 10)

handler = eventHandler()
handler.addEvent(close, QUIT)
handler.addEvent(close, K_ESCAPE)
handler.addEvent(jump, K_SPACE)
handler.addEvent(up , K_UP)
handler.addEvent(down , K_DOWN)
handler.addEvent(left , K_LEFT)
handler.addEvent(right , K_RIGHT)
