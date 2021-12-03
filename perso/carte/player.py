from classcarte import *
from jeucarte2 import *


class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.nbCartes = 0
        self.mainJoueur = []

    def setMain(self, cartes):  # Définit la main du joueur, donc la liste de ses cartes au début du jeu
        self.mainJoueur = cartes
        self.nbCartes = len(cartes)

    def getNom(self):  # Accesseur de l’attribut nom
        return self.nom

    def getNbCarte(self):  # Accesseur du champ nbCartes
        return self.nbCartes

    def jouerCarte(self):  # Enlève et renvoie la dernière carte (objet de type Carte) de la main du joueur pour la jouer, ou retourne None s’il n’y a plus de cartes dans la main du joueur
        derniere = self.mainJoueur.pop()
        if self.getNbCarte() == 0:
            return None
        else:
            self.nbCartes -= 1
            print("la carte de {} est : {} de {}".format(self.nom, derniere.getNom(), derniere.getCouleur()))
        return derniere

    def insererMain(self, cartegagnee):  # Fonction qui insère les cartes de la liste des cartes gagnées dans la main du joueur
        new_liste = [cartegagnee] + self.mainJoueur
        self.mainJoueur = new_liste
        self.nbCartes += 1




