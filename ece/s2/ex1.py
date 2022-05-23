def moyenne(lst):
	total = 0
	total_coef = 0
	for i in lst:
		total += i[0]*i[1]
		total_coef += i[1]
	return total/total_coef



def main():
	print(moyenne([(15,2),(9,1),(12,3)]))

main()