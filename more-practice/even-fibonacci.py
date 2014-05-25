max_fibonacci_num = 4*(10**6)
prev = 1
num = 2
total = 2
while num <= max_fibonacci_num:
	tmp = prev + num
	prev = num
	num = tmp
	if num%2 == 0:
		total = total + num
print total