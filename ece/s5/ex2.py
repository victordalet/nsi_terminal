class Carte:
    """Initialise Couleur (entre 1 a 4), et Valeur (entre 1 a 13)"""
    def __init__(self, c, v):
        assert 1<=c<=4 , 'la couleur est comprise entre 1 et 4'
        assert 1<=v<=13 , 'la valeur est comprise entre 1 et 13' 
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10, 
       Valet, Dame, Roi"""
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    """Remplit le paquet de cartes"""
    def remplir(self):
       self.contenu = [ Carte(couleur,valeur) for couleur in range(1, 4) for valeur in range( 1, 13)]

    """Renvoie la Carte qui se trouve a  la position donnee"""
    def getCarteAt(self, pos):
        assert 0<= pos <= len(self.contenu) , 'la carte existe pas'
        if 0 <= pos < len(self.contenu) :
            return self.contenu[pos-1]


def main():
    unPaquet = PaquetDeCarte()
    unPaquet.remplir()
    uneCarte = unPaquet.getCarteAt(20)
    print(uneCarte.getNom() + " de " + uneCarte.getCouleur())

main()