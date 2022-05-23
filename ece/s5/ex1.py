def RechercheMinMax(tab):
	if tab == []:
		return{'min':None,'max':None}
	v_min = tab[0]
	v_max = tab[0]
	for i in tab:
		if v_min > i:
			v_min = i
		if v_max < i:
			v_max = i
	return {'min':v_min,'max':v_max}


def main():
	print(RechercheMinMax([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))
	print(RechercheMinMax([]))

main()


