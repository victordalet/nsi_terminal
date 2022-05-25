def recherche(elt,tab):
	for i in range(len(tab)):
		if tab[i] == elt:
			return i
	return -1

def main():
	print(recherche(1,[10,12,1,56]))

main()