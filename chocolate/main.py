# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range (0,T):
    N,C,M = [int(x) for x in raw_input().split(' ')]

    W = N/C
    chocolate_bars_eaten = W
    while(W/M >= 1):
    	chocolate_bars_eaten = chocolate_bars_eaten + (W/M)
    	# how many remaing wrappers are there?
    	W = W%M + (W/M)
    print chocolate_bars_eaten