import numpy as np
# import random
#Math Operations

a=np.array([1,2,3,4,5])
print("original array:",a)
print(np.mean(a))           #Mean
print(np.median(a))         #Median
print(np.std(a))            #Standard Deviation

print()
b=np.random.rand()  
print(4)
b=np.random.rand(5)
print(b)
print()
b=np.random.rand(2,3)
print(b)
print()

c=np.random.randint(1,10)
print(c)
print
c=np.random.randint(0,100,size=5)
print(c)