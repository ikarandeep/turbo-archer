T = input()
for t in range(T):
	people = input()
	num = 0
	if people > 1:
		for p in range(people):
			num = num + p
		print num
	else:
		print 0