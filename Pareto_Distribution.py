from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = sns.displot(random.pareto(a=2, size=1000))
plt.show()

y = random.pareto(a=2, size=(2, 3))
print(y)