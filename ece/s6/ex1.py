def maxi(tab):
	v_max = (tab[0],0)
	for i in range(len(tab)):
		if v_max[0] < tab[i]:
			v_max = (tab[i],i)
	return v_max

def main():
	print(maxi([1,5,6,9,1,2,3,7,9,8]))

main()
