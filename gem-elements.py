# each element is represented by a-z
# an element can be represented multiple times in a rock
# an element is called a "gem-element"  if it occurs at least once in each of the rocks

# input N = num of rocks
# each line contains rock compositions
# each composition consists of letters

# what

N = input()
found = []
for i in range(N):
	temp = list("".join(set(raw_input()))) + found
	if len(found) > 0:
		found = list(set([i for i in temp if temp.count(i) > 1]))
	elif i == 0:
		found = list(set(temp))
print len(found)