# a = 3
# b = 4
# c = 5
# total = 1000
# product = 1

# 	#int((a+b)**0.5) = c
# 	# a + b + c = 1000
# 	# c = 1000-a-b
# 	# c = sqrt(a) + sqrt(b)
# 	# 1000 - a - b = sqrt(a) + sqrt(b)
# 	# 1000 = sqrt(a) + sqrt(b) + a + b
# 	# 1000**2 = a + b + a**2 + b**2


# while (1000**2) != (a+b) + a**2 + b**2 and (a + b + c != 1000) and flag = False:
# 	a = a + 1
# 	b = b + 1
# 	c = c + 1
# 	print a
# 	print b
# 	print c


# print a
# print b



# # d = 1
# # while total - int(d**0.5) != c:
# # 	d = d+1




n = 50000
# iterate through every number
for a in range(1,n):
	# iterate through each number that is after i
	for b in range(1,n-a,1):
		c = n - a - b
		if a**2+b**2==c**2 and a < b :
			print a
			print b
			print c
			print a*b*c
