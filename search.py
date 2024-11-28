list = [1, 5, 3, 2, 4, 10, 8, 9, 7, 6]

def bin_search(targetnum):
    newlist = list
    newlist.sort()
    searches = 0
    startind = 0
    endind = len(newlist)-1

    current = (endind + startind)//2
    
    while startind <= endind:
        searches += 1
        if targetnum == newlist[current]:
            return str(targetnum) + " found at index " + str(current) + " with " + str(searches) + " searches"
        elif targetnum > newlist[current]:
            startind = current+1
        else:
            endind = current-1
        current = (endind + startind)//2
    return str(targetnum) + " was not found in the list with " + str(searches) + " searches"

def lin_search(targetnum):
    
    searches = 0
    numfound = False
    current = 0

    for num in list:
        searches += 1
        current += 1
        if num == targetnum:
            numfound = True
            break

    if numfound:
        return str(targetnum) + " found at index " + str(current) + " with " + str(searches) + " searches"
    else:
        return str(targetnum) + " was not found in the list with " + str(searches) + " searches"

print(lin_search(2), " (linear)")
print(bin_search(2), " (binary)")
