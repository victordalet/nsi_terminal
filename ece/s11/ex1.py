def recherche(tab,n):
	debut = 0
	fin = len(tab)
	while debut <= fin:
		millieu = (fin+debut)//2
		if tab[millieu] == n:
			return millieu
		else:
			if n < tab[millieu]:
				fin = millieu-1
			else:
				debut = millieu+1
	return -1

def main():
	print(recherche([2, 3, 4, 5, 6], 5))
	print(recherche([2, 3, 4, 6, 7], 5))

main()