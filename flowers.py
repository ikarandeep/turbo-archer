N,K = [int(i) for i in raw_input().split()]
C = []
flowers = [int(i) for i in raw_input().split()]
flowers.sort()
flowers.reverse()
lastFlowers = []
while N%K != 0:
	lastFlowers.append(flowers.pop(N-N%K))
	N=N-1
splitArrays = zip(*[iter(flowers)]*(K))
i=0
total=0
while i < N/K:
	total = sum(splitArrays[i])*(i+1)+total
	i+=1
total = sum(lastFlowers)*(i+1)+total
print total