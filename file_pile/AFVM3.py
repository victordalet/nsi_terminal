def inserer(l,element,i):
	if (l[0] == nb_place +1) or (i-1 > l[0]):
		return False
	else:
		for k in range(l[0]+1,i+1,-1):
			l[k] = l[k+1]
		l[i] = element
		l[0] += 1
		return True


def supprimer(l,i):
	if (l[0]!= 0) and (i <= l[0]):
		for k in range(i,l[0]+1):
			l[k] = l[k+1]
		l[0] = l[0]-1
		return True
	else:
		return False

def main():
	global nb_place
	nb_place = 5 
	ma_liste = [None]*(nb_place+1)
	ma_liste[0] = 0
	inserer(ma_liste,3,1)
	inserer(ma_liste,5,2)
	inserer(ma_liste,8,1)
	supprimer(ma_liste,2)
	print(ma_liste)

main()



"""
l = [None,None,None,None,None,None]
l = [1,3,None,None,None,None]
l = [2,3,5,None,None,None]
l = [2,8,5,None,None,None]
l = [1,8,None,None,None,None]
"""
