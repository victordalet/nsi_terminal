def calcul(n):
	lst = [n]
	while lst[-1] != 1:
		if lst[-1]%2 == 0:
			lst.append(int(lst[-1]/2))
		else:
			lst.append(lst[-1]*3+1)
	return lst

def main():
	print(calcul(7))

main()
