
def naturalNumBasic(num):

    n_num = num

    while num > 0:
        num -= 1
        n_num += num
    
    #print(n_num)

naturalNumBasic(5)

def naturalNumRec(num):

    if num <= 1:
        return 1
    else:
        return naturalNumRec(num-1) + num

print(naturalNumRec(5))

# s(n) = s(n-1) + n
# s(5) = 1 + 2 + 3 + 4 + 5

def factorialBasic(num):

    f_num = num

    while num > 1:
        num -= 1
        f_num *= num
    
    # print(f_num)

factorialBasic(5) # !

def factorialRec(num):

    if num == 1 or num == 0:
        return 1
    else:
        return factorialRec(num-1) * num

print(factorialRec(3))