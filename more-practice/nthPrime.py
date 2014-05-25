# determine the Nth prime number
# keep an index to keep track of the nth prime
# keep increasing i until we see a prime
# how do we test if i is a prime?
# if we get a prime, increase index

def isPrime(number):
	# 2 is the only even number that is prime
	if number == 2:
		return True
	# even numbers are not prime
	elif number % 2 == 0:
		return False

	# we need to check all the numbers from 1 to the square_root of n to see if they are prime
	max_num = (int(number**0.5))+1
	# start checking at 3
	z = 3
	while z <= max_num:
		# if the number is divisble by any of the other numbers, then its not prime
		if number % z == 0:
			return False
		# we dont need to check even numbers so increase by 2
		z = z+2

	return True


N = 10001

index = 1
i = 2
prime = 0
while index <= N:
	# is i prime?
	if isPrime(i):
		index = index + 1
		prime = i
		print "prime = ",prime
	i = i + 1

print prime