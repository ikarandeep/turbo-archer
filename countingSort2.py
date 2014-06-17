N = input()
nums = [int(i) for i in raw_input().split()]
counts = [nums.count(n) for n in xrange(100)]
allNums = []
for i in xrange(100):
	z = 0
	while z < counts[i]:
		allNums.append(i)
		z+=1
print ' '.join(map(str,allNums))