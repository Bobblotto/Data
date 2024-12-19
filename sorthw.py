
players = ["Zach", "Andy", "Isaac", "Beth", "Daniel", "Ronald", "Donald"]

def bubbleSort(list):
    
    comps = 0
    swaps = 0

    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            comps += 1
            if list[j] > list[j+1]:
                swaps += 1
                list[j], list[j+1] = list[j+1], list[j]
    
    print("Comparisons(bubble): "+str(comps))
    print("Swaps(bubble): "+str(swaps))

bubbleSort(players)

def selectSort(list):

    comps = 0
    swaps = 0

    for i in range(len(list)-1):
        min = None
        for j in range(i, len(list)):
            comps += 1
            if min == None or min > list[j]:
                min = list[j]
                mindex = j
        swaps += 1
        list[i], list[mindex] = list[mindex], list[i]
    
    print("Comparisons(select): "+str(comps))
    print("Swaps(select): "+str(swaps))
        

selectSort(players)