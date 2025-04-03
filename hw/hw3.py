import numpy as np
import time

ltime = 0
atime = 0

ltime = time.time()
lis = []
for i in range(1, 100001):
    lis.append(i)
ltime = time.time() - ltime

atime = time.time()
arr = np.arange(1, 100001)
atime = time.time() - atime

print("List time: ", ltime)
print("Array time: ", atime)