L1 = []
L2 = []
L1 = [1]
L1 = [1,2]
L1 = [1,2,3]
L1 = [1,2,3,4]
L2 = [1]
L2 = [2,1]
L2 = [3,2,1]
L2 = [4,3,2,1]

#####################################

F = []
F = [4]
F = [4,1]
F = [4,1,3]
F = [1,3] ;  N = 4
F = [1,3,8]
F = [3,8] ;  N = 1

###################################

F1 = ['A','B','C','D','E']
P1 = [None,None,None,None,None]
P2 = [None,None,None,None,None]
counter = 0
for i in F1:
	P1[counter] = i
	counter += 1
for j in F1:
	N = depiler(P1)
	empiler(P2,N)

