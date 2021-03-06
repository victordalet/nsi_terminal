from classcarte import *  # Il faut importer la classe Carte et les variables globales
import random  # Nécessaire pour mélanger le jeu


class JeuCartes:
    def __init__(self, nbCartes=52):
        assert nbCartes in [32, 52] , "32 ou 52 !!!!!!"
        # Le jeu doit comporter 32 ou 52 cartes, effectuer un contrôle
        self.jeu = []  # self.jeu est une liste des self.nbCartes
        self.nbCartes = nbCartes
        self.creerJeu()

        ################# Définition des méthodes d'instances #####################

    def getTailleJeu(self):
        """Fonction qui retourne le nombre de cartes du jeu
        Valeur retournée: type int"""  
        return self.nbCartes

    def creerJeu(self):  
        """Créée la liste des cartes de l'attribut self.jeu"""
        if self.nbCartes == 52:
            for n in noms:
                for c in couleurs:
                    self.jeu.append(Carte(n, c))
        elif self.nbCartes == 32:
            for n in noms[5:]:
                for c in couleurs:
                    self.jeu.append(Carte(n, c))

    def getJeu(self):
        """Renvoie la liste des cartes correspondant à l'attribut self.jeu"""
        return self.jeu

    def melanger(self):  # utiliser le module random ...
        """Mélange sur place les cartes de la liste des cartes associée
        au champ self.jeu"""
        random.shuffle(self.jeu)

    def distribuerCarte(self):
        """Cette fonction permet de distribuer une carte à un joueur.
        Elle retourne la carte Valeur retournée: Objet de type Carte"""
        return self.jeu.pop()

    def distribuerJeu(self, nbJoueurs, nbCarteADonner):
        """Cette méthode distribue nbCartes à chacun des nbJoueurs, ..."""
        n = nbJoueurs
        nc = nbCarteADonner
        main = [[] for i in range(n)]
        for e in main:
            for i in range(nc):
                e.append(self.distribuerCarte())
        return main


# Fonction test et vérification de la classe JeuCartes
def testJeuCartes():
    jeu52 = JeuCartes(52)
    jeu52.melanger()
    L = jeu52.getJeu()
    carte = L[2]  # le 3e carte
    print("Nom:", carte.getNom())
    print("Couleur:", carte.getCouleur())
    print("Valeur:", carte.getValeur())
    # Distribution de 4 cartes à 3 joueurs
    distribution_3j_4c = jeu52.distribuerJeu(3, 4)
    for i in range(3):
        print("Joueur", i + 1, ":")
        listeCartes = distribution_3j_4c[i]
        for c in listeCartes:
            print(c.getNom(), "de", c.getCouleur())
    #distribution_6_joueurs_10_cartes_par_joueur = jeu52.distribuerJeu(6, 10) 
    #for i in range(3):
        #print("Joueur", i + 1, ":")
        #listeCartes = distribution_6_joueurs_10_cartes_par_joueur[i]
        #for c in listeCartes:
            #print(c.getNom(), "de", c.getCouleur())
    

