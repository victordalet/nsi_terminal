def puissance(entier,exposant):
	if exposant < 1:
		return 1
	return entier* puissance(entier,exposant-1)


def mystere(n,x):
	mist  = 0
	if n > 0 : 
		print("avant-appel {} {}".format(n,x))
		mist = x + mystere(n-1,x)
	print("apes appel : {} {}".format(n,x))
	return mist


def main():
	print(puissance(5,3))
	print(mystere(5,3))

main()