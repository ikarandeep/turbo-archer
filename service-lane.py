# length of highway and service lane is N units
# service lane also consists of N segments while each segment has different widths
# entry segment = i
# exit segment = j
# exit segment > entry segment
# i >=0
# pass all segements from i to j including i and j
# 3 cars
# width of vehicle of length N
# width[k] = width of kth segment
# if width[k] == 1 : only bike
# if width[k] == 2 : bike and car
# if width[k] == 3 : bike car or truck
# N = length of freeway
# T = number of test cases
(N,T) = raw_input().split()
width = [int(i) for i in list(str(raw_input()).split())]
for t in range(int(T)):
	(entry, exit) = [int(i) for i in raw_input().split()]
	print min(width[entry:exit+1])