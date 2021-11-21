from jeucarte2 import *
from classcarte import * 
from player import *


class Bataille:
	def __init__(self):
		self.liste = []

	def lastElement(self):
		return self.liste[-1]

	def SetElement(self,carte):
		self.liste += [carte]

	def BinElement(self):
		return self.liste.pop()

	def nbCartes(self):
		return len(self.liste)


def run():
	commit = JeuCartes()
	commit.creerJeu()
	commit.melanger()
	player1 = Joeur("bob",int(commit.getTailleJeu()/2))
	player2 = Joeur("billy",int(commit.getTailleJeu()/2))
	for i in range(1,int(commit.getTailleJeu()/2)):
		print(player1.getNbCarte())
		player1.insererMain(commit.distribuerCarte())
	for i in range(1,int(commit.getTailleJeu()/2)):	
		player2.insererMain(commit.distribuerCarte())
	liste1 = Bataille()
	liste2 = Bataille()
	manche = 1
	while player1.mainJoeur != [] and player2.mainJoeur != []:
		try : 
			liste1.SetElement(player1.jouerCarte())
			liste2.SetElement(player2.jouerCarte())
			while (liste1.lastElement().egalite(liste2.lastElement())):
				liste1.SetElement(player1.jouerCarte("invisible"))
				liste1.SetElement(player1.jouerCarte())
				liste2.SetElement(player2.jouerCarte("invisible"))
				liste2.SetElement(player2.jouerCarte())
			if liste2.lastElement().estSuperieureA(liste1.lastElement()):
				print("{} a gagné contre {} à la manche {}".format(player2.getNom(),player1.getNom(),manche))
				gagnant = player1
			else : 
				print("{} a gagné contre {} à la manche {}".format(player1.getNom(),player2.getNom(),manche))
				gagnant = player2
			while(liste1.liste != []):
				gagnant.insererMain(liste1.BinElement())
			while(liste2.liste != []):
				gagnant.insererMain(liste2.BinElement())
			manche += 1 
			print("---------------------------------------")
		except : continue
	if player2.mainJoeur == [] :
		print("{} a gagnée la partie contre {}".format(player1.getNom(),player2.getNom()))
	else : print("{} a gagnée la partie contre {}".format(player2.getNom(),player1.getNom()))



"""
JeuCartes
	getTailleJeu
	creerJeu
	getJeu
	melanger
	distribuerCarte
	distribuerJeu
Carte
	setNom
	getNom
	getCouleur
	getValeur
	egalite
	estSuperieureA
	estInferieurA
Player
	distribuerJeu
	insererMain
	jouerCarte
	getNbCarte
"""
	