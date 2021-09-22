from shapes import *
from color import *

class window:
    def __init__(self):
        self.height = 30
        self.color = (255,255,255)

    def construction(self,multiplierX,multiplierY):
        positionX,positionY = turtle.pos()
        square(self.height,self.color,multiplierX,multiplierY+10)

class door(generateColor):
    def __init__(self):
        self.height = 50
        self.width = 30
        super().__init__()

    def construction(self,multiplierX,multiplierY):
        positionX,positionY = turtle.pos()
        rectangle(self.height,self.width,self.randomColor,multiplierX,0)

