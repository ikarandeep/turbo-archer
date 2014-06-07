N = raw_input()
numbers = [int(i) for i in raw_input().split()]
for i in set(numbers):
	if numbers.count(i) == 1:
		print i
		break