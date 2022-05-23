def correspond(mot,mot_a_trous):
	mot = list(mot)
	mot_a_trous = list(mot_a_trous)
	for i in range(len(mot_a_trous)):
		if mot_a_trous[i] == '*':
			mot_a_trous[i] = mot[i]
	if mot == mot_a_trous:
		return True
	return False

def main():
	print(correspond('INFORMATIQUE', 'INFO*MA*IQUE'))
	print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE'))

main()