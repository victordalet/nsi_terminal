def ft_has_parenthesis(element):
	P1 = []
	P2 = []
	for i in element:
		if i == '(':
			P1.append(i)
		elif i == ')':
			P2.append(i)
	if len(P1) == len(P2):
		return True
	else :
		return False



def main():
	print(ft_has_parenthesis('((()())'))
	print(ft_has_parenthesis('((())) '))
	print(ft_has_parenthesis('()(()()'))

main()