import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data=np.random.randn(1000)
plt.hist(data,bins=30,color='black',edgecolor='red')        #Histogram
plt.title("Histogram")
plt.show()