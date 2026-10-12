from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

a = random.binomial(n=10,p=0.5,size=10)
print(a)

b = sns.displot(random.binomial(n=1,p=0.5,size=100),kind="kde")
plt.show()

c = sns.displot({
    "normal":random.normal(loc=1,scale=4,size=1000),
    "binomial":random.binomial(n=10,p=0.5,size=1000)
    })
plt.show()