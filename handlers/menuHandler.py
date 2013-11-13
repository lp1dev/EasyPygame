import sys
sys.path.append("../easyPygame")
from easyPygame import *
from pygame.locals import *

def close(loop):
    loop.stop()

def printBuf(loop):
    loop.Window.findByName("buffer").setText(loop.Buffer)
    loop.Window.update()

handler = eventHandler()
handler.addEvent(close, QUIT)
handler.addEvent(printBuf, KEYDOWN)
handler.addEvent(close, K_ESCAPE)

