from color import *
from shapes import *
from opening import *


class groundFloor(generateColor):
    def __init__(self):
        self.height = 140
        self.width = 60
        super().__init__()

    def construction(self):
        positionX, positionY = turtle.pos()
        rectangle(self.width, self.height, self.randomColor,positionX,positionY)
        window1 = window()
        window2 = window()
        door1 = door()
        window1.construction(1)
        window2.construction(10)
        door1.construction(5)


class floor(generateColor):
    def __init__(self):
        self.height = 140
        self.width = 60
        generateColor.__init__(self)

    def construction(self):
        positionX, positionY = turtle.pos()
        rectangle(self.width,self.height,self.randomColor,positionX+200,positionY+60)
        window1 = window()
        window2 = window()
        window3 = window()
        window1.construction(1)
        window2.construction(5)
        window3.construction(10)

class roof(generateColor):
    def __init__(self):
        self.length = 140
        super().__init__()

    def construction(self):
        positionX, positionY = turtle.pos()
        triangle(self.length,self.randomColor,positionX,positionY+60)
