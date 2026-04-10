name = input("Enter your name :")
print(name)
age = input()
print(age)

'''Note :
input() result for input() is always str
'''

val = input() #if you  enter int output as a string
print(type(val))
# To solve this problem we can use type casting
#like int("2") 
val = int (input())
print(type(val))   #output :<class 'int'>

val = float (input())
print(type(val))   #output :<class 'float'>