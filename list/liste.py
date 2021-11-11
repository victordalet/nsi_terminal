import random,csv
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
	liste += [element]
	return liste

#########################################################

def supprimerElement(liste,rang= -1):
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
	liste = ordreCroissant(liste)
	return liste[0]

#########################################################	

def recupererMax(liste):
	liste = ordreCroissant(liste)
	return liste[-1]

#########################################################

def fromCvsToList(url):
	contenu = csv.reader(open(url,"rb"))
	return contenu


#########################################################

def aleatoire():
	return nombre


#########################################################

def randomList(mini=0,maxi=100):
	liste = [random.randint(mini,maxi) for i in range(random.randint(mini,maxi))]
	return liste


#########################################################

def supprimerListe(liste):
	return []

#########################################################

def couperListe(liste):
	dic_liste = {}
	for i in range(longeurListe(liste)):
		dic_liste[str(i)] = liste[i]
	print(dic_liste)
	return dic_liste


print(supprimerElement([5,4,8,1]))
