# find all multiples of 3 or 5 below N

N = 1000

total = 0

for num in range(1,N):
	if num%3 == 0:
		total = total + num
	elif num%5 == 0:
		total = total + num
print total
