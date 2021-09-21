import time
from street import *
def main():

	apartmentBuilding1 = apartmentBuilding()
	apartmentBuilding2 = apartmentBuilding()
	apartmentBuilding1.construction()
	apartmentBuilding2.construction()
	time.sleep(5)

main()