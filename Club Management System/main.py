def add_club():
    club_name=input("Enter club name:").strip()
    if club_name in clubs:
        print("Club already exists!")
    else:
        clubs[club_name]=set()
        print(f"Club '{club_name}' created successfully!")

def add_member():
    club_name=input("Enter club name:").strip()
    if club_name not in clubs:
        print("Club does not exist!")
        return
    roll=input("Enter roll number:").strip()
    name=input("Enter student name:").strip()
    member=(roll,name)
    if member in clubs[club_name]:
        print("Member already in this club!")
    else:
        clubs[club_name].add(member)
        print("Member added successfully!")

def remove_member():
    club_name=input("Enter club name:").strip()
    if club_name not in clubs:
        print("Club does not exist!")
        return
    roll=input("Enter roll number:").strip()
    name=input("Enter student name:").strip()
    member=(roll,name)
    if member in clubs[club_name]:
        clubs[club_name].remove(member)
        print("Member removed successfully!")
    else:
        print("Member not found in this club.")

def common_members():
    club1=input("Enter first club name:").strip()
    club2=input("Enter second club name: ").strip()
    if club1 not in clubs or club2 not in clubs:
        print("One or both clubs do not exist!")
        return
    common=clubs[club1].intersection(clubs[club2])
    if common:
        print("Common Members:")
        for roll,name in common:
            print(f"{roll} - {name}")
    else:
        print("No common members")

def unique_members():
    club_name=input("Enter club name:").strip()
    if club_name not in clubs:
        print("Club does not exist!")
        return
    others=set()
    for c in clubs:
        if c!=club_name:
            others|=clubs[c]
    unique=clubs[club_name] - others
    if unique:
        print("Unique Members in",club_name)
        for roll,name in unique:
            print(f"{roll} - {name}")
    else:
        print("No unique members.")

def display_clubs():
    if not clubs:
        print("No clubs available.")
        return
    print("\nClubs and Member Count:")
    for club, members in clubs.items():
        print(f"{club}: {len(members)} members")

# Menu
clubs = {}
while True:
    print("\n***Club Management***")
    print("1. Add Club")
    print("2. Add Member to Club")
    print("3. Remove Member from Club")
    print("4. Show Common Members Between Clubs")
    print("5. Show Unique Members of a Club")
    print("6. Display All Clubs and Member Count")
    print("7. Exit")

    choice=input("Enter your choice: ")

    if choice=="1":
        add_club()
    elif choice=="2":
        add_member()
    elif choice=="3":
        remove_member()
    elif choice=="4":
        common_members()
    elif choice=="5":
        unique_members()
    elif choice=="6":
        display_clubs()
    elif choice=="7":
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again")
