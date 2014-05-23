# get the amoutn of cases
T = input()
#iterate through the cases 1 by 1
for t in range(T):
    # get the input of the total COST
    C = input()
    # get the amount of numbers
    L = input()
    # creating a list of the costs from the input
    costs = [int(c) for c in raw_input().split()]
    # a flag
    done = False
    # iterate through the range of numbers
    for i in range(L):
        # iterate through the remaning numbers
        for j in range(i+1,L):
            if costs[i] + costs[j] == C:
                print '%d %d'%(i+1,j+1)
                done = True
                break
        if done:
            break