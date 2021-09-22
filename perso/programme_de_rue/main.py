import time
from street import *
def main():

	apartmentBuilding1 = apartmentBuilding()
	apartmentBuilding2 = apartmentBuilding()
	apartmentBuilding1.construction(0)
	apartmentBuilding2.construction(150)
	time.sleep(5)

main()