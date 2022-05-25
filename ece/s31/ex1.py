def recherche(a,lst):
	somme_a = 0
	for i in lst:
		if a==i:
			somme_a +=1
	return somme_a

def main():
	print(recherche(5,[-2, 5, 3, 5, 4, 5]))

main()