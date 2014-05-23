string = raw_input()
i = 0
total = 0
m = 10**9+7
for letter in string:
	z = i+1
	while i+z < len(string)+1:	
		total = (int(string[i:i+z])%m + total)%m
		print "i = ", i
		print "total = ", total
		z = z + 1
	i = i + 1
print total