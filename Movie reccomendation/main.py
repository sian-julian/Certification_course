user_A={"Nezha","Superman","fantastic 4","Elementals","Thunderbolts"}
user_B={"Coolie","Revenant","F1","Nezha","Thudarum"}

print("First User movies:",user_A)
print("Second User movies:",user_B)

common=user_A.intersection(user_B)
A_diff=user_A.difference(user_B)

sugg_B=user_B.difference(user_A)

print("Movies both have watched: ",common)
print("Movies unique to User A:",A_diff)
print("Suggested movies for User A based on User B’s watched list:",sugg_B)
