def xor(tab1,tab2):
	tab = []
	for i in range(len(tab1)):
		if tab1[i] == tab2[i]:
			tab.append(0)
		else : 
			tab.append(1)
	return tab

def main():
	a = [1, 0, 1, 0, 1, 1, 0, 1]
	b = [0, 1, 1, 1, 0, 1, 0, 0]
	c = [1, 1, 0, 1]
	d = [0, 0, 1, 1]
	assert(xor(a, b) == [1, 1, 0, 1, 1, 0, 0, 1])
	assert(xor(c, d) == [1, 1, 1, 0])

main()
