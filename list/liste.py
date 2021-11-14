import random,csv
def longeurListe(liste):
	"""
	entrée : une liste
	sortie : nombre d'éléments de la liste
	"""
	c = 0
	for i in liste:
		c += 1
	return c

#########################################
def ordreCroissant(liste):
	"""
	entrée : une liste d' int ou float
	sortie : la liste triée dans l'ordre croissant
	"""
	if longeurListe(liste) == 1:
		return liste

	t1 = ordreCroissant(liste[0:longeurListe(liste)//2])
	t2 = ordreCroissant(liste[longeurListe(liste)//2:])

	return fusionCrossante(t1, t2)

def fusionCrossante(t1,t2):

	if t1 == []:
		return t2

	elif t2 == []:
		return t1

	elif t1[0] < t2[0]:
		return [t1[0]] + fusionCrossante(t1[1:],t2) 

	else:
		return [t2[0]] + fusionCrossante(t1,t2[1:])


#########################################################

def ordreDecroissant(liste):
	"""
	entrée : une liste d' int ou float
	sortie : la liste triée dans l'ordre décroissant
	"""
	if longeurListe(liste) == 1:
		return liste

	t1 = ordreCroissant(liste[:longeurListe(liste)//2])
	t2 = ordreCroissant(liste[longeurListe(liste)//2:])

	return fusionDecrossante(t1, t2)


def fusionDecrossante(t1,t2):

	if t1 == []:
		return t2

	elif t2 == []:
		return t1

	elif t1[0] > t2[0]:
		return [t2[0]] + fusionDecrossante(t1,t2[1:])

	else:
		return [t1[0]] + fusionDecrossante(t1[1:],t2)

#########################################################

def calculeMoyenne(liste):
	"""
	entrée : une liste d' int ou float
	sortie : la moyenne de la liste
	"""
	moyenne = 0
	for i in liste:
		moyenne += i
	moyenne /= longeurListe(liste)+1
	return liste

#########################################################

def calculeMediane(liste):
	"""
	entrée : une liste d' int ou float
	sortie : la mediane de la liste
	"""
	liste = ordreCroissant(liste)
	if longeurListe(liste) < 1:
		return None
	elif longeurListe(liste) % 2 == 0:
		return (liste[int((longeurListe(liste) - 1) / 2)] + liste[int((longeurListe(liste) + 1) / 2)]) / 2.0
	else:
		return liste[int((longeurListe(liste) - 1) / 2)]

#########################################################	

def calculeEtendue(liste):
	"""
	entrée : une liste d' int ou float
	sortie : l'étendue de la liste
	"""
	liste = ordreCroissant(liste)
	return liste[-1] - liste[0]

#########################################################

def ajouterElement(liste,element):
	"""
	entrée : une liste , un élément
	sortie : la liste avec un nouvelle élément
	"""
	liste += [element]
	return liste

#########################################################

def supprimerElement(liste,rang= -1):
	"""
	entrée : une liste , le rang d'une liste (prédéfinie au dernier élément)
	sortie : la liste avec l'élément en moins
	"""
	if rang == -1:
		rang = longeurListe(liste) -1
	dic = couperListe(liste)
	liste = supprimerListe(liste)
	for key,value in dic.items():
		if key != str(rang):
			liste = ajouterElement(liste,value)
	return liste

#########################################################

def recupererMin(liste):
	"""
	entrée : une liste d' int ou float
	sortie : l'élément le plus petit de la liste
	"""
	liste = ordreCroissant(liste)
	return liste[0]

#########################################################	

def recupererMax(liste):
	"""
	entrée : une liste d' int ou float
	sortie : l'élément le plus grand de la liste
	"""
	liste = ordreCroissant(liste)
	return liste[-1]

#########################################################

def fromCvsToList(url):
	"""
	entrée : l'url d'un fichier cvs 
	sortie : la liste du fichier cvs
	"""
	contenu = csv.reader(open(url,"rb"))
	return contenu


#########################################################

def aleatoire():
	return nombre


#########################################################

def randomList(mini=0,maxi=100):
	"""
	entrée : rien 
	sortie : une liste avec des nombres aléatoires et de rangs aléatoires  
	"""
	liste = [random.randint(mini,maxi) for i in range(random.randint(mini,maxi))]
	return liste


#########################################################

def supprimerListe(liste):
	"""
	entrée : une liste 
	sortie : la liste vidée
	"""
	return []

#########################################################

def couperListe(liste):
	"""
	entrée : une liste
	sortie : un dictionnaire avec en valeur le rang et en valeur la valeur du rang 
	"""
	dic_liste = {}
	for i in range(longeurListe(liste)):
		dic_liste[str(i)] = liste[i]
	print(dic_liste)
	return dic_liste


print(supprimerElement([5,4,8,1]))
