import random,csv,turtle

#doc : http://virginieduhamel.lescigales.org/doc/


def longeurListe(liste):
	"""
	entrée : une liste
	sortie : nombre d'éléments de la liste
	"""
	assert isinstance(liste,list), "une liste est demandée"
	c = 0
	for i in liste:
		c += 1
	return c

#########################################
def ordreCroissant(liste):
	"""
	entrée : une liste d' int ou float
	sortie : la liste triée dans l'ordre croissant par la méthode de fusion
	"""
	assert isinstance(liste,list), "une liste est demandée"
	assert longeurListe(liste) > 0, "Tableau est vide"
	chercheList(liste)
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
	assert isinstance(liste,list), "une liste est demandée"
	assert longeurListe(liste) > 0, "Tableau est vide"
	chercheList(liste)
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
	assert isinstance(liste,list), "une liste est demandée"
	assert longeurListe(liste) > 0, "Tableau est vide"
	chercheList(liste)
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
	assert isinstance(liste,list), "une liste est demandée"
	assert longeurListe(liste) > 0, "Tableau est vide"
	chercheList(liste)
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
	assert isinstance(liste,list), "une liste est demandée"
	assert longeurListe(liste) > 0, "Tableau est vide"
	chercheList(liste)
	liste = ordreCroissant(liste)
	return liste[-1] - liste[0]

#########################################################

def ajouterElement(liste,element):
	"""
	entrée : une liste , un élément
	sortie : la liste avec un nouvelle élément
	"""
	assert isinstance(liste,list), "une liste est demandée"
	liste += [element]
	return liste

#########################################################

def supprimerElement(liste,rang= -1):
	"""
	entrée : une liste , le rang d'une liste (prédéfinie au dernier élément)
	sortie : la liste avec l'élément en moins
	"""
	assert isinstance(liste,list), "une liste est demandée"
	assert longeurListe(liste) > 0, "Tableau est vide"
	chercheList(liste)
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
	assert isinstance(liste,list), "une liste est demandée"
	assert longeurListe(liste) > 0, "Tableau est vide"
	chercheList(liste)
	liste = ordreCroissant(liste)
	return liste[0]

#########################################################	

def recupererMax(liste):
	"""
	entrée : une liste d' int ou float
	sortie : l'élément le plus grand de la liste
	"""
	assert isinstance(liste,list), "une liste est demandée"
	assert longeurListe(liste) > 0, "Tableau est vide"
	chercheList(liste)
	liste = ordreCroissant(liste)
	return liste[-1]

#########################################################

def fromCvsToList(url,type_separateur = ";"):
	"""
	entrée : l'url d'un fichier cvs 
	sortie : la liste du fichier cvs
	"""
	assert isinstance(type_separateur,str), "le séparateur est un str"
	liste = []
	liste2 = []
	try : 
		with open(url, newline='') as csvfile:
			contenu = csv.reader(csvfile, delimiter=' ', quotechar='|')
			for i in contenu:
				ajouterElement(liste, i)
			for i in liste[0]:
				for j in i:
					if j != type_separateur:
						liste2.append(j)
	except : print("Erreur : mauvais séparateur ou mauvais chemain d'accès")
	return liste2
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
	assert isinstance(liste,list), "une liste est demandée"
	return []

#########################################################

def couperListe(liste):
	"""
	entrée : une liste
	sortie : un dictionnaire avec en valeur le rang et en valeur la valeur du rang 
	"""
	assert isinstance(liste,list), "une liste est demandée"
	assert longeurListe(liste) > 0, "Tableau est vide"
	chercheList(liste)
	dic_liste = {}	
	for i in range(longeurListe(liste)):
		dic_liste[str(i)] = liste[i]
	print(dic_liste)
	return dic_liste

##########################################################

def bulle(liste):
	"""
	entrée : une liste
	sortie : la liste triée dans l'ordre croissant
	"""
	assert isinstance(liste,list), "une liste est demandée"
	assert longeurListe(liste) > 0, "Tableau est vide"
	chercheList(liste)
	for i in range(longeurListe(liste)):
		for j in range(longeurListe(liste) - i - 1):
			if liste[j] > liste[j + 1]:
				liste[j], liste[j + 1] = liste[j + 1], liste[j]
	return liste

##########################################################


def somme(liste):
	"""
	entrée : une liste
	sortie : la somme des thermes
	"""
	assert isinstance(liste,list), "une liste est demandée"
	assert longeurListe(liste) > 0, "Tableau est vide"
	chercheList(liste)
	somme = 0
	for i in  liste:
		somme += i
	return somme


###########################################################

def dichotomie(liste,valeur):
	"""
	entrée : une liste, une valeur a rechercher dans la liste
	sortie : True si la valeur est dans la liste, sinon False
	"""
	assert isinstance(liste,list), "une liste est demandée"
	assert isinstance(valeur,int), "une int est demandée"
	assert longeurListe(liste) > 0, "Tableau est vide"
	chercheList(liste)
	a = 0
	b = longeurListe(liste) - 1
	while a <= b:
		moyenne = (a + b) // 2
		if liste[moyenne] == valeur:
			return True
		elif liste[moyenne] < valeur:
			a = moyenne + 1
		else:
			b = moyenne - 1
	return False

###########################################################

