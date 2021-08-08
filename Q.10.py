# Question

# Socho aapke paas ek school ki class mein har student ke har subject ke marks hain. Jaise
 
# marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
 

# Yeh ek list mein andar aur lists hain.
#  Andar waali list mein har bache ke saare subjects mein marks hain.
#   Ek max_marks naam ka function banao jo ki ek aisi list le aur har 
#   students ke maximum marks print kare. Jaise agar main aapke max_marks 
#   function ko upar waali list ke saath call karunga ,


def max_function(marks):
    s=max(marks)
    print(s)
max_function([[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]] 
 )







big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]] 

# Iss list se agar humne saare numbers ko ek ek kar ke print karna hai toh hum kuch aisa code likh sakte hain:
 
big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
counter1 = 0
while counter1 < len(big_list):
    small_list_length = len(big_list[counter1])
    counter2 = 0
    while counter2 < small_list_length:
        print (big_list[counter1][counter2])
        counter2 = counter2 + 1
    counter1 = counter1 + 1
    print ('-----') 