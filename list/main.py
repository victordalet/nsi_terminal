import liste
def main():
	ma_liste = [2,3,2.0]
	graphe = [
	[1,5,3],
	[0,5,2],
	[1,4],
	[2,1,5,0],
	[0],
	[],
	[2,3],
	[0,1,2,3,4],
	[5]
	]
	element = 9
	rang = 2
	valeur = rang

	print(liste.longeurListe(ma_liste))
	"""
	entrée : une liste
	sortie : nombre d'éléments de la liste
	"""

	print(liste.ordreCroissant(ma_liste))
	#tri par fusion
	"""
	entrée : une liste d' int ou float
	sortie : la liste triée dans l'ordre croissant
	"""

	print(liste.ordreDecroissant(ma_liste))
	"""
	entrée : une liste d' int ou float
	sortie : la liste triée dans l'ordre décroissant
	"""

	print(liste.calculeMoyenne(ma_liste))
	"""
	entrée : une liste d' int ou float
	sortie : la moyenne de la liste
	"""

	print(liste.calculeEtendue(ma_liste))
	"""
	entrée : une liste d' int ou float
	sortie : l'étendue de la liste
	"""

	print(liste.calculeMediane(ma_liste))
	"""
	entrée : une liste d' int ou float
	sortie : la mediane de la liste
	"""

	print(liste.ajouterElement(ma_liste,element))
	"""
	entrée : une liste , un élément
	sortie : la liste avec un nouvelle élément
	"""

	print(liste.supprimerElement(ma_liste,rang))
	"""
	entrée : une liste , le rang d'une liste (prédéfinie au dernier élément)
	sortie : la liste avec l'élément en moins
	"""

	print(liste.recupererMin(ma_liste))
	"""
	entrée : une liste d' int ou float
	sortie : l'élément le plus petit de la liste
	"""

	print(liste.recupererMax(ma_liste))
	"""
	entrée : une liste d' int ou float
	sortie : l'élément le plus grand de la liste
	"""

	print(liste.randomList())
	"""
	entrée : rien 
	sortie : une liste avec des nombres aléatoires et de rangs aléatoires  
	"""

	print(liste.supprimerListe(ma_liste))
	"""
	entrée : une liste 
	sortie : la liste vidée
	"""

	print(liste.couperListe(ma_liste))
	"""
	entrée : une liste
	sortie : un dictionnaire avec en valeur le rang et en valeur la valeur du rang 
	"""

	print(liste.bulle(ma_liste))

	print(liste.somme(ma_liste))

	print(liste.dichotomie(ma_liste,valeur))

	print(liste.Tinsertion(ma_liste))

	print(liste.fromCvsToList("data.csv"))

	print(liste.Trapide(ma_liste))

	print(liste.Tselection(ma_liste))

	liste.dessiner_graphe(graphe)


main()