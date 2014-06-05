def isFib(N):
	# if the number is less than 0 than its not a Fib
	if (N <= 0):
		return "IsNotFibo"
	# start at 0
	a = 0
	# the first fib is 1 -> second fib-> 0 + 1 = 1 (the second fib is 1 also)
	b = 1
	# start i at 1
	i = 1
	# a while loop can also be used
	# while(i<=N): 
	# the i statement at the end must be included
	# range(N) cannot be used. it causes memory issues
	# in Python 3 it should work however
	for i in xrange(N):
		fib = a+b
		if fib == N:
			return "IsFibo"
		elif fib > N:
			return "IsNotFibo"
		else:
			a = b
			b = fib
		#i+=1

T = input()

for t in range(T):
	N = input()
	print isFib(N)
