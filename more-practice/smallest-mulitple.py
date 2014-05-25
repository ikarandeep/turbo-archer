import largestPrimeNum


total = 1
prime = []
for n in range(1,21):
	prime = largestPrimeNum.prime_factors(n) + prime

print prime
print set(prime)
for num in prime:
	total = num*total
print total

# find the smallest number thats divisble by all nums from 1 to 20
# if its divisble by 20 - then its divisble by 10, 5, 2, 4
# 19 is not disible by anything
# if its divisble by 18 - then its divisible by 9,6,3,2
# 17 is not divisble by anything
# if its divisble by 16 - then its divisble by 8,4,2
# if its divisble by 15 - then its divisble by 5,3
# if its divisble by 14 - then its divisble by 7,2
# 13 is not divisible by anything
# if its divisble by 12 - then its divisble by 6,4,3,2
# 11 is not divisble by anything
# 10 is covered
# 9 is covered
# 8
# 7
# 6
# 5
# 4
# 3
# 2

# find the smallest number thats divisble by all nums from 1 to 10
# 10 - 5,2
# 9 - 3
# 8 - 4,2
# 7
# 6 - 3,2
# 5
