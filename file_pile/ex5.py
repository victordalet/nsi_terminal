def creer_pile():
	return []

def empiler(P,element):
	P.append(element)

def depiler(P):
	P.pop(-1)
	try : 
		return P[-1]
	except :
		return None

def est_vide(P):
	if P == [] :
		return True
	return False


def main():
	P = creer_pile()
	empiler(P,5)
	empiler(P,9)
	print(P)
	while est_vide(P) == False:
		depiler(P)
	print(P)

main()