def selection_sort(num):
	# print the list before we sort to see what it looks like
	print num

	# iterate through the list
	for i in range(len(num)):
		# the first item we want to swap is at index 0
		# key = num[0]
		key = num[i]
		index = 0
		# we want to iterate through the list each time so we can find the smallest number and compare it to the key
		# the z = 0 will let the while loop start at index 0.
		z = i+1

		# iterate through the while. we want to check every single value
		while z < len(num):
			# find the smallest number
			if num[z] < key:
				key = num[z]
				index = z
			z=z+1
		if key == num[index]:
			num[index] = num[i]
			num[i] = key
	print num



theList = [36,6,3,103,82,5]
selection_sort(theList)