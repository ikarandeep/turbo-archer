def reverseStringRecursive(string):
	if string != "":
		# chop off the last letter
		print string[-1:]
		print "remaining: " + string[:-1]
		return string[-1:] + reverseStringRecursive(string[:-1])
	else:
		return ""



print reverseStringRecursive("john")