def dessiner_graphe(graphe):
	"""
	entrée : un graphe
	sortie : l'affichage du graphe
	"""
	assert isinstance(graphe,list), "une graphe est demandée"
	assert longeurListe(graphe) > 0, "graphe est vide"
	turtle.title("graphe")
	####################### Noeud #######################	
	coordonnees = []
	x,y = (0,0)
	distance = 70
	for i in range(longeurListe(graphe)):
		coordonnees.append([x,y])
		noeud = draw()		
		noeud.polygone(x,y,(0,0,0))
		if i < int(longeurListe(graphe)/2):
			y -= distance 
			if i == 0:
				x += distance 
		else :
			if i != int(longeurListe(graphe)/2):
				y += distance 
			x = -distance


	####################### Ligne #######################
	for i in range(longeurListe(graphe)):
		for j in range(longeurListe(graphe[i])):
			ligne = draw()
			ligne.line(coordonnees[i][0],coordonnees[i][1],(220,0,0),coordonnees[graphe[i][j]][0],coordonnees[graphe[i][j]][1])

	turtle.mainloop()

class draw:
	def __init__(self):
		self.t = turtle.Turtle()
		self.t.speed(0)
		self.length = 10

	def initialization(self,positionX,positionY,color):
		self.t.up()
		self.t.goto(positionX, positionY)
		self.t.down()
		self.t.screen.colormode(255)
		turtle.Screen().bgcolor((8,192,254))
		self.t.fillcolor(color)
		self.t.begin_fill()
		turtle.hideturtle()

	def polygone(self, positionX, positionY, color):
		self.initialization(positionX, positionY, color)
		for i in range(10):
			self.t.forward(self.length)
			self.t.left(360 / 10)

	def line(self, positionX, positionY, color,positionX2,positionY2):
			self.initialization(positionX, positionY, color)
			self.t.goto(positionX2,positionY2)


###########################################################
def Tinsertion(liste):
	"""
	entrée : une liste
	sortie : la liste triée dans l'ordre croissant avec la méthode par inserction
	"""
	assert isinstance(liste,list), "une liste est demandée"
	assert longeurListe(liste) > 0, "Tableau est vide"
	chercheList(liste)
	for i in range(1,longeurListe(liste)):
		c = liste[i]
		valeur = i - 1
		while valeur >= 0 and liste[valeur] > c:
			liste[valeur + 1] = liste[valeur]
			valeur -= 1
		liste[valeur + 1] = c

	return liste

############################################################

def Trapide(liste):
	"""
	entrée : une liste
	sortie : la liste triée dans l'ordre croissant avec la méthode de trie rapide
	"""
	assert isinstance(liste,list), "une liste est demandée"
	assert longeurListe(liste) > 0, "Tableau est vide"
	chercheList(liste)
	pivot = liste[longeurListe(liste) - 1]
	c = 0
	valeur = 0
	while valeur < longeurListe(liste) - 1:
		if liste[valeur] <= pivot:
			liste[c], liste[valeur] = liste[valeur], liste[c]
			c += 1
		valeur += 1
	liste[longeurListe(liste) - 1], liste[c] = liste[c], liste[longeurListe(liste) - 1]

	return liste

############################################################

def Tselection(liste):
	"""
	entrée : une liste
	sortie : la liste triée dans l'ordre croissant avec la méthode de trie par selection
	"""
	assert isinstance(liste,list), "une liste est demandée"
	assert longeurListe(liste) > 0, "Tableau est vide"
	chercheList(liste)
	n = longeurListe(liste)
	for i in range(n - 2):
		value_min = i
		for j in (i + 1, n - 1):
			if liste[j] < liste[value_min]:
				value_min = j
			if value_min != i:
				liste[i], liste[value_min] = liste[value_min], liste[i]
	return liste
#################################################################

def chercheList(liste):
	for i in liste:
		assert isinstance(i,float) or isinstance(i,int), "une liste de floatant ou d'int est demandée"

################################################
def enfiller(liste,element):
	"""
	enfiller un element dans une fille
	entrée : liste (list) , element
	sortie : la liste avec l'élément enfiller (list)
	"""
	assert isinstance(liste,list), "une liste est demandée"
	assert longeurListe(liste) > 0, "Tableau est vide"
	chercheList(liste)
	new_liste = []
	for i in liste:
		new_liste += [i]
	new_liste += [element]
	return new_liste

def defiller(liste):
	"""
	defiller un element dans une fille
	entrée : liste (list)
	sortie : la liste defiller (list)
	"""
	assert isinstance(liste,list), "une liste est demandée"
	assert longeurListe(liste) > 0, "Tableau est vide"
	chercheList(liste)
	new_liste = []
	for i in range(len(liste)):
		if i != 0:
			new_liste += [liste[i]]
	return new_liste

def empiler(liste,element):
	"""
	empile un element dans une pile
	entrée : liste (list) , element
	sortie : la liste avec l'élément enpiler (list)
	"""
	return enfiller(liste,element)
	

def depiler(liste):
	"""
	defiller un element dans une fille
	entrée : liste (list)
	sortie : la liste defiller (list)
	"""
	assert isinstance(liste,list), "une liste est demandée"
	assert longeurListe(liste) > 0, "Tableau est vide"
	chercheList(liste)
	new_liste = []
	for i in range(len(liste)):
		if i != len(liste)-1:
			new_liste += [liste[i]]
	return new_liste

