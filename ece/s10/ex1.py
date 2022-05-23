def occurence_lettres(phrase):
	dico = {}
	for i in phrase:
		dico[i] = 0
	for i in phrase:
		dico[i] += 1
	return dico

def main():
	print(occurence_lettres('Hello world !'))

main()