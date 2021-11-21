import random
from classcarte import *
class Joeur:
	def __init__(self,nom,nbCarte):
		self.nom = nom
		self.nbCarte = nbCarte
		self.mainJoeur = []

	def setMain(self,commit):
		for i in range(self.nbCarte):
			self.mainJoeur += [commit]

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


