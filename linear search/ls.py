
list = [1, 5, 3, 2, 4, 10, 8, 9, 7, 6]

targetnum = 5

numfound = False
current = 0

while not numfound:
    print(list[current])
    if current >= len(list)-1:
        break
    else:
        if list[current] == targetnum:
            numfound = True
        else:
            current += 1

if numfound:
    print("Number", list[current],"found at index", current)
else:
    print("Number", targetnum, "not in the list")