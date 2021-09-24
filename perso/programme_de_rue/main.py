import turtle
from street import *
from shapes import *
def main():
	line(-400,-1)
	##################### creation of apartments (launch of the calsse __init__) #####################
	apartmentBuilding1 = apartmentBuilding()
	apartmentBuilding2 = apartmentBuilding()
	apartmentBuilding3 = apartmentBuilding()
	apartmentBuilding4 = apartmentBuilding()
	apartmentBuilding5 = apartmentBuilding()
	##################### construction of apartments (launch of the calsse construction) #####################
	apartmentBuilding1.construction(-400)
	apartmentBuilding2.construction(-200)
	apartmentBuilding3.construction(0)
	apartmentBuilding4.construction(200)
	apartmentBuilding5.construction(400)
	##################### final observation time #####################
	turtle.mainloop()

main()