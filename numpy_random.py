
from numpy import random

b = random.rand(10)
c = random.rand(3,5)
d = random.randint(9)
e = random.randint(9, size = (3,5)) 
a = random.choice([3,5,5,6,7,8,9,1,2], size = (3,2))

print(b)
print(c)
print(d)
print(e)
print(a)