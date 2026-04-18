# Facebook (FB)

# Account → post, react, share, messaging
#        → stored in database, same as your data

# Client ↔ Server communication uses JSON (JavaScript Object Notation)
post = "Hello, this is my first post"
how_like_json = '{"user_id" : 123 , "post" : "Hello, this is my first post", "edit" : True}'
print(type(how_like_json))

import json
#python obj to  json ----> called serialization
data = {
    "user_id" : 123 , "post" : "Hello, this is my first post", "edit" : True
}
print(type(data))
json_str = json.dumps(data , indent = 4)
print(json_str , type(json_str))


#json string to python object ---->called deserilization
json_string = '{"user_id" : 123 , "post" : "Hello, this is my first post", "edit" : true}'
python_obj = json.loads(json_string)
print(python_obj)

#Crud Operation
#C-Create ->post req
#R-Repeat ->get req
#U-Update ->put/patch req
#D-Delete ->delete req

import requests
#Get Requests
""" res = requests.get("https://jsonplaceholder.typicode.com/posts")
if res.status_code == 200:
    print("Successful Request" , res.json())
else:
    print("Failed to get Data") """

#Post Request
value =  {
    "userId": 1,
    "id": 101,
    "title": "test",
    "body": "test body"
  }
res = requests.post("https://jsonplaceholder.typicode.com/posts", value)
if res.status_code == 201:
    print("Successful Request" , res.json())
else:
    print("Failed to get Data")

#Update Request
#fb profile er -> image change korte chan -> Patch request
#fb er post -> Caption ,image,date -> Put Request


#Patch request
value =  {
    
    "title": "test",
    
  }
res = requests.patch("https://jsonplaceholder.typicode.com/posts/1" , value)
if res.status_code == 200:
    print("Successful Request" , res.json())
else:
    print("Failed to get Data")

#Put Request
value =  {
    "userId": 1,
    "id": 101,
    "title": "test",
    "body": "test body"
  }
res = requests.put("https://jsonplaceholder.typicode.com/posts/1" , value)
if res.status_code == 200:
    print("Successful Request" , res.json())
else:
    print("Failed to get Data")

#Delete
res = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
if res.status_code == 200:
    print("Successful Request" , res.json())
else:
    print("Failed to get Data")
