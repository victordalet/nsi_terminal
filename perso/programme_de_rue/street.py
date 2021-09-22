from floors import *
from opening import *

class apartmentBuilding:
    def __init__(self):
        self.number_of_floor = random.randint(2, 4)

    def construction(self,multiplierX):
        floor1 = groundFloor()
        floor2 = floor()
        roof1 = roof()
        floor1.construction(multiplierX)
        for i in range(self.number_of_floor):
            floor2.construction(multiplierX,60*(i+1))
        roof1.construction(multiplierX,60*(i+1)+60)




