def rendu(somme_a_rendre):
	n = [0,0,0]
	pieces = [5,2,1]
	somme = 0
	for i in range(len(pieces)):
		while somme+pieces[i] <= somme_a_rendre:
			somme += pieces[i]
			n[i] += 1
	return n

def main():
	print(rendu(13))
	print(rendu(64))

main()
