def function(x,y):
    a=("x: ",x)
    b=("y: ",y)
    return a
    return b
def function(x,y=90):
    a=("x: ",x)
    b=("y: ",y)
    return (a,b)


def function(one,two):
    a=(one,two)
    return a

def function(one,two):
    a=(two,one)
    return a

def function(one,two):
    a=(one,two)
    return a

def function (name,age):
    a=('I am',name)
    b=('my age',age)
    return (a,b)

def nameage(name,age):
    print('I am',name)
    print('my age',age)
nameage(18,'Anu')

def function(x,y):
    return x+y
result=function(9,8)
result2=function(51,21)
print(result)
print(result2)

def function(x,y):
    return x-y
result=function (52,6)
result2=function (85,7)
print(result)
print(result2)

def function():
    return (20,40)
x,y=function()
print("x: ",x)
print("y: ",y)
x,*y=5,10,15
print(x,y)





