T = input()
#iterate through the cases 1 by 1
for t in range(T):
	number = input()
	original_number = float(number)
	i = 0
	while number:
		# get the digit
		digit = number % 10
		number /= 10
		if digit != 0:
			if (original_number/float(digit))%1 == 0:
				i = i+1
	print i
