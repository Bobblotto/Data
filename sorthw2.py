
players = [6, 1, 3, 2, 4, 5]

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


def mergeSort(list):

    comps = 0
    swaps = 0

    if len(list) <= 1:
        return list

    midindex = len(list)//2
    left = list[0 : midindex] # slice list
    right = list[midindex:]

    left = mergeSort(left)
    right = mergeSort(right)

    newlist = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        comps += 1
        if left[i] < right[j]:
            swaps += 1
            newlist.append(left[i])
            i += 1
        else:
            swaps += 1
            newlist.append(right[j])
            j += 1
    
    newlist.extend(left[i:])
    newlist.extend(right[j:])
    swaps += len(left[i:]) + len(right[j:])
    
    print("Comparisons(merge): "+str(comps))
    print("Swaps(merge): "+str(swaps))

    return newlist

#Comparisons(merge): 3
#Swaps(merge): 6

mergeSort(players)