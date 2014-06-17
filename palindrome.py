T = input()
for case in xrange(T):
	# read the line
	chars = [ord(i) for i in raw_input()]
	j = 0
	k = len(chars)-1
	# compare the first letter with the last letter
	# if they are the same, then go to the next one
	# if they are not the same, then decrease the last character by whatever to = the first character
	moves = 0
	while j != k and j < k:
		if chars[j] != chars[k]:
			diff = abs(chars[k]-chars[j])
			moves+=diff
			chars[k] = chars[k]-diff
		j+=1
		k-=1
	print moves