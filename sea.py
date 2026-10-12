import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

a = sns.displot([random.randint(100) for x in range(100)], kind = "kde")
plt.show(a)

b = sns.displot([12,34,5,5,66,5,4,89,3,2,1,29,3,90])
plt.show(b)