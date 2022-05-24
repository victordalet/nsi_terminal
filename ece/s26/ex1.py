def RechercheMin(lst):
	s_min = lst[0],0
	for i in range(len(lst)):
		if lst[i] < s_min[0]:
			s_min = lst[i],i
	return s_min[1]

def main():
	print(RechercheMin([5, 3, 2, 2, 4]))

main()