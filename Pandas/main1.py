import pandas as pd

s=pd.Series([10,20,30,40])
print(s)

#2 dimensional data structure
print()

data={'Name':['Alice','bob','sian','siya','anvi','abin'],'Age':[25,20,None,12,34,45]}
df=pd.DataFrame(data,index=['a','b','c','d','e','f'])
print(df)

print()
# print(df.head())
# print()
# print(df.tail())
# print()
# print(df.info())
# print()
# print(df.describe())
# print()

# print(df.columns)
# print()
# print(df.shape)
# print()


# print(df.loc['a'])
# print(df.loc['b','Name'])
# print(df.loc[:,['Name','Age']])
# print()

# print(df.iloc[0])
# print(df.iloc[1,0])
# print(df.iloc[:,0:2])

# print()
# print(df.isnull)
# print()

print(df.dropna())
print()
print(df.fillna(25))

