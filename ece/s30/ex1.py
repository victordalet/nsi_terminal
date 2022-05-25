def fusion(tab1,tab2):
	lst = []
	for i in range(len(tab1)):
		if tab1[i] < tab2[i]:
			lst.append(tab1[i])
			lst.append(tab2[i])