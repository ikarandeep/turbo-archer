cases = int(raw_input())
case = 1
if cases < 1 and cases > 50:
        print "error"
else:
    while case <= cases:
        skip=0
        howMuchToSpend = int(raw_input())
        if howMuchToSpend < 2 or howMuchToSpend > 100000:
            print "1skipping"
            skip=1
        numberOfFlavors = int(raw_input())
        if numberOfFlavors < 2 or numberOfFlavors > 100000:
            skip=1
        costOfFlavorsList = raw_input().split()
        for c in costOfFlavorsList:
            if int(c) < 1 or int(c) > 100000:
                skip=1         
        currentFlavorIndex = 1
        combinationList = []
        while currentFlavorIndex <= numberOfFlavors and skip==0:
            # take the cost of the current flavor
            i=0
            currentFlavorIndexCost = int(costOfFlavorsList[currentFlavorIndex-1])
            for flavor in costOfFlavorsList:
                i=i+1
                flavor = int(flavor)
                if i != currentFlavorIndex:
                    # take the current flavor and add it to the next one and check if its = 4
                    total = currentFlavorIndexCost+flavor
                    if total == howMuchToSpend:
                        flag=0
                        if len(combinationList) == 0:
                            flag=1
                        
                        for combo in combinationList:
                            if ((combo[0] == currentFlavorIndex and combo[1] == i) or (combo[1] == currentFlavorIndex and combo[0] == i)):
                                break
                            else:
                                flag=1
                       
                        if flag == 1:
                                print currentFlavorIndex, i
                                combination =[currentFlavorIndex, i]
                                combinationList.append(combination)
                                skip=1
                        
            currentFlavorIndex = currentFlavorIndex + 1
        case = case + 1