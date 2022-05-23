def nombre_de_mots(phrase):
	nb_mot = 0 
	for i in range(len(phrase)-1):
		if phrase[i] == ' ' and phrase[i-1] != ' ':
			nb_mot += 1
	return nb_mot

def main():
	print(nombre_de_mots('Le point d exclamation est separe !'))
	print(nombre_de_mots('Il y a un seul espace entre les mots !'))

main()