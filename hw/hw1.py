import numpy as np

lis = np.arange(3, 28, 3)
lis = lis.reshape(3, 3)

# -------------------------------------------------------------
# Solve the linear equation
# 2x + 3y = 8
# 5x - y = 4

eq = np.array([[2, 3], [5, -1]])
ans = np.array([8, 4])

eqM = np.matrix([[2, 3], [5, -1]])
ansM = np.matrix([[8], [4]])

inverseEqM = np.linalg.inv(eqM)
print(inverseEqM)

done = inverseEqM * ansM
print(eqM * done)
print(done)