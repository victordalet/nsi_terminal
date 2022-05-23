def moyenne(tab):
	if tab == []:
		return 'erreur'
	resultat = 0
	for i in tab:
		resultat += i
	return resultat/len(tab)

def main():
	print(moyenne([1,2,3,4,5,6,7,8,9,10]))
	print(moyenne([]))

main()