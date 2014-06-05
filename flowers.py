# K = amount of people
# N = amount of flowers
# second flower will cost:
# (x+1)*C
# (2)*cost
K,N = [int(i) for i in raw_input().split()]
C = []

numbers = [int(i) for i in raw_input().split()]
numbers.sort()
numbers.reverse()
if (K/N) == 1:
	print sum(numbers)
else:
# each person can buy N/K
# if N/K = 3: each person buys 3.
# person 1 buys 0,3,6
# person 2 buys 1,4,7
# person 3 buys 1,5,8
# still have two left
# person 1 buys 9
# person 2 buys 10
	totalCost = 0
	for person in range(K):
		personsFlowers = []
		i = 0
		while i < N/K:
			personsFlowers.append(numbers[person+K]*i+1)
			i+=1
		totalCost+=sum(personsFlowers) 
	print totalCost
# iterate through the list backwards... first person buys the most expensive first
# for eachPerson in range(K):
# 	for cost in numbers:
# 		cost = prev