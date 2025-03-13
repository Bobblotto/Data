import numpy as np

l1 = [3, 5, 2, 4, 9]
l2 = [5, 2, 1, 7, 8]

l1 = np.array(l1) # converts list to numpy array
l2 = np.array(l2)

print(l1)
print(type(l1))

l3 = np.arange(1, 21, 1) # makes numpy array from first value to last value (last argument is step)
print(l3)

l4 = np.linspace(1, 10, 10) # makes numpy array from first value to last value (last argument is the length of the array)
print(l4)

l5 = np.random.randint(1, 10, size=5) # gives an amount of random integers from first value to last value
print(l5)
print(l1.ndim) # gets dimension of array

l6 = l3.reshape(5, 4) # makes array 2d
print(l6)
print(l6.ndim)

l7 = l3.reshape(2, 2, 5)
print(l7)

l5 = np.random.randint(1, 10, size=(2, 5)) # gives an amount of random integers from first value to last value in a 2d array
print(l5)

l5 = np.random.randint(1, 10, size=(2, 3, 5))
print(l5)

print(np.sqrt(16)) # square root function

print(np.pi) # pi

radius = [5, 2, 3, 7]

for i in radius:
    print("area: ", i**2*np.pi)

radius = np.array(radius)

areas = radius**2*np.pi
print("areas: ", areas)

print(l4[3:7]) # slice

print(l4[[1, 3, 6]]) # get specific indexes

print(l4>5) # shows booleans based on condition
print(l4[l4>5]) # shows numbers that fit the condition
print(l4[l4%2==0])

l8 = np.ones(2) # makes 1d array of 1s
print(l8)

l9 = np.ones((2, 2)) # makes 2d array of 1s
print(l9)

l10 = np.ones((2, 5, 4))
print(l10)

l11 = np.zeros(2) # makes 1d array of 0s
print(l11)