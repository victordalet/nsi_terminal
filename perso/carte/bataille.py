from jeucarte2 import *
from classcarte import *
from player import *

LIMITE_MANCHES = 50000 #définit un nombre de tours limités pour éviter les parties infinies

class Bataille:
    def __init__(self):
        self.paquet = JeuCartes (int(input("32 ou 52 cartes?:")))
        self.paquet.creerJeu()
        self.paquet.melanger()
        self.player1 = Joueur(input("Nom du joueur 1:"))
        self.player2 = Joueur(input("Nom du joueur 2:"))
        npaquet = self.paquet.distribuerJeu(2, int(self.paquet.getTailleJeu()/2)) #variable qui contient un paquet divisé en 2
        self.player1.setMain(npaquet[0])
        self.player2.setMain(npaquet[1])
        self.liste1 = [] #correspond à la pile du joueur 1
        self.liste2 = [] #correspond à la pile du joueur 2
        self.manche = 1

    def jouer(self): #méthode qui permet de lancer une partie de cartes
        while (self.player1.getNbCarte() and self.player2.getNbCarte() and self.manche <= LIMITE_MANCHES): #pose la condition : tant que chaque joueur a des cartes et que la limite n'est pas atteinte
            try: #bloc try qui sert à tester le code potentiellement problématique ()

                #les deux joueurs jouent une carte dans leur pile respective
                self.liste1.append(self.player1.jouerCarte()) 
                self.liste2.append(self.player2.jouerCarte())

                #tant que les cartes des joueurs sont égales, une bataille a lieu 
                while self.liste1[-1].egalite(self.liste2[-1]): 
                    self.liste1.append(self.player1.jouerCarte())
                    self.liste1.append(self.player1.jouerCarte())  # correspond à la carte retournée face cachée
                    self.liste2.append(self.player2.jouerCarte())
                    self.liste2.append(self.player2.jouerCarte())  # correspond à la carte retournée face cachée 

                #si la carte du joueur 2 est supérieure à celle du joueur 1, le joueur 2 gagne et inversement
                if self.liste2[-1].estSuperieureA(self.liste1[-1]): 
                    print("{} a gagné contre {} à la manche {}".format(self.player2.getNom(),self.player1.getNom(),self.manche,))
                    gagnant = self.player2
                else:
                    print("{} a gagné contre {} à la manche {}".format(self.player1.getNom(),self.player2.getNom(),self.manche,))
                    gagnant = self.player1

                #tant que la pile du joueur 1 ou du joueur 2 n'est pas vide, le gagnant récupère leur dernière carte
                while self.liste1 != []: 
                    gagnant.insererMain(self.liste1.pop()) 
                while self.liste2 != []:
                    gagnant.insererMain(self.liste2.pop())
                gagnant.mainJoueur.reverse() #inverse la main du joueur 
                self.manche += 1

                #Cas où le nombre limite de manches est dépassé
                if self.manche > LIMITE_MANCHES: #si la limite de manches est dépassée:
                    print("---------------------------------------")
                    if self.player2.getNbCarte() < self.player1.getNbCarte(): #si le joueur1 a plus de cartes que le joueur2, il gagne la partie
                        print(
                            "{} détient {} cartes alors que {} n'en a que {}".format(
                                self.player1.getNom(),
                                self.player1.getNbCarte(),
                                self.player2.getNom(),
                                self.player2.getNbCarte(),
                            )
                        )
                    elif self.player2.getNbCarte() > self.player1.getNbCarte(): #si le joueur2 a plus de cartes que le joueur1, il gagne la partie
                        print(
                            "{} détient {} cartes alors que {} n'en a que {}".format(
                                self.player2.getNom(),
                                self.player2.getNbCarte(),
                                self.player1.getNom(),
                                self.player1.getNbCarte(),
                            )
                        )
                    else:
                        print("Égalité, les deux joueurs ont {} cartes".format(self.player1.getNbCarte()))
                print("---------------------------------------")

            #si l'exception IndexError est rencontrée, l'exception est levée
            except : continue

        #si la main du joueur 2 est vide, le joueur 1 a gagné et inversement
        if self.player2.mainJoueur == []: 
            print("{} a gagné la partie contre {}".format(self.player1.getNom(), self.player2.getNom()))
        elif self.player1.mainJoueur == []:
            print("{} a gagné la partie contre {}".format(self.player2.getNom(), self.player1.getNom()))

#Test
def test():
    b = Bataille()
    b.jouer()

test()

