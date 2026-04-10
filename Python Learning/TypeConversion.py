# Tyupe conversion become two type

'''
1. type conversion-> python do automatically
2.Type casting -> We can do it manually
'''

a = 2
b = 2.45
sum = a + b  # 2.0 + 2.45
print(sum)
r ="2"
z = 2.8
# s = r + z error can only concatenate str (not "int") to str
#Manually Typcast
s  = float(r) + z 
print(s)

c = 34.4
c =  str(c) #typecasting
print(type(c))