def recherche(tab):
	resultat = []
	for i in range(1,len(tab)):
		if tab[i] == tab[i-1]+1:
			resultat.append([tab[i-1],tab[i]])
	return resultat

def main():
	print(recherche([1, 4, 3, 5]))
	print(recherche([1, 4, 5, 3]))
	print(recherche([7, 1, 2, 5, 3, 4]))
	print(recherche([5, 1, 2, 3, 8, -5, -4, 7]))

main()
