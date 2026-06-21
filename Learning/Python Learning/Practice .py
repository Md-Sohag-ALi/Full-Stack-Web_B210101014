movies = []
print("Enter 1st movie :")
mov1 = input()
movies.append(mov1)

print("Enter 2nd movie :")
mov2 = input()
movies.append(mov2)

print("Enter 3rd movie :")
mov3 = input()
movies.append(mov3)
print(movies)
#Check palindrome

list = [1, 2, 1]
list2 = [1 , 2, 3]
list_co = list.copy()
list_co.reverse()
if(list_co == list):
   print("Palindrome")
else:
    print("Not palindrome")

list2_co = list2.copy()
list2_co.reverse()
if(list2_co == list2):
    print("Palindrome")
else:
    print("Not Palindrome")
    
#Tuple practice
tup = ["A", "B","A+","F","A+","A+","A-"]
a = tup.count("A+")
print(a)
