from opening import *
import random

##################### class that create the ground floor #####################
class groundFloor(generateColor):
    def __init__(self):
        self.height = 140
        self.width = 60
        ##################### heritage of the generateColor class to retrieve a color #####################
        super().__init__()

    def get_color(self):
        ##################### method for recovering the color for the rest of the apartment #####################
        return self.randomColor

    def construction(self,multiplierX,multiplierY):
        ##################### creating the twoo windows and the door #####################
        rectangle(self.width, self.height, self.randomColor,multiplierX,multiplierY)
        window1 = window()
        window2 = window()
        door1 = door()
        window1.construction(12.5+multiplierX,multiplierY)
        window2.construction(97.5+multiplierX,multiplierY)
        door1.construction(55+multiplierX,multiplierY)

##################### class that create the floor #####################
class floor(groundFloor):
    def __init__(self,floor1):
        super().__init__()
        self.color = floor1.get_color()

    def construction(self,multiplierX,multiplierY):
        ##################### creating the three windows #####################
        rectangle(self.width,self.height,self.color,multiplierX,multiplierY)
        window1 = window()
        window2 = window()
        window3 = window()
        window1.construction(12.5+multiplierX,multiplierY)
        window2.construction(55+multiplierX,multiplierY)
        window3.construction(97.5+multiplierX,multiplierY)

##################### class that create the roof #####################
class roof(generateColor):
    def __init__(self):
        self.width = 140
        self.height = 10
        super().__init__()

    def construction(self,multiplierX,multiplierY):
        ##################### choice of roof #####################
        type = random.randint(1,2)
        if type == 1:
            triangle(self.randomColor,multiplierX,multiplierY)
        else:
            rectangle(self.height,self.width,self.randomColor,multiplierX,multiplierY)
