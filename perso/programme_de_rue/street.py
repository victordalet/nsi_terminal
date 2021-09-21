import random
from floors import *
from opening import *

class apartmentBuilding:
    def __init__(self):
        self.number_of_floor = random.randint(1, 5)

    def construction(self):
        floor1 = groundFloor()
        floor2 = groundFloor()
        roof1 = roof()
        floor1.construction()
        for i in range(self.number_of_floor):
            floor2.construction()
        roof1.construction()




