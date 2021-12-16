import liste as l
def main():
	ma_liste = [2,3,2.0]
	liste2 = [5,7,2.0,[],'a']
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

##################################################################################################
	assert l.longeurListe(ma_liste) == 3 , "Erreur : mauvais résultat attendu"

	assert l.ordreCroissant(ma_liste) == [2.0, 2, 3] , "Erreur : mauvais résultat attendu"

	assert l.ordreDecroissant(ma_liste) == [2, 2.0, 3], "Erreur : mauvais résultat attendu"

	assert l.calculeMoyenne(ma_liste) == [2, 3, 2.0], "Erreur : mauvais résultat attendu"

	assert l.calculeEtendue(ma_liste) == 1.0, "Erreur : mauvais résultat attendu"

	assert l.calculeMediane(ma_liste)== 2, "Erreur : mauvais résultat attendu"

	assert l.ajouterElement(ma_liste,element) == [2, 3, 2.0, 9], "Erreur : mauvais résultat attendu"

	assert l.supprimerElement(ma_liste,rang) == [2, 3, 9], "Erreur : mauvais résultat attendu"

	assert l.recupererMin(ma_liste)==2.0, "Erreur : mauvais résultat attendu"

	assert l.recupererMax(ma_liste)==9, "Erreur : mauvais résultat attendu"

	assert l.supprimerListe(ma_liste)==[], "Erreur : mauvais résultat attendu"

	assert l.couperListe(ma_liste)=={'0': 2, '1': 3, '2': 2.0, '3': 9}, "Erreur : mauvais résultat attendu"

	assert l.bulle(ma_liste)==[2, 2.0, 3, 9], "Erreur : mauvais résultat attendu"

	assert l.somme(ma_liste)==16.0, "Erreur : mauvais résultat attendu"

	assert l.Tinsertion(ma_liste)==[2, 2.0, 3, 9], "Erreur : mauvais résultat attendu"

	assert l.fromCvsToList("data.csv")==['1', '2', '3', '4'], "Erreur : mauvais résultat attendu"

	assert l.Trapide(ma_liste)==[2, 2.0, 3, 9], "Erreur : mauvais résultat attendu"

	assert l.Tselection(ma_liste)==[2, 2.0, 3, 9], "Erreur : mauvais résultat attendu"

	assert l.enfiller(ma_liste,"avc")==[2, 2.0, 3, 9, 'avc'], "Erreur : mauvais résultat attendu"

	assert l.defiller(ma_liste)==[2.0, 3, 9], "Erreur : mauvais résultat attendu"

	assert l.empiler(ma_liste,"h6")==[2, 2.0, 3, 9, 'h6'], "Erreur : mauvais résultat attendu"

	assert l.depiler(ma_liste)==[2, 2.0, 3], "Erreur : mauvais résultat attendu"
