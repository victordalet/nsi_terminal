def max_dico(dico):
	like_max = 0,0
	for key,element in dico.items():
		if dico[key] > like_max[0]:
			like_max = dico[key],key
	return like_max

def main():
	print(max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}))

main()