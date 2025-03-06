
def prefixChecker(lis):

    lis.sort()

    l1 = lis[0]
    l2 = lis[-1]

    index = 0

    while index < len(l1) and index < len(l2) and l1[index] == l2[index]:
        
        index += 1
    

    return l1[0:index]
            
def prefixChecker2(lis):

    first = lis[0]

    for i in range(len(first)):
        fi = first[i]
        for j in lis[1:]:
            if j[i] != fi or i >= len(j):
                return first[:i]


print(prefixChecker2( ["car", "california", "cadilac"] ))