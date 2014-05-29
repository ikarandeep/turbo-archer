def isFib(N):
	a = 0
	b = 1
	for i in range(N):
		fib = a+b
		if fib == N:
			return "IsFibo"
		elif fib > N:
			return "IsNotFibo"
		else:
			a = b
			b = fib




T = input()

for t in range(T):
	N = input()
	print isFib(N)
