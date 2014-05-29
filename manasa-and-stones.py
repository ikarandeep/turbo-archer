T = input()

for t in range(T):
	steps = input()-1
	a = input()
	b = input()
	maxNum = max(a,b)
	minNum = min(a,b)
	combinations = []
	end = steps*maxNum
	combinations.insert(0,end)
	# iterate through the steps starting at the top
	while steps > 0:
		end = end-maxNum+minNum
		if end not in combinations:
			combinations.insert(0,end)
		steps = steps -1

	print ' '.join(str(s) for s in combinations)