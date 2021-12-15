def pgcol(a,b):
	"""
	renvoie le plus grand diviseur commun
	entrée : deux int
	sortie : int (le plus grand divisuer)
	"""
	assert isinstance(a,int) or isinstance(a,float) , 'on demande un int ou un float'
	assert isinstance(b,int) or isinstance(b,float) , 'on demande un int ou un float'
	if b == 0:
		return a
	return pgcol(b,a%b)


def boucle(i,k):
	"""
	affiche les entiers entre deux nobmres
	entrée : deux int ou float
	sortie : les affichages
	"""
	assert isinstance(i,int) or isinstance(i,float) , 'on demande un int ou un float'
	assert isinstance(k,int) or isinstance(k,float) , 'on demande un int ou un float'
	if i ==k:
		return i  
	print(i) 
	return boucle(i+1,k)



def boucle2(i):
	"""
	affiche les entiers entre deux nobmres
	entrée : un tuple de deux int ou float
	sortie : les affichages
	"""
	for nombre in range(i[0],i[1]+1):
		print(nombre)



def main():
	print(pgcol(2,4))
	print('----------------------------------')
	print(boucle(2,9))
	print('----------------------------------')
	boucle2((2,9))

main()