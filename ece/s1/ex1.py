def recherche(caractere,mot):
	nb_caractere = 0
	for i in mot:
		if i == caractere:
			nb_caractere += 1
	return nb_caractere

def main():
	print(recherche('e', "sciences"))
	print(recherche('i',"mississippi"))
	print(recherche('a',"mississippi"))

main()
