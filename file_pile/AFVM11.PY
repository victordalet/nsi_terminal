def emfiler(F,element):
	queue = F[1]
	taille = F[2]
	if taille == nb_place:
		return False
	else:
		F[queue] = element
		if queue == nb_place+3:
			queue = 3
		else :
			queue += 1
			taille -= 1
		F[2] = taille
		F[1] = queue
		return True


def defiler(F):
	tete = F[1]
	taille = F[2]
	if taille != 0:
		x = F[tete-1]
		if tete == (nb_place+3):
			tete = 3
		else:
			tete -= 1
			taille += 1
			F[2] = taille
			F[1] = tete
		F[-1] = None
		return x


def main():
	global nb_place
	nb_place = 5 
	ma_file = [None]*(nb_place+1)
	ma_file[0] = 3
	ma_file[1] = 3
	ma_file[2] = 0
	emfiler(ma_file,8)
	print(ma_file)
	emfiler(ma_file,3)
	print(ma_file)
	emfiler(ma_file,5)
	print(ma_file)
	print(defiler(ma_file))
	print(ma_file)
	emfiler(ma_file,16)
	print(ma_file)

main()



"""
f = [None,None,None,None,None,None]
f = [3,None,None,None,None,None]
f = [3,3,None,None,None,None]
f = [3,3,0,None,None,None]
f = [3, 4, -1, 8, None, None]
f = [3, 5, -2, 8, 3, None]
f = [3, 6, -3, 8, 3, 5]
f = [3,5, -4, 8, 3, None]
f = [3, 6, -4, 8, 3, 16]
"""