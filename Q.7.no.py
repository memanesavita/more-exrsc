


# Socho aapke paas 2 lists hain.
# Aapne aisa code likhna hain jisse ek nayi list banne jisme inn dono 
# lists ke woh item hone chaiye ho dono list mein aa rahe hain. 
# Socho aapki do list yeh hain:
 
# list1 = [1, 342, 75, 23, 98]
# list2 = [75, 23, 98, 12, 78, 10, 1] 

# Inn dono list se aapki nayi list yeh banni chaiye:



list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 
for i in range(len(list2)):
    for j in list1:
        if j not in list2:
            list2.append(j)
print(list2)






