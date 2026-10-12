import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

a = random.normal(size = (3,3))
print(a)
print()

b = random.normal(loc=1,scale=2,size=(3,3))
print(b)
print()

c = sns.displot(random.normal(size = 1000), kind = "kde")
plt.show()


