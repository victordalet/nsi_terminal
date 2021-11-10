def give_change(price,given_money):

	####################### INITIALISATION #######################

	if given_money < price :
		print("Erreur : il manque {}€".format(price-given_money))
		return False
	dic_of_box = {"1":15,"5":4,"10":12,"20":5,"50":4}
	dic_of_money = {"1":0,"5":0,"10":0,"20":0,"50":0}
	list_of_money = [50,20,10,5,1]
	difference = given_money - price
	complete = 0

	####################### CALCULE #######################

	for i in list_of_money:
		if i+complete < difference:
			while((complete < difference) and (dic_of_box[str(i)] > 0)):
				complete += i
				dic_of_money[str(i)] += 1
				dic_of_box[str(i)] -= 1

			if (dic_of_box["1"] ==  0) and (complete != difference):
				print("ERREUR PAS ASSER DE MONNAIE DANS LA CAISSE")
				return False

			if complete > difference:
				complete -= i
				dic_of_money[str(i)] -= 1
				dic_of_box[str(i)] += 1

	####################### AFFICHAGE #######################

	for i,j in dic_of_money.items():
		if j > 0:
			if i == "1":
				type_of_monney = "piece"
			else:
				type_of_monney = "billet"
			if j > 1 :
				s = "s"
			else : 
				s=""
			print("on vous rend {} {} de {}€".format(j,type_of_monney+s,i))

	print("caisse: {}".format(dic_of_box))

	return dic_of_money






def main():
	give_change(50,1340)
	print("------------------------------")
	give_change(150,30)
	print("------------------------------")
	give_change(80,97)
	print("------------------------------")
	give_change(40,132)

main()