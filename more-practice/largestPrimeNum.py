def prime_factors(n):
	factors = []
	# divider
	d = 2
	# while the number n is greater than 1:
	while n > 1:
		# while n mod d is 0 aka n is divisble by d and theres no remainder
		while n % d == 0:
			# if n is divisble by d, then we should append the dividor
			factors.append(d)
			# we then want to see 
			n = n/d
		d = d + 1
		if d*d > n:
			if n > 1:
				factors.append(n)
				break
	return factors

# prime factors of 13195 are 5, 7, 13, 29
# what is the largest prime factor of 600851475143?

