""" filename = "input.txt"
#write in file
text = open(filename,"w")
text.write("I am a full stack web developper")

#open a file
text = open(filename ,"r")
content = text.read()
text.close()
print(content)

 """


#In modern 
""" filename = "input.txt"
with open(filename,"r") as file:
    content = file.read()
    print(content)

with open(filename,"a") as file:
    content = file.write(" and I am also want to be a Software Engineer") """
    

#Binary file
filename = "img.jpg"
with open(filename ,"rb") as file:
    content = file.read()
    print(content)


