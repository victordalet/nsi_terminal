import random
def trie(t):

	if len(t) == 1:
		return t

	t1 = trie(t[0:len(t)//2])
	t2 = trie(t[len(t)//2:])

	return fusion(t1, t2)


def fusion(t1,t2):

	if t1 == []:
		return t2

	elif t2 == []:
		return t1

	elif t1[0] < t2[0]:
		return [t1[0]] + fusion(t1[1:],t2) 

	else:
		return [t2[0]] + fusion(t1,t2[1:])


def main():
	n = 1005
	t = [random.randint(0,50) for i in range(n)]
	print(t)
	print(trie(t))

main()