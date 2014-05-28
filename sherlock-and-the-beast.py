def decentNum(N):
	if N < 8 and N%3 != 0 and N%5 !=0:
		return -1
	# if N does not have 
	elif N%3 == 0:
		return int(''.join(map(str,[5]*N)))
	elif N == 5:
		return int(''.join(map(str,[3]*N)))
	else:
		flag = False
		amountOf5s = N
		while (amountOf5s-5)%3 != 0:
			amountOf5s = amountOf5s - 5
		amountOf5s = amountOf5s - 5
		amountOf3s = N - amountOf5s
		return int(''.join(map(str,[5]*amountOf5s+[3]*amountOf3s)))

T = input()
for i in range(T):
	print decentNum(input())


		# N will represent the amount of digits in the value to be returned
		# so example
		# N = 3,
		# this means there are 3 digits in it
		# the digits can eitehr be 3 or 5
		# so we have
		# 3 3 3
		# 3 3 5
		# 3 5 3
		# 3 5 5
		# etc...
		# brute force would be really slow here
		# must be an algorithm for it...
		# if the number is less than 5, then the value is
		# if the number is 10 digits, what combinations can we have?
		# 3 appears 10 times
		# if 11 digits:
		# 3 apperas 5 times and 5 appears 6 times
		# if 12 digits
		# 5 appear 12 times
		# if 13 digits
		# 5 appears 3 times
		# 3 appears 10 times
		# if 14 digits
		# 3 appears 5 times
		# 5 apperears 9 times
		# if 15 digits
		# 5 appears 15 times
		# if 16 digits
		# 16 - 5 = 11%3 == 0? no
		# 16 - 10 = 6%3 == 0? yes
		# 5 appears 6 times
		# 3 appears 10 times
		# if 17 digits
		# 17 - 5 = 12%3 == 0? yes
		# 5 appears 12 times
		# 3 appears 5 times
		# if 18 digits
		# 18 - 5 = 13%3 ==0? no
		# 18 - 10 = 8 % 3 ==0? no
		# 18 - 15 = 3%3 == 0? yes
		# 555 15 3's
		# 5 5 5 3 3 3 3 3
		# 
		# 10 -> ()
		# a/5 + b/3 = N
		#15(3a + 5b) = N
		#3a + 5b = N/15


		# number of times 3 apperas is divisble by 5
		# number of times 5 appears is divisble by 3




