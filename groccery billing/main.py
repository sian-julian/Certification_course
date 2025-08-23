
items=["milk", "bread", "egg"]
prices=[40, 25, 5]
total_bill=0

print("Available items:")
for i in range(len(items)):
    print(f"{items[i]} - Rs.{prices[i]}")

while True:
    item=input("\nEnter item bought (or 'done' to finish):").lower()
    
    if item=="done":
        break
    
    if item in items:
        qty=int(input(f"Enter quantity of {item}: "))
        index=items.index(item)
        cost=qty*prices[index]
        total_bill+=cost
        print(f"Added {qty} {item}(s) = Rs.{cost}")
    else:
        print("Item not available!")

discount = 0
if total_bill > 1000:
    discount = 0.2
elif total_bill > 500:
    discount = 0.1

final_bill=total_bill-(total_bill*discount)

print("\n***")
print(f"Total Bill:Rs.{total_bill}")
print(f"Discount Applied:{discount*100}%")
print(f"Final Bill after discount:Rs.{final_bill}")
print("***")
