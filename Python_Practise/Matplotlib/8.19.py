import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
from pandas import Series,DataFrame
#别用pylab，直接用pyplot就好了，pyplot是matplotlib中的一个模块

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()


n = 20
Z = np.random.uniform(0,1,n)
pie(Z), show()



data=Series(np.random.randn(1000),index=np.arange(1000))
data=data.cumsum()
data.plot()
plt.show()