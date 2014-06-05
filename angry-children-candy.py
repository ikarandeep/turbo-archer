# the below code does not work... using python's built in .sort method works better

# N = input()
# K = input()
# i = 0
# candies=[]
# while i < N:
# 	numOfCandiesInPacket = input()
# 	if len(candies)==K:
# 		maxInCandies = max(candies)
# 		if numOfCandiesInPacket < maxInCandies:
# 			candies.remove(maxInCandies)
# 			candies.append(numOfCandiesInPacket)
# 	else:
# 		candies.append(numOfCandiesInPacket)
# 	i+=1
# print max(candies) - min(candies)

N = input()
K = input()
i = 0
candies=[]
while i < N:
	candies.append(input())
	i+=1
candies.sort()
i=0
minUnFairness = []
while K+i < len(candies):
	minUnFairness.append(candies[K-1+i] - candies[i])
	i+=1
print min(minUnFairness)