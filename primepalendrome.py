""" Another CodeEval challenge. This one finds the largest Prime Palendrome under 1000"""

def is_prime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if not n & 1:
		return False
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0:
			return False
	return True

def is_palendrome(n):
	n = str(n)
	if n == n[::-1]:
		return True
	return False

for x in range(1000,0,-1):
	if is_palendrome(x) and is_prime(x):
		print(x)
		break
