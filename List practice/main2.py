grossary=[
    {"item":"Milk","qty":3,"price":28},
    {"item":"apple","qty":3,"price":36},
    {"item":"snickers","qty":2,"price":56}
    ]

print(grossary)

while True:
    print("\n1.Add\n2.Exit\n")
    choice=int(input("Enter your choice:"))
                                                                ######pgm of dictionary inside a list#######
    if choice==1:
        key1=input("Enter Key1:")
        value1=input(f"enter value for {key1}:")
        print()
        key2=input("Enter Key1:")
        value2=input(f"enter value for {key2}:")
        print()
        key3=input("Enter Key1:")
        price=int(input(f"enter value for {key3}:"))
        discount=0.4
        if  price>= 300:
            price=price - (price*discount)
        print()

        new={key1:value1,key2:value2,key3:price}

        grossary.append(new)
        print("updated list:",grossary)
    elif choice==2:
        print("exiting...")
        break
    else:
        print("invalid choice....")