
def bubbleSort(list):
    
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            print(list)
        print("")

# bubbleSort([5, 4, 1, 3, 2])

def selectSort(list):

    for i in range(len(list)-1):
        min = None
        for j in range(i, len(list)):
            if min == None or min > list[j]:
                min = list[j]
                mindex = j
        list[i], list[mindex] = list[mindex], list[i]
        print(list)
        

selectSort([5, 4, 1, 3, 2])