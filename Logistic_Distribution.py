from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)

y = sns.displot(random.logistic(size=1000), kind="kde")
plt.show()

