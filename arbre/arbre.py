def insererElementArbre(arbre,indice_pere,fg,fd):
	"""
	Insere le fils gauche et droite d'une pere dans un arbre
	entrée : l'arbre (list) , indice du père (int) , element du fils gauche , element du fils droit
	sortie : l'arbre modifié (list)
	"""
	assert isinstance(arbre,list) , "l'arbre doit est de type list"
	assert isinstance(indice_pere,int) , "l'indice du père est un int"
	try : 
		arbre[2*indice_pere+1] , arbre[2*indice_pere+2] = fg,fd 
		return arbre
	except :
		for i in range(len(arbre),2**(indice_pere)+3):
			arbre.append(None)
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
	assert isinstance(arbre,list) , "l'arbre doit est de type list"
	for i in range(len(arbre)):
		if 2**(i+1) -1 == len(arbre):
			return i

def TrouveParent(arbre,indice_fils):
	"""
	etant donnée un arbre créer une fonction qui retrouve le parent(la valeur contenue dedans) d'un noeud
	entrée : l'arbre (list) , l'indice du fils (int)
	sortie : la valeur du noeud du père
	"""
	assert isinstance(arbre,list) , "l'arbre doit est de type list"
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
	assert isinstance(arbre,list) , "l'arbre doit est de type list"
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
	assert isinstance(arbre,list) , "l'arbre doit est de type list"
	assert isinstance(indice_pere,int) , "l'indice du père est un int"
	try : 
		return arbre[2**(indice_pere )],arbre[2**(indice_pere )+1]
	except : raise TypeError("le père n'as pas de fils")


def valueIsRacine(arbre,value):
	"""
	True si la valeur est la racine
	entrée : l'arbre (list) ,  la valeur 
	sortie : True si noeud sinon False
	"""
	assert isinstance(arbre,list) , "l'arbre doit est de type list"
	if value == arbre[0]:
		return True
	return False

def isSheet(arbre,indice):
	"""
	Regarde si l'indice est une feuille
	entrée : l'arbre (list) , l'indice (int)
	sortie : True si est une feuille sinon False
	"""
	assert isinstance(arbre,list) , "l'arbre doit est de type list"
	assert isinstance(indice,int) , "l'indice est un int"
	try : 
		if arbre[indice] == None:
			return True
		return False
	except : raise TypeError("l'indice est trop grand")


def InitialiserArbreRecursife(profondeur):
	"""
	Initialiser un arbre recursif
	entrée : la profondeur (int)
	sortie : un arbre recursif (list)
	"""
	assert isinstance(profondeur,int) , "la profondeur est un int"
	if profondeur == 0:
		return 
	return [None,[InitialiserArbreRecursife(profondeur-1),InitialiserArbreRecursife(profondeur-1)]]

def ConvertirArbreInRecursive(arbre,c=0):
	"""
	Convertis l'arbre en arbre recursif
	entrée : un arbre non recursif (list)
	sortie : un arbre recursif (list)
	"""
	assert isinstance(arbre,list) , "l'arbre doit est de type list"
	if len(arbre) <= 2*c+1:
		return arbre[c]
	return [arbre[c],[ConvertirArbreInRecursive(arbre,2*c+1),ConvertirArbreInRecursive(arbre,2*c+2)]]


def ProfondeurRecursif(arbre,profondeur=0):
	"""
	calcule la profondeur en appelle recursif
	entrée : arbre (list)
	sortie : la profondeur (int)
	"""
	assert isinstance(arbre,list) , "l'arbre doit est de type list"
	if 2*profondeur+1 >= len(arbre) :
		return 0 
	return 1+ProfondeurRecursif(arbre,2*(profondeur)+1)

def ProfondeurListImbriquer(arbre):
	"""
	calcule la profondeur en appelle recursif de liste imbriquer
	entrée : arbre (list)
	sortie : la profondeur (int)
	"""
	assert isinstance(arbre,list) , "l'arbre doit est de type list"
	if arbre[1] == []:
		return 0
	profondeur = []
	for i in arbre[1:]:																									
		profondeur.append(ProfondeurListImbriquer(i))
	return max(profondeur)+1

def ConvertirArbreInIterratif(arbre):
	"""
	convertir un arbre recursif en iterratif
	entrée : un arbre recursif
	sortie : l'arbre iterratif
	"""
	assert isinstance(arbre,list) , "l'arbre doit est de type list"
	new_arbre = []
	new_arbre.append()
	return new_arbre


def ParcoursLargeur(arbre):
	"""
	Parcour la liste en largeur
	entrée : arbre recursif
	sortie : void
	"""
	assert isinstance(arbre,list) , "l'arbre doit est de type list"
	new_arbre = ConvertirArbreInIterratif(arbre)
	for i in new_arbre:
		print(i)

def ParcoursLongeur(arbre):
	"""
	Parcour la liste en longeur
	entrée : arbre recursif
	sortie : void
	"""
	assert isinstance(arbre,list) , "l'arbre doit est de type list"
	arbre = str(arbre)
	for i in arbre:
		if i != '[' and i != ']' and i != ',' and i!=  ' ':
			print(i)






