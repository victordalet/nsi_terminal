import random
from classcarte import *
class Joeur:
	def __init__(self,nom,nbCarte):
		self.nom = nom
		self.nbCarte = nbCarte
		self.mainJoeur = [Carte(random.choice(noms),random.choice(couleurs)) for i in range(self.nbCarte)]

	def setMain(self):
		for i in range(self.nbCarte):
			self.mainJoeur += [Carte(random.choice(noms),random.choice(couleurs))]

	def getNom(self):
		return self.nom
 
	def getNbCarte(self):
		return len(self.mainJoeur)

	def jouerCarte(self,mode="visible"):
		if self.mainJoeur == []:
			return None
		derniere = self.mainJoeur.pop()
		if mode == "visible":
			print("la carte de {} est : {} de {}".format(self.nom,derniere.getNom(),derniere.getCouleur()))
		return derniere

	def insererMain(self,carte):
		self.mainJoeur += [carte]


