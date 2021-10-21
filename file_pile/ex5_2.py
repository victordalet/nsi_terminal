def creer_file():
	return []

def emfiler(F,element):
	F.append(element)

def defiler(F):
	F.pop(0)
	try : 
		return F[0]
	except :
		return None

def est_vide(F):
	if F == [] :
		return True
	return False


def main():
	F = creer_file()
	emfiler(F,5)
	emfiler(F,9)
	print(F)
	while est_vide(F) == False:
		defiler(F)
	print(F)

main()
