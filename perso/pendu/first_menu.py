from button import *
from random import choice
from pendu import *
from PIL import *

def launcher():
	fichier=open('liste2.txt',"r")
	contenu = fichier.readlines()
	mot_secret = choice(contenu)
	print('lancement...')
	Jeu(mot_secret[:-1])
	W.exit()

def launcher2():
	fichier=open('motsdifficiles.txt',"r")
	contenu = fichier.readlines()
	mot_secret = choice(contenu)
	print('lancement...')
	Jeu(mot_secret[:-1])
	W.exit()

def launcher3():
	if random.random() < 1/2:
		url = 'liste2.txt'
	else:
		url = 'motsdifficiles.txt'
	fichier=open(url,"r")
	contenu = fichier.readlines()
	mot_secret = choice(contenu)
	print('lancement...')
	Jeu(mot_secret[:-1])
	W.exit()



def menuOne(W):
	bttn(W,0,0,"FACILE","#ffcc66","#141414",launcher)
	bttn(W,0,37,"DIFICILE","#25dae9","#141414",launcher2)
	bttn(W,0,74,"ALEATOIRE","#f86263","#141414",launcher3)
