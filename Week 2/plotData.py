import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style


style.use('ggplot')

data = pd.read_csv('ex1data1.txt')
arr = np.array(data)
X = arr[:,0]
y = arr[:,1]
plt.scatter(X,y,label='scatter',color='r')
plt.legend()
plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000s')
plt.show()