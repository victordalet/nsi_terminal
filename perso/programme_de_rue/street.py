from floors import *
from opening import *

##################### class that will create apartments #####################

class apartmentBuilding:
    def __init__(self):
        ##################### we look for the number of floors to be created #####################
        self.number_of_floor = random.randint(1, 4)
        self.multiplierY = -300

    def construction(self,multiplierX):
        ##################### creation of the ground floor, the floor and the roof #####################
        floor1 = groundFloor()
        floor2 = floor(floor1)
        roof1 = roof()
        floor1.construction(multiplierX,self.multiplierY)
        ##################### assembly of floors according to the predefined random number #####################
        for i in range(self.number_of_floor):
            floor2.construction(multiplierX,self.multiplierY+60*(i+1))
        roof1.construction(multiplierX,self.multiplierY+60*(i+1)+60)




