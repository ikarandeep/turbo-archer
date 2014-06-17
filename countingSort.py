N = input()
nums = [int(i) for i in raw_input().split()]
counts = [nums.count(n) for n in xrange(100)]
print ' '.join(map(str,counts))