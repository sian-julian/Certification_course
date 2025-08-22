stdA={"dancing","swimming","drawing"}
stdB={"cycling","swimming","watching movies"}

common=stdA.intersection(stdB)
print("common hobbies in both sets:",common)

unique_A=stdB.difference(stdA)
print("the hobbies that are unique in stdA:")



total=stdA.union(stdB)
print("all hobbies in  both sets:",total)