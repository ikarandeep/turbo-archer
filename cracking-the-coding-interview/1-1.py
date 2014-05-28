
# o(n)
# it needs to iterate through the whole string
# can we make it smaller
# can it be less?


string="abcdefabcde"
for i in string:
	if string.count(i) == 1:
		print i