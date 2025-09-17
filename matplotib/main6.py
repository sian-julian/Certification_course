import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sizes=[20,30,25,25]
labels=['A','B','C','D']
plt.pie(sizes,labels=labels,autopct='%1.1f%%',startangle=90)        #Pie chart
plt.title("pie chart")
plt.show()