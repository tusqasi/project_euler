import math 

def if_is_prime(p):
	"""
	a func made to find if given number is prime or not 
	gives b

	"""
	x = 0
	for z in range(int(math.ceil(math.sqrt(p)))-1,2,-1):
		if p%z==0:
			x = False
			break
		else:
			x = True
	return x

n = 600851475143
s_o_n = math.sqrt(n)
factors = []

for i in range(int(s_o_n),2,-1):

	if n%i==0:
		if if_is_prime(i)==True:
			print(i)
			break


