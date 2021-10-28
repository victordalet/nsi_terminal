import numpy
import random

def ft_guicher(t,p):
	t2 = (t*60)*60
	moyenne = 0
	for i in range(t2):
		moyenne += random.randint(30,299)
	moyenne /= t2
	nb_client = [random.randint(120,1799) for i in range(int(t2/(moyenne/10))) if random.random() <= p ]
	c1 = 0
	c2 = 0
	for j in range(len(nb_client)): 
		if nb_client[0] < random.randint(30,299) : 
			c2 += 1
		else :
			c1 += 1
		nb_client.pop(0)


	print("on a {} clients qui sont passée et {} qui sont partis".format(c1,c2))
	print("l'efficacité est de {}%".format((moyenne/c1)*100))



def main():
	ft_guicher(8,1/10)
main()

