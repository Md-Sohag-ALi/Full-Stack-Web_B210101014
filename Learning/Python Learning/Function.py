""" def addNum(a,b,c):
    return a*b*c
x = addNum(3,5,6)
print(x) """



def addNum(*arga,**argb):
    print(arga)
    print(argb)
x = addNum(a=5,b=6)

  