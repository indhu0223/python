def function(x,y):
    print("x: ",x)
    print("y: ",y)
function(30,80)
    
def function(x,y=90):
    print("x: ",x)
    print("y: ",y)
function(80,9)

def function(one,two):
    print(one,two)
function(one='first',two='second')

def function(one,two):
    print(one,two)
function(two='first',one='second')

def function(one,two):
    print(two,one)
function('first','second')

def function(one,two):
    print(one,two)
function('first','second')

def nameage(name,age):
    print('I am',name)
    print('my age',age)
nameage('anu',18)

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

'''def function(title,*args,**kwargs):
    print("Title:",title)
    print("positional argument:",*args)
    print("keyward argument:",**kwargs)
function("letter","pen","note", age=16,name="anu")'''
    
def function(**kwargs):
    print("keyward arguments:" , **kwargs)
function(age=16,city="sdf")







