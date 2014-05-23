T = input()
for t in range(T):
	bulbs = input()
	num = 1
	if bulbs > 1:
		for b in range(bulbs):
			b = b + 1
			num = num*b
			if b == bulbs:
				print b
		#print num - ()
	else:
		print 1


# 3
# on on on
# on on off
# on off on
# on off off
# off on on
# off on off
# off off on
# off off off

# 4
# on on on on
# on off off off
# on on off off
# on on on off
# on off on off
# on off off on
# off off off off
# off on on on
# off off on on
# off on off on
# off on on off
# off off on

#5
#on on on on on
#on off on on on
#on on off on on
#on on on off on
#on on on on off
#on off off on on
#on off on off on
#on off on on off
#on on off off on
#on on off on off