######################################################################################################
	assert l.longeurListe(2) == 3 , 'Erreur : une list est attendu'

	assert l.ordreCroissant(2) == [2.0, 2, 3] , 'Erreur : une list est attendu'

	assert l.ordreDecroissant(2) == [2, 2.0, 3], 'Erreur : une list est attendu'

	assert l.calculeMoyenne(2) == [2, 3, 2.0], 'Erreur : une list est attendu'

	assert l.calculeEtendue(2) == 1.0, 'Erreur : une list est attendu'

	assert l.calculeMediane(2)== 2, 'Erreur : une list est attendu'

	assert l.ajouterElement(2,element) == [2, 3, 2.0, 9], 'Erreur : une list est attendu'

	assert l.supprimerElement(2,rang) == [2, 3, 9], 'Erreur : une list est attendu'

	assert l.recupererMin(2)==2.0, 'Erreur : une list est attendu'

	assert l.recupererMax(2)==9, 'Erreur : une list est attendu'

	assert l.supprimerListe(2)==[], 'Erreur : une list est attendu'

	assert l.couperListe(2)=={'0': 2, '1': 3, '2': 2.0, '3': 9}, 'Erreur : une list est attendu'

	assert l.bulle(2)==[2, 2.0, 3, 9], 'Erreur : une list est attendu'

	assert l.somme(2)==16.0, 'Erreur : une list est attendu'

	assert l.Tinsertion(2)==[2, 2.0, 3, 9], 'Erreur : une list est attendu'

	assert l.fromCvsToList("data.csv")==['1', '2', '3', '4'], 'Erreur : une list est attendu'

	assert l.Trapide(2)==[2, 2.0, 3, 9], 'Erreur : une list est attendu'

	assert l.Tselection(2)==[2, 2.0, 3, 9], 'Erreur : une list est attendu'

	assert l.enfiller(2,"avc")==[2, 2.0, 3, 9, 'avc'], 'Erreur : une list est attendu'

	assert l.defiller(2)==[2.0, 3, 9], 'Erreur : une list est attendu'

	assert l.empiler(2,"h6")==[2, 2.0, 3, 9, 'h6'], 'Erreur : une list est attendu'

	assert l.depiler(2)==[2, 2.0, 3], 'Erreur : une list est attendu'
###########################################################################################################	
	assert l.longeurListe(liste2) == 3 , "Erreur : une list deint ou float est demandée"

	assert l.ordreCroissant(liste2) == [2.0, 2, 3] , "Erreur : une list deint ou float est demandée"

	assert l.ordreDecroissant(liste2) == [2, 2.0, 3], "Erreur : une list deint ou float est demandée"

	assert l.calculeMoyenne(liste2) == [2, 3, 2.0], "Erreur : une list deint ou float est demandée"

	assert l.calculeEtendue(liste2) == 1.0, "Erreur : une list deint ou float est demandée"

	assert l.calculeMediane(liste2)== 2, "Erreur : une list deint ou float est demandée"

	assert l.ajouterElement(liste2,element) == [2, 3, 2.0, 9], "Erreur : une list deint ou float est demandée"

	assert l.supprimerElement(liste2,rang) == [2, 3, 9], "Erreur : une list deint ou float est demandée"

	assert l.recupererMin(liste2)==2.0, "Erreur : une list deint ou float est demandée"

	assert l.recupererMax(liste2)==9, "Erreur : une list deint ou float est demandée"

	assert l.supprimerListe(liste2)==[], "Erreur : une list deint ou float est demandée"

	assert l.couperListe(liste2)=={'0': 2, '1': 3, '2': 2.0, '3': 9}, "Erreur : une list deint ou float est demandée"

	assert l.bulle(liste2)==[2, 2.0, 3, 9], "Erreur : une list deint ou float est demandée"

	assert l.somme(liste2)==16.0, "Erreur : une list deint ou float est demandée"

	assert l.Tinsertion(liste2)==[2, 2.0, 3, 9], "Erreur : une list deint ou float est demandée"

	assert l.fromCvsToList("data.csv")==['1', '2', '3', '4'], "Erreur : une list deint ou float est demandée"

	assert l.Trapide(liste2)==[2, 2.0, 3, 9], "Erreur : une list deint ou float est demandée"

	assert l.Tselection(liste2)==[2, 2.0, 3, 9], "Erreur : une list deint ou float est demandée"

	assert l.enfiller(liste2,"avc")==[2, 2.0, 3, 9, 'avc'], "Erreur : une list deint ou float est demandée"

	assert l.defiller(liste2)==[2.0, 3, 9], "Erreur : une list deint ou float est demandée"

	assert l.empiler(liste2,"h6")==[2, 2.0, 3, 9, 'h6'], "Erreur : une list deint ou float est demandée"

	assert l.depiler(liste2)==[2, 2.0, 3], "Erreur : une list deint ou float est demandée"
######################################################################################################

	l.dessiner_graphe(graphe)


main()