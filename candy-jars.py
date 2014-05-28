N, M = raw_input().split()


candies = 0
# faster way to do:
for eachLine in range(int(M)):
	a,b,amount = raw_input().split()
	candies = ((int(b)+1 - int(a))*int(amount)) + candies


print candies/(int(N))


# iterate through all the lines
# #jars = [0]*N


# for eachLine in range(int(M)):
# 	a,b,amount = input().split()
# 	for i in range(a,b+1):
# 		jars[i] = jars[i] + int(amount)


# get the average
