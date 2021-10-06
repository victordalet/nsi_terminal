def ft_puissance(x,n):
	if n < 0 :
		return "Erreure :  pas de chiffre négatif"
	elif n ==0: 
		return 1
	if n > 0 : 
		return x*ft_puissance(x,n-1)


def main():
	print(ft_puissance(2,5))

main()

