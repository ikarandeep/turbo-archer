def convert_letter_to_number(letter):
	number = ord(letter) - 96
	return number

def get_amount_of_operations(n1,n2):
	return abs(convert_letter_to_number(n2)-convert_letter_to_number(n1))


T = input()
for t in range(T):
	letter_list = list(raw_input())
	letter_list_len = len(letter_list)
	if letter_list_len %2 == 0:
		middle_bottom = (letter_list_len/2)-1
		middle_top = (letter_list_len/2)
		operations = get_amount_of_operations(letter_list[middle_bottom],letter_list[middle_top])
		i = 1
		while ((middle_bottom-i) > -1 ):
			bottom = middle_bottom-i
			top = middle_bottom+1+i
			operations = get_amount_of_operations(letter_list[bottom],letter_list[top]) + operations
			i = i+1
	else:
		# we know the lenght
		# determine the middle number
		middle = int(round(letter_list_len/float(2)))-1
		middle_letter = letter_list[middle]
		i = 1
		operations = 0
		while ((middle-i) > -1):
			if letter_list[middle-i] == letter_list[middle+i]:
				i = i+1
			else:
				bottom = middle-i
				top = middle+i
				operations = get_amount_of_operations(letter_list[bottom],letter_list[top]) + operations
				i = i+1
				# determine the distance betwe
	print operations

