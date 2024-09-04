#TBA Homework 1

def Comb(List1, Var) :
	try :
		K = len(Var)
		Res = [x1 + x2 for x1 in List1 for x2 in Var]
	except :
		if Var - 1 > 1 :
			Res = [x1 + x2 for x1 in Comb(List1, Var - 1) for x2 in List1]
		else :
			Res = [x1 + x2 for x1 in List1 for x2 in List1]
	return Res

def Star(List1, Limit=10) :
	return Union(List1, Comb(List1, Limit))

def Union(List1, List2) :
	return List1 + List2

def Minus(List1, List2) :
	return [x for x in List1 if x not in List2]

def Inter(List1, List2) :
	return [x for x in List1 if x in List2] 

A = ['aca', 'bb', 'c', 'caba']
B = ['a', 'ac', 'baa', 'cbca']
C = ['ba', 'c']

"""
Your friendly paladin here.

Here's how to use this code.

From : To
AA   : Comb(A, 2)
AB   : Comb(A, B)
A*   : Star(A)
AUB  : Union(A, B)
A-B  : Minus(A, B)
A&B  : Inter(A, B)

Additional Infos :
1. You could set the limit of the Star(A, B) by replacing B with any integer
"""

AA = Comb(A, 2)
print('AA Done')
BBB = Comb(B, 3)
print('BBB Done')
CS = Star(C, 20)
print('CS Done')
Res = Minus(Comb(AA, BBB), CS)
print(Res)