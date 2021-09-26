import time
import turtle

from shapes import *

##################### class that will create the background #####################
class Background:
    def __init__(self):
        self.color_sun = (255,255,0)
        self.color_moon = (227,222,218)
        self.color_cloud = (200,200,200)
        self.list_color_sky = [(8,192,254),(8,172,254),(8,152,254),(8,132,254),(8,112,254),(8,92,254),(8,72,254),(8,52,254),(8,32,254),(8,12,254),(0,4,224),(1,5,195),(2,5,155),
                               (2,4,114),(1,3,96),(0,1,63)]
        self.list_color_sky_reverse = [(0,1,63),(1,33,96),(2,4,114),(2,5,155),(1,5,195),(8,12,254),(8,32,254),(8,52,254),(8,72,254),(8,92,254),(8,112,254),(8,132,254),(8,152,254),
                                       (8,172,254),(8,192,254)]
        self.position_starX = -300
        self.position_starY = 300

    def construction(self):
        cloud1 = cloud(self.color_cloud)
        cloud2 = cloud(self.color_cloud)
        cloud3 = cloud(self.color_cloud)
        cloud4 = cloud(self.color_cloud)
        cloud1.construction(-400,250,40)
        cloud2.construction(0,250,30)
        cloud3.construction(400, 250,40)
        cloud4.construction(700, 250,20)

    def day(self,number_of_days):
        for days in range(number_of_days):
            circle(30, 360, self.color_sun, self.position_starX, self.position_starY)
            for sky_day_night in self.list_color_sky:
                turtle.Screen().bgcolor(sky_day_night)
                time.sleep(0.1)
            circle(30, 360, self.color_moon, self.position_starX, self.position_starY)
            for sky_night_day in self.list_color_sky_reverse:
                turtle.Screen().bgcolor(sky_night_day)
                time.sleep(0.1)


##################### class that will create clouds #####################
class cloud:
    def __init__(self,color):
        self.color = color

    def construction(self,positionX,positionY,len):
        shapes_cloud(positionX,positionY,self.color,len)
