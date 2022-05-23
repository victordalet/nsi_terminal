def maxi(tab):
	nb_max = (tab[0],0)
	for i in range(len(tab)):
		if tab[i] > nb_max[0]:
			nb_max = (tab[i],i)
	return nb_max

def main():
	print(maxi([1,5,6,9,1,2,3,7,9,8]))

main()