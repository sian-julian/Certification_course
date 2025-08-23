import numpy as np
a=np.array([1,2,3])             #create array
print(a)

print(np.zeros((2,3)))          #zeros
print(np.ones((2,3)))           #ones

b=np.arange(1,12,2)
print(b)   
print(b[1:5])                   #slicing, slice from index 1 to 5
                                #Arange
b1=b.reshape((2,3))
print("reshaped:",b1)           #reshape

c=np.linspace(0,1,5)            #linespace
print(c)

print()
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print("shape:",arr.shape)       #shape-determines shape
print("size:",arr.size)         #size-no of elements
print("data type:",arr.dtype)   #data type