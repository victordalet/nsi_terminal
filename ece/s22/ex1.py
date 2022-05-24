def reverse(chaine):
	chaine_reverse = ''
	for i in chaine:
		chaine_reverse = str(i) + chaine_reverse
	return chaine_reverse



def main():
	print(reverse("euqitamrofni"))

main()