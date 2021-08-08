
# Question 8

# Socho aapke paas do lists hain.
# Ab aapko nayi list banani hai jisme dono lists ke elements hone chaiye. 
# Lekin yeh dhyan mein rakhna hai ki dono lists ke saare elements sirf ek-ek baar hi hone chaiye.
# Agar humare paas yeh do lists hain:
 
# list1 = [1, 5, 10, 12, 16, 20]
# list2 = [1, 2, 10, 13, 16] 

# Toh humari nayi list yeh hogi:
 
# new_list = [1, 2, 5, 10, 12, 13, 16, 20] 

list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
for i in range(len(list2)):
    for j in list1:
        if j not in list2:
            list2.append(j)
print(list2)



