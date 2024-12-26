
def bubbleSort(list):
    
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            print(list)
        print("")

# bubbleSort([5, 4, 1, 6, 3, 2])

def selectSort(list):

    for i in range(len(list)-1):
        min = None
        for j in range(i, len(list)):
            if min == None or min > list[j]:
                min = list[j]
                mindex = j
        list[i], list[mindex] = list[mindex], list[i]
        print(list)
        

# selectSort([5, 4, 1, 6, 3, 2])

def mergeSort(list):

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
        if left[i] < right[j]:
            newlist.append(left[i])
            i += 1
        else:
            newlist.append(right[j])
            j += 1
    

    """ while i < len(left):
        newlist.append(left[i])
        i += 1
    while j < len(right):
        newlist.append(right[j])
        j += 1 """
    
    newlist.extend(left[i:])
    newlist.extend(right[j:])

    return newlist
    # return left, right


    

print(mergeSort([5, 4, 1, 6, 3, 2]))
