string = raw_input()
a = len(string)
total = 0
i = 0
modulo = 10**9+7
offset = 0
# reverses the order (-1,-1)
for j in range(a-1,-1,-1):
	num = int(string[j])
	print num
	offset = (10*offset)%modulo + 1
	print offset