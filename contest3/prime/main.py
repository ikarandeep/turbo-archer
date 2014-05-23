def check_prime(num):
	sum_of_primes = 0
	Flag = True
	factors = []
	for i in range(2,num):
		print "num & i = ", num, i
		if num % i == 0:
			sum_of_primes = i + sum_of_primes
			Flag = False;
			factors.append(i)
			#if i*2 || i+sum_of_primes 
			break
	#return all(num % i for i in range(2,num))
	print factors
	return Flag


T = input()
for t in range(T):
	N,K = raw_input().split()
	print check_prime(int(N))


# cases
# 10 2 : yes
# 1 6 : no
# 100 3 : ?