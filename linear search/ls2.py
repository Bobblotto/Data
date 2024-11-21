
list = [1, 5, 3, 2, 4, 10, 8, 9, 7, 6]

targetnum = 5

numfound = False
current = 0

for num in list:
    current += 1
    if num == targetnum:
        numfound = True
        break

if numfound:
    print("Number", targetnum,"found at index", current)
else:
    print("Number", targetnum, "not in the list")