import numpy as np
from numpy import random

a = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.5, 0.1], size=(5))

print(a)
print()

b = random.choice([x for x in range(0,100)], p=[1/100]*100, size=(3,5))
print(b)
print()

c = np.array([1,2,4,5,6,3,6])
random.shuffle(c)
print(c)
print()


d = np.array([1, 2, 3, 4, 5])
print(random.permutation(d))
print()

