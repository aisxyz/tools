#coding:utf-8
import math

def prime(n):
	if n % 2 == 0 :
		return False
	for i in range(2, int(math.sqrt(n))+1):
		if n % i == 0:
			#print n,i
			return False
	return True
	
def get_primes(start, end):
	if end % 2 == 0:
		end -= 1
	while end >= start:
		if prime(end):
			yield end
		end -= 2
		
if __name__ == "__main__":
	prim_list = list(get_primes(10000,20000))
	#r = [(i, j) for i in prim_list for j in prim_list if i*j == 2599]
	print prim_list