
def digisum(num, sum):

    if type(num) is list:
        numlist = num
    else:
        numlist = []
        for digit in str(num):
            numlist.append(int(digit))
    
    if numlist:
        sum += numlist[-1]
        numlist.pop(-1)
        return digisum(numlist, sum)
    else:
        return sum

def digisum2(num):

    if num == 0:
        return num
    else:
        return num%10 + digisum2(num//10)

print(digisum2(1234))