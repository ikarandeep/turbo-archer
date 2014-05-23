
# iterate through each item in the array starting from the second item
def increasingOrder(num):
	for index in range(0,len(num)):
		# the number to check is the one at the index
		key = num[index]
		# we want to check to see if the item below key is greater or less
		i = index - 1
		# keep checking to see if its less --> figure out which "i" we need to put the key in
		# each time we are in this while loop
		while i >= 0 and num[i] > key:
			num[i+1] = num[i] 
			i = i - 1
		num[i+1] = key
	print num

def decreasingOrder(num):
	print num
	for index in range(0,len(num)):
		# the number to check is the one at the index
		key = num[index]
		# we want to check to see if the item below key is greater or less
		i = index - 1
		# keep checking to see if its less --> figure out which "i" we need to put the key in
		# each time we are in this while loop
		while i >= 0 and num[i] < key:
			num[i+1] = num[i] 
			i = i - 1
		num[i+1] = key
	print num


num = list("524613")

#increasingOrder(num)
decreasingOrder(num)
