s_cart=[]

while True:
    print("***SHOPPING CART***")
    print("1.ADD\n2.REMOVE\n3.UPDATE\n4.VIEW\n5.SEARCH\n6.SLICE\n7.SORT\n8.EXIT\n")

    ch=int(input("Enter your choice:"))

    if ch==1:
        name=input("Enter an item:")
        s_cart.append(name)
        print("Item Added Successfully!!\n")

    elif ch==2:
        rem=input("enter the element to remove:")
        found=False

        for item in s_cart:
            if s_cart[item]==rem:
                s_cart.remove(rem)
                print("Item removed successfully!!\n")
                found=True
                break
        
        if found==False:
            print("No element found!!\n")
        
    elif ch==3:
        if s_cart:
            item=input("Enter the name of the item:")

            if item in s_cart:
                found=True
                up_item=input("Enter the updated name of the item:")
                index=s_cart.index(item)
                s_cart[index]=up_item
                print("item updated successfully!!\n")
            else:
                print("No element found!!")
                print()
        else:
            print("No elements added!!\n")
        
    elif ch==4:
        print("View all items")

        if s_cart:
            print(s_cart)
        else:
            print("no Added elements!!")
            print()

    elif ch==5:
        if s_cart:
            search=input("Enter the item to search:")

            if search in s_cart:
                    print(f"{search} is found in {s_cart[item]} position")
            else:
                print("item not found\n")
        else:
            print("No Items added\n")

    elif ch==6:
        if s_cart:
            start=int(input("Enter start index:"))
            end=int(input("Enter end index:"))
            print("Sliced items:",s_cart[start:end])
        else:
            print("no elements found!!\n")
    
    elif ch==7:
        if s_cart:
            s_cart.sort()
            print("the sorted shopping cart:",s_cart)
        else:
            print("no Elements added\n")
    elif ch==8:
        break



        
            
            
        
    
