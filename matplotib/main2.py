import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x=np.random.rand(50)
y=np.random.rand(50)
plt.scatter(x,y,color='red',marker='x')             #Scatter plot
plt.title("Scatter plot")
plt.show()