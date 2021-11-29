def insererElementArbre(arbre,indice_pere,fg,fd):
	"""
	Insere le fils gauche et droite d'une pere dans un arbre
	entrée : l'arbre (list) , indice du père (int) , element du fils gauche , element du fils droit
	sortie : l'arbre modifié (list)
	"""
	assert isinstance(arbre,list) , "l'arbre est de type list"
	assert isinstance(indice_pere,int) , "l'indice du père est un int"
	arbre[2*indice_pere+1] , arbre[2*indice_pere+2] = fg,fd 
	return arbre

def InitialiserArbre(profondeur):
	"""
	Initialise un arbre vide d'une certaine profondeur
	entrée : la profondeur (int)
	sortie : l'arbre (list)
	"""
	assert isinstance(profondeur,int) , "la profondeur est un int"
	return [None for i in range(2**(profondeur+1)-1)]

def calculeProfondeur(arbre):
	"""
	Calcule la profondeur de l'arbre
	entrée : l'arbre (list)
	sortie : la profondeur (int)
	"""
	assert isinstance(arbre,list) , "l'arbre est de type list"
	for i in range(arbre):
		if 2**(i+1) -1 == len(arbre):
			return i

def TrouveParent(arbre,indice_fils):
	"""
	etant donnée un arbre créer une fonction qui retrouve le parent(la valeur contenue dedans) d'un noeud
	entrée : l'arbre (list) , l'indice du fils (int)
	sortie : la valeur du noeud du père
	"""
	assert isinstance(arbre,list) , "l'arbre est de type list"
	assert isinstance(indice_fils,int) , "l'indice doit être un int"
	assert indice_fils > 0 , "l'indice du fils est trop petit" 
	if indice_fils%2 == 0:
		return arbre[(indice_fils-2)//2]
	return arbre[(indice_fils-1)//2]


def isNotEmpty(arbre):
	"""
	regarde si l'arbre est vide
	entrée : l'abre (list)
	sortie : True si vide , False si pas vide
	"""
	assert isinstance(arbre,list) , "l'arbre est de type list"
	if arbre == []:
		return True
	for i in arbre:
		if i != None : 
			return False
	return True


def TrouveFils(arbre,indice_pere):
	"""
	trouve les fils du parent
	entrée : l'abre (list) , l'indice du père (int)
	sortie : la valeur des deux fils (tuple)
	"""
	assert isinstance(arbre,list) , "l'arbre est de type list"
	assert isinstance(indice_pere,int) , "l'indice du père est un int"
	return arbre[2**(indice_noeud_pere +1)],arbre[2**(indice_noeud_pere +2)]


print(TrouveParent([1,2,5,6,2,3,4,5,2],7))