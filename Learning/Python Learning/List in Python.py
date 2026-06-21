#list 
#A build in data type that store a set of data
#It can Store different type [int ,float,str,etc]
marks = [87,"sk",95,76,80,34] #access by marks[0],marks[1] ...
marks[0] = 90 #allowed in python but string not aloowed
print(marks) #output :[90, 67, 95, 76]
print((len(marks)))

#LIST SLICING
#SIMILAR TO STRING SLICING
#marks[1 : 4] is ["sk",95,76,80]
#marks[ : 4] is same as marks[0 : 4]
#marks[-3 : -1] is [76 ,80]
#marks[1 : ] is same as marks[1 : len(marks)]
print( marks[2 : 4] ) # output :[95, 76]
mark_slicing = marks[1 : 5]
print(mark_slicing) #Output :['sk', 95, 76, 80]
print (marks[-3 : -1] )

#List Method
#list = [2, 1, 3]
#append()->adds one element in the end
#sort()->sort in asending order
#sort(reverse = true) ->sort in descending osrder
#list.reverse() ->reverse list
#insert(idx ,element) ->insert element at index
#remove(1)->remove first occurence of element 1
#pop(idx) ->removes element at idx
list =[2, 1, 3]
list.append(1)
print(list)
list.sort()
print(list)
list.sort(reverse = True)
print(list)
list.reverse()
list.insert(2 ,50)
print(list)
list.remove(1)
print(list)
list.pop(1)
print(list)
list2 = list.copy()
print(list2)