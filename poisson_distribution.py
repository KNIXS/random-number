import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

a = random.poisson(3, 10)
print(a)

#b = sns.displot(random.poisson(3, 1000))
#plt.show()

data = {
    "Binomial":random.binomial(3,0.5,10),
    "Normal":random.normal(3,2,10),
    "Poisson":random.poisson(3,10)
    }

c = sns.displot(data,kind = "kde")
plt.show()

