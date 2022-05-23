def delta(lst):
	resultats = [lst[0]]
	for i in range(1,len(lst)):
		resultats.append(lst[i]-lst[i-1])
	return resultats



def main():
	print(delta([1000, 800, 802, 1000, 1003]))
	print(delta([42]))

main()