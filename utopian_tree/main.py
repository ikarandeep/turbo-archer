T = input()
#iterate through the cases 1 by 1
for t in range(T):
	N = input()
	height = 1
	for n in range(N):
		if n % 2 == 0:
			height = height*2
		else:
			height = height+1
	print height




		# 0 = 1
		# 1 = 2
		# 2 = 3
		# 3 = 6
		# 4 = 7
		# 5 = 14
		# 6 = 15
		# 7 = 30
		# 8 = 31
		# 9 = 62
		# 10 = 63
		# 11 = 126
