T = input()
#iterate through the cases 1 by 1
for t in range(T):
	numbers = input()
	if numbers % 2 == 0:
		if (numbers/2) % 2 == 0:
			print 3
		else:
			print 4
	else:
		print(2)