import time
from shapes import *


##################### class that will create the background #####################
class Background:
    def __init__(self):
        self.color_sky = (45,227,226)
        self.color_sun = (255,255,0)
        self.color_moon = (227,222,218)
        self.color_cloud = (240,240,240)
        self.list_color_sky = [(8,192,254),(8,172,254),(8,152,254),(8,132,254),(8,112,254),(8,92,254),(8,72,254),(8,52,254),(8,32,254),(8,12,254),(51,0,184),(26,1,90),(13,0,48)]
        self.len_list_color_sky = len(self.list_color_sky)
        self.position_starX = 50
        self.position_starY = 50

    def construction(self):
        cloud1 = cloud(self.color_cloud)
        cloud2 = cloud(self.color_cloud)
        cloud3 = cloud(self.color_cloud)
        cloud4 = cloud(self.color_cloud)
        cloud1.construction(-600,400)
        cloud2.construction(-200, 400)
        cloud3.construction(200, 40)
        cloud4.construction(600, 400)

    def day(self,number_of_days):
        for days in range(number_of_days):
            for i in self.list_color_sky:
                turtle.Screen().bgcolor(i)
                time.sleep(0.1)
                if len(i) < self.len_list_color_sky/2:
                    circle(30,360,self.color_sun,self.position_starX,self.position_starY)
                else:
                    circle(30,180,self.color_moon,self.position_starX,self.position_starY)


##################### class that will create clouds #####################
class cloud:
    def __init__(self,color):
        self.color = color

    def construction(self,positionX,positionY):
        shapes_cloud(positionX,positionY,self.color)

