import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

data = {
    "uniform": random.uniform(0, 10, 1000),
    "binomial": random.binomial(10, 0.5, 1000),
    "normal": random.normal(10, 5, 1000),
    "poisson": random.poisson(10, 1000),
    "logistic": random.logistic(10, 5, 1000),
    "exponential": random.exponential(10, 1000),
    "chisquare": random.chisquare(10, 1000),
    "rayleigh": random.rayleigh(10, 1000),
    "pareto": random.pareto(10, 1000),
    "zipf": random.zipf(10, 1000)
}

a = sns.displot(data, kind = "kde")
plt.show()

b = random.uniform(0,20,10)
print(b)

#random.logistic : just like normal distribution but for large number of data. ex:- logistic regression
#random.multinomial : just like binomial distribution but for n number of trials.
#random.exponential : Used to model waiting time until an event occurs.
#random.chiSquare : Are these observed frequencies significantly different from what we expected?
#random.rayleigh : The Rayleigh distribution is often used when dealing with the magnitude of two-dimensional random components. Magnitude of random signals/components
#random.pareto : Pareto describes situations where a small number of things account for a very large proportion of the total. A few are extremely large, while most are small
#random.zipf : Zipf models situations where rank and frequency have a strong relationship. Rank determines frequency