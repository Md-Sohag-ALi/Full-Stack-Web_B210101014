str1 = "This is"
str2 = 'ApnaCollage'
str3 = """this is a string"""
print (str1)
print (str2)
print(str3)
# causes of different different qutes
# "this is apnacollage's toutorial" ->in this case need " " or """ """ qutes to remove ambiguite
# for this string  Apanacollage"s need ' ' or """ """ qoute

#FOr new line  
str4 = "This is my work.\n for learning"
print(str4)
#Concatenation
str5 = str1 + " " + str2
print(str5)
print(len(str1))
#Indexing
str = "apna collage"
print(str[5])
# str[4] = 'x' #assinged is not possible in python

#SLICING :
#Accessing parts of a string
# str[strting_idx : ending_idx]       ending index is not included
str6 =   "apna_colla"
#indexing:0123456789

str7 = str6[ : 7] #means na_co     
# str[2 : ] means 2 to last -> na_colla
# str[ : 4] means 0 to 4 -> apna_
print(str7) #output :na_co

#SLICING for Negetive index
str8 = "APPLE" # A P P L E
# indexing     #-5-4-3-2-1 
str9 = str8[-3 : -1] #in this case PL will print last index skip
print(str9)


#STRING FUNCTOION 
 #endswith()  ->returns true if ends with substr
str10 = "i am a begginer in competitive programming"
print (  str10.endswith("ing")  ) #the string ends with ing so return true

#capitalize() ->capitalize the 1st ch of string
print(  str10.capitalize()  ) #output :I am a begginer in competitive programming note:Not change in main string
print(str10)
str10 = str10.capitalize() #change main string
print(str10)
 
 
 #replace(old , new)
str11 = "I am studying python from Apnacollage"
str11 = str11.replace("python" , "javascript")
print(str11)
#find() return 1st occurance index
str12 = "we are muslim"
print( str12.find("a")) # print 3

str13 = "Hi , manager ,Shohanur himel"
print(str13.count("m")) # print 2