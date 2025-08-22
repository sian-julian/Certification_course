subjects=set()

while True:
    print("***SUBJECT***")
    print("1.ADD\n2.REMOVE\n3.VIEW\n4.EXIT\n")

    choice=int(input("Enter your choice:"))

    if choice==1:
        sub=input("Enter the subject name:")
        subjects.add(sub)

        print("Subject added successfully!!\n")
    
    elif choice==2:
        if subjects:
            rem=input("Enter the subject to remove:")

            if rem in subjects:
                subjects.remove(rem)
                print("Subject removed successfully!!\n")
            else:
                print("subject not found!!\n")
        else:
            print("no subjects added!!\n")
    
    elif choice==3:
        if subjects:
            print(subjects)
        else:
            print("no subjects added!!\n")
    
    elif choice==4:
        print("exiting..")
        break
    else:
        print("Invalid choice!! try again...")

