import time
from street import *
def main():
	##################### creation of apartments (launch of the calsse __init__) #####################
	apartmentBuilding1 = apartmentBuilding()
	apartmentBuilding2 = apartmentBuilding()
	apartmentBuilding3 = apartmentBuilding()
	apartmentBuilding4 = apartmentBuilding()
	apartmentBuilding5 = apartmentBuilding()
	##################### construction of apartments (launch of the calsse construction) #####################
	apartmentBuilding1.construction(0)
	apartmentBuilding2.construction(150)
	apartmentBuilding3.construction(300)
	apartmentBuilding4.construction(450)
	apartmentBuilding5.construction(600)
	##################### final observation time #####################
	time.sleep(5)

main()