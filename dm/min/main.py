def minimum(liste):
	mini = liste[0]
	for i in liste:
		if i < mini:
			mini = i
	print(mini)
	return mini


def minimumV2(liste):
	print(min(liste))
	return min(liste)

def main():
	minimum([5,1,9,2,8,1])
	minimumV2([5,1,9,2,8,1])

main()