

# Question 6

# Socho aapko paas ek list hai jisme kuch values baar baar aa rahi hain.
#  Ek aisa code likho jisse aap ek nayi list banayein jisme iss list ki
#  items ek ek baar hi aaye. Jaise:
 
string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"] 



i=0
k=[]
while i<len(string_list):
        if string_list[i] not in k:
            k.append(string_list[i])
        i=i+1
print(k)






string_list = ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai'] 


i=0
b=[]
while i<len(string_list):
    if string_list[i] not in b:
        b.append (string_list[i])
    i=i+1
print(b)




# Iss nayi list mein sirf saare shehron ka naam sirf ek baar aa raha hai.
#  Yeh rahi aapki pehli items repeat hone waali list:
 
string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"] 


i=0
c=[]
while i<len(string_list):
    if string_list[i] not in c:
        c.append(string_list[i])
    i=i+1
print(c)