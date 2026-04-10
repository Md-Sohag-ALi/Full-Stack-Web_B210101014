#Tuple
#immutable->assinged not allowed
#single element tuple tup = (1 ,) otherwise take as integer
tup = (2 , 1, 3, 2)
print(tup)

#Slicing also possible in tuple

#TUPLE METHOD
#index(elem)->return index of element
#count(el)->count no of el in tuple
print(tup.index(3))
print(tup.count(2))
