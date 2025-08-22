# items=["apple","orange","peer","grapes"]
# print(items)
# print(items[0])
# print(items[1:3])

# items.append("watermelon")
# items.append(["milk","soap"])
# print(items)

# if "milk" in items:
#     print("item is present")
# else:
#     print("item not found")

# items.remove("orange")
# print(items)

# while True:
#     print("1.Add\n2.view\n3.Exit")
#     choice=int(input("Enter your choice:")) 

#     if choice==1:
#         new_item=input("Enter new item:")
#         items.append(new_item)
#         print("item add successfully!!")
#     elif choice==2:
#         print("all the items:\n",items)
#     elif choice==3:
#         print("exiting...")
#         break
#     else:
#         print("invalid choice!!..try again")

# for i,it in enumerate(items,start=1):
#     print(i,it)


grossary=[
    {"item":"Milk","qty":3,"price":28},
    {"item":"apple","qty":3,"price":36},
    {"item":"snickers","qty":2,"price":56}
    ]

print(grossary)

while True:
    print("\n1.Add\n2.Exit\n")
    choice=int(input("Enter your choice:"))

    if choice==1:
        key1=input("Enter Key1:")
        value1=input(f"enter value for {key1}:")
        print()
        key2=input("Enter Key1:")
        value2=input(f"enter value for {key2}:")
        print()
        key3=input("Enter Key1:")
        value3=input(f"enter value for {key3}:")
        print()

        new={key1:value1,key2:value2,key3:value3}

        grossary.append(new)
        print("updated list:",grossary)
    elif choice==2:
        print("exiting...")
        break
    

