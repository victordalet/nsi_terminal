from shapes import *
from color import *
import random

##################### class that create windows from square #####################
class window:
    def __init__(self):
        self.height = 30
        self.width = 50
        self.color = (255,255,255)
        self.colorBlack = (00,00,00)

    def construction(self,multiplierX,multiplierY):
        random_window = random.randint(1,2)
        if random_window == 1:
            square(self.height,self.color,multiplierX,multiplierY+10)
        else:
            frenchWindow(self.color,self.colorBlack,multiplierX,multiplierY)

##################### class that create windows from rectangle #####################
class door(generateColor):
    def __init__(self):
        self.height = 50
        self.width = 30
        super().__init__()

    def construction(self,multiplierX,multiplierY):
        random_door = random.randint(1, 2)
        if random_door == 1 :
            rectangle(self.height,self.width,self.randomColor,multiplierX,0)
        else :
            rounded_rectangle(self.width,self.randomColor,multiplierX,0)

