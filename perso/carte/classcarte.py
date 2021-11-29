couleurs = ('CARREAU', 'COEUR', 'TREFLE', 'PIQUE') 
noms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi','As'] 
valeurs = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
'9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14} 
# Classe Carte 
class Carte: 
    def __init__(self, nom, couleur): 
 # Affectation des attributs nom et couleur avec contrôle. 
        self.nom = nom
        self.couleur = couleur 
        self.valeur = valeurs[self.nom] #on prend les valeurs la haut 
        assert nom not in noms, "Erreure"
        if couleur not in couleurs: 
            raise NameError
        else:
            self.couleurs=couleur
            
    def setNom(self, nom): # setter 
        self.nom=nom
        self.valeur = valeurs[self.nom]
    def getNom(self):
        return self.nom # getter 
    def getCouleur(self):
        return self.couleur  # getterDescription 
    def getValeur(self): # getter 
        return self.valeur
    def egalite(self, carte): 
        if self.valeur==carte.valeur:
            return True
        else:
            return False
# Renvoie True si les cartes ont même valeur, False sinon carte: Objet de type Carte 
    def estSuperieureA(self, carte): 
        if self.valeur>carte.valeur:
            return True
        else:
            return False
#donner chaque domaine des parametres
#Renvoie True si la valeur de self est supérieure à celle de carte, False sinon carte: Objet de type Carte ''' 
    def estInferieureeA(self, carte): 
        if self.valeur<carte.valeur:
            return True
        else:
            return False 
#Renvoie True si la valeur de self est inferieure à celle de carte, False sinon carte: Objet de type Carte '''

def testCarte(): 
    valetCoeur = Carte('Valet', 'CARREAU') 
    print('Nom:', valetCoeur.getNom()) 
    print('Couleur:', valetCoeur.getCouleur()) 
    print('Valeur:', valetCoeur.getValeur()) 
    valetCoeur.setNom('Dame')       
    print('Nom modifie:', valetCoeur.getNom()) 
    print('Valeur modifiee:', valetCoeur.getValeur()) 

if __name__ == "__main__":
    testCarte()
