def fibonacci(nb):
	if nb < 2:
		return nb
	return fibonacci(nb-1)+fibonacci(nb-2)

def main():
	print(fibonacci(25))

main()
