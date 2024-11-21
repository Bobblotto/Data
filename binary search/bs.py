
list = [1, 5, 3, 2, 4, 10, 8, 9, 7, 6]

def bin_search(targetnum):
    list.sort()

    startind = 0
    endind = len(list)-1

    current = (endind + startind)//2
    
    while startind <= endind:
        if targetnum == list[current]:
            return str(list[current]) + " found at index " + str(current)
        elif targetnum > list[current]:
            startind = current+1
        else:
            endind = current-1
        current = (endind + startind)//2
    return str(targetnum) + " was not found in the list"


print(bin_search(2))
