def fib(n):
	if n < 0 :
		return 'Erreur, pas de chiffres négatif'
	if n < 2:
		return n
	return (fib(n-1)+fib(n-2))


def main():
	print(fib(-2))
	print(fib(2))
	print(fib(5))
		
main()