from color import *
from shapes import *
from opening import *


class groundFloor(generateColor):
    def __init__(self):
        self.height = 140
        self.width = 60
        super().__init__()

    def construction(self,multiplierX):
        positionX, positionY = turtle.pos()
        rectangle(self.width, self.height, self.randomColor,multiplierX,0)
        window1 = window()
        window2 = window()
        door1 = door()
        window1.construction(23+multiplierX,0)
        window2.construction(115+multiplierX,0)
        door1.construction(69+multiplierX,0)


class floor(generateColor):
    def __init__(self):
        self.height = 140
        self.width = 60
        super().__init__()

    def construction(self,multiplierX,multiplierY):
        positionX, positionY = turtle.pos()
        rectangle(self.width,self.height,self.randomColor,multiplierX,multiplierY)
        window1 = window()
        window2 = window()
        window3 = window()
        window1.construction(23+multiplierX,multiplierY)
        window2.construction(69+multiplierX,multiplierY)
        window3.construction(115+multiplierX,multiplierY)

class roof(generateColor):
    def __init__(self):
        self.length = 140
        super().__init__()

    def construction(self,multiplierX,multiplierY):
        positionX, positionY = turtle.pos()
        triangle(self.length,self.randomColor,multiplierX,multiplierY)
