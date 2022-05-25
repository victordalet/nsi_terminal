def moyenne(lst):
	somme = 0
	for i in lst:
		somme += i
	return somme/len(lst)

def main():
	print(moyenne([1.0, 2.0, 4.0]))

main()