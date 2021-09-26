import turtle
from street import *
from shapes import *
from background import *
def main():
	turtle.title("programme de rue")
	line(-700,-300,1340)
	##################### creation of apartments (launch of the calsse __init__) #####################
	apartmentBuilding1 = apartmentBuilding()
	apartmentBuilding2 = apartmentBuilding()
	apartmentBuilding3 = apartmentBuilding()
	apartmentBuilding4 = apartmentBuilding()
	apartmentBuilding5 = apartmentBuilding()
	apartmentBuilding6 = apartmentBuilding()
	apartmentBuilding7 = apartmentBuilding()
	##################### construction of apartments (launch of the calsse construction) #####################
	apartmentBuilding1.construction(-700)
	apartmentBuilding2.construction(-500)
	apartmentBuilding3.construction(-300)
	apartmentBuilding4.construction(-100)
	apartmentBuilding5.construction(100)
	apartmentBuilding6.construction(300)
	apartmentBuilding7.construction(500)
	##################### cconstruction and observation of bakcground #####################
	background_final = Background()
	background_final.construction()
	background_final.day(20)
	##################### final observation time #####################
	turtle.mainloop()


main()