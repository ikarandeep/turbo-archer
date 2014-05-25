# 3 digits * 3 digits = 6 digits
# start from the largest 3 digit number: 999
a = 999
numbers = []
while a > 100:
	b = 999
	while b > 100:
		digits = list(str(a*b))
		mid = len(digits)/2
		first = digits[0:mid]
		second = digits[mid:len(digits)]
		if first == second[::-1]:
			numbers.append(a*b)
		b = b -1
	a = a-1
print max(numbers)

# the last 3 digits of the number will be b * the last digit of number a
# the first 3 digits will be
#hile ([i for i in list(a*b)][0]
