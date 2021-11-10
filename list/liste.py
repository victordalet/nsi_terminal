def longeurListe(liste):
	c = 0
	for i in liste:
		c += 1
	return c

#########################################
def ordreCroissant(liste):
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
	moyenne = 0
	for i in liste:
		moyenne += i
	moyenne /= longeurListe(liste)+1
	return liste

#########################################################

def calculeMediane(liste):
	liste = ordreCroissant(liste)
	if longeurListe(liste) < 1:
		return None
	elif longeurListe(liste) % 2 == 0:
		return (liste[int((longeurListe(liste) - 1) / 2)] + liste[int((longeurListe(liste) + 1) / 2)]) / 2.0
	else:
		return liste[int((longeurListe(liste) - 1) / 2)]

#########################################################	

def calculeEtendue(liste):
	liste = ordreCroissant(liste)
	return liste[-1] - liste[0]

#########################################################

def ajouterElement(liste,element):
	liste += element
	return liste

#########################################################

def supprimerElement(liste,rang= -1):
	del liste[rang]
	return liste

#########################################################

def recupererMin(liste):
	liste = ordreCroissant(liste)
	return liste[0]

#########################################################	

def recupererMax(liste):
	liste = ordreCroissant(liste)
	return liste[-1]

#########################################################

def fromCvsToList(liste,url):
	return liste


#########################################################

def aleatoire(min,max):
	return n


#########################################################

def randomList():
	liste = [aleatoire(0,50) for i in range(aleatoire(0,50))]
	return liste


#########################################################

def supprimerListe(liste):
	return []

#########################################################

def couperListe(liste):
	dic_liste = {}
	for i in range(longeurListe(liste)):
		dic_liste[str(i)] = liste[i]
	return dic_liste


def test():
	print(supprimerElement([5,9,7,2],1))


	def doc() : 	
		liste.longeurListe(ma_liste)
		"""
		entrée : une liste
		sortie : nombre d'éléments de la liste
		"""

		liste.ordreCroissant(ma_liste)
		"""
		entrée : une liste d' int ou float
		sortie : la liste triée dans l'ordre croissant
		"""

		liste.ordreDecroissant(ma_liste)
		"""
		entrée : une liste d' int ou float
		sortie : la liste triée dans l'ordre décroissant
		"""

		liste.calculeMoyenne(ma_liste)
		"""
		entrée : une liste d' int ou float
		sortie : la moyenne de la liste
		"""

		liste.calculeEtendue(ma_liste)
		"""
		entrée : une liste d' int ou float
		sortie : l'étendue de la liste
		"""

		liste.calculeMediane(ma_liste)
		"""
		entrée : une liste d' int ou float
		sortie : la mediane de la liste
		"""

		liste.ajouterElement(ma_liste,element)
		"""
		entrée : une liste , un élément
		sortie : la liste avec un nouvelle élément
		"""

		liste.supprimerElement(ma_liste,rang)
		"""
		entrée : une liste , le rang d'une liste (prédéfinie au dernier élément)
		sortie : la liste avec l'élément en moins
		"""

		liste.recupererMin(ma_liste)
		"""
		entrée : une liste d' int ou float
		sortie : l'élément le plus petit de la liste
		"""

		liste.recupererMax(ma_liste)
		"""
		entrée : une liste d' int ou float
		sortie : l'élément le plus grand de la liste
		"""

		liste.fromCvsToList(url)
		"""
		entrée : l'url d'un fichier cvs 
		sortie : la liste du fichier cvs
		"""

		liste.randomList()
		"""
		entrée : rien 
		sortie : une liste avec des nombres aléatoires et de rangs aléatoires  
		"""


		liste.supprimerListe(ma_liste)
		"""
		entrée : une liste 
		sortie : la liste vidée
		"""

		liste.couperListe(ma_liste)
		"""
		entrée : une liste
		sortie : un dictionnaire avec en valeur le rang et en valeur la valeur du rang 
		"""

	


test()