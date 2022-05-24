def maxliste(lst):
	s_max = lst[0]
	for i in lst:
		if i > s_max:
			s_max = i
	return s_max

def main():
	print(maxliste([98, 12, 104, 23, 131, 9]))

main()