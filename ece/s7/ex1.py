def conv_bin(n):
	b = []
	while n != 0:
		if n%2 == 0:
			b.insert(0,0) 
		else :
			b.insert(0,1)
		n //= 2
	bit = len(b)
	return (b,bit)

def main():
	print(conv_bin(20))

main()

		