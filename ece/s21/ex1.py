def multiplication(a,b):
	somme = 0
	if b >= 0:
		for i in range(b):
			somme += a
	else:
		for i in range(b,0):
			somme -= a
	return somme

def main():
	print(multiplication(-4,-8))
	print(multiplication(-4,8))

main()