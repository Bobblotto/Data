
def powerBasic(num, power):

    newnum = num

    while power > 1:
        newnum *= num
        power -= 1
    return newnum

# print(powerBasic(2, 3))

def powerRec(num, power):

    if power == 0:
        return 1 # num ^ power * 1
    else:
        return powerRec(num, power-1) * num

# n^m = n^m-1 * n
# 2^3 = 2^2 * 2

# print(powerRec(2, 3))

def fibBasic(amnt):

    fir = 0
    sec = 1
    print(fir)
    print(sec)

    while amnt > 2: # exluciding previous 2

        amnt -= 1
        
        thi = fir + sec
        fir = sec
        sec = thi

        print(thi)

#fibBasic(6)

def fibRec(n):

    if n == 1 or n == 0:
        return n
    else:
        return fibRec(n-1) + fibRec(n-2)


print(fibRec(6))