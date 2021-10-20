def empiler(p,element):
	if (p[0] == nb_place+1):
		return False
	else:
		i = p[0]
		p[i] = element
		p[0] = i+1
		return True

def depiler(p):
	if p[0] != 1 :
		p[0] = p[0]-1
		i = p[0]
		p[i] = None
		return p[i] 

def main():
	global nb_place
	nb_place = 5 
	ma_pile = [None]*(nb_place+1)
	ma_pile[0] = 1
	empiler(ma_pile,8)
	empiler(ma_pile,3)
	empiler(ma_pile,5)
	print(depiler(ma_pile))
	print(ma_pile)

main()



"""
p = [None,None,None,None,None,None]
p = [2,8,None,None,None,None]
p = [3,8,3,None,None,None]
p = [4,8,3,5,None,None]
p = [3,8,3,None,None,None]
"""