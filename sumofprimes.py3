# This is another CodeEval challenge. This returns the sum of the first 1000 prime numbers.
#

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

primes, total, counter = 0,0,0

while primes != 1000:
	if is_prime(counter) is True:
		total += counter
		primes += 1
	counter +=1

print(total)
