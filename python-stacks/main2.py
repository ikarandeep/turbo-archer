class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)


# if a string of parentheses is entered, write an algorithm to check if its balanced
def parChecker(symbolString):

	# create the stack

	s = Stack()
	
	# set a boolean to determine if its balanced or not
	balanced = True

	# start at 0
	index = 0

	# iterate through the string
	# only when its balanced
	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		print symbol

		# if its an opening parenthese, add it to the stack
		if symbol == "(":
			s.push(symbol)
		else:

			# if the stack is empty and we dont have an opening parenthese, then we messed up!
			if s.isEmpty():
				balanced = False
			else:
				# else pop the parenthese from the stack
				s.pop()
		index = index + 1
	if balanced and s.isEmpty():
		return True
	else:
		return False


def divideBy2(decNumber):
	remstack = Stack()

	# only valid for numbers greater than 0
	while decNumber > 0:
		# whats the remainder of the number after we divide it by 2?
		rem = decNumber % 2 
		# add the remainder to the stack
		remstack.push(rem)
		# the new number is the number divided by 2
		decNumber = decNumber / 2

	binString = ""
	# while the stack is not empty, keep popping the stack to create the bin we want
	while not remstack.isEmpty():
		binString = binString + str(remstack.pop())

	return binString


print divideBy2(1059015)


