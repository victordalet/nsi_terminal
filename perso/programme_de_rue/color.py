import random
##################### class that generates a random color rgb in binary (this class is used in other class) #####################
class generateColor:
    def __init__(self):
        self.randomColor_red = random.randint(1,255)
        self.randomColor_green = random.randint(1, 255)
        self.randomColor_blue = random.randint(1, 255)
        self.randomColor = (self.randomColor_red,self.randomColor_green,self.randomColor_blue)