try:
    with open("input.txt","r") as file :
        content = file.read()
        """ Rahim = Karim """
        """ Rahim = int("string") """
        a = [1,2,3,4,5]
        """ print(a[5]) #index out of range  """
        #x = 10/0
except ZeroDivisionError:
    print("Division by zero Error")

except IndexError:
    print("Invalid Index")        
except FileNotFoundError :
    print("File Not Fopund")
except ValueError:
    print("Value Error")
         
except Exception as e:
    print("Some error occured !!",e)        


def check_file(filename):
    if not filename.endswith('.txt'):
        raise ValueError("Only .txt files are allowed !!")
    print("Valid File")
try:    
    check_file("hello.jpg") 
 
except Exception as e:
    print(e)
else:
    print("Vhai tumi sera !! tomar code a kono vul nai") 
finally:
    print("Ami print hoboi")       

