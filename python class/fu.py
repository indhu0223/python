'''def function(*args):
    print("Pen:",args)
function('blue','red','block')

def function(pen):
    print("pen:",pen)
function('blue')
def function(**kwargs):
    print("keyword arguments:",kwargs)
function(age=15,city='olso')

def function(title,*args,**kwargs):
    print("Title:",title)
    print("positional arguments:",args)
    print("keyward arguments:",kwargs)
function("school","note","pen",number=10,name='anu')

def function(*args):
    print("non-keyward arguments (*args):")
    for arg in args:
        print(arg)
function('word','hello')
def function(x,y,z):
    return x-y-z
number=[85,41,34]
result=function(*number)
print(result)
        
def function(a,b,c):
    return a+b+c
number=[96,58,43]
result=function(*number)
print(result)

def function(fname,lname):
    print("Hello",fname,lname)
person={'fname':'emil','lname':'refsnes'}
function(**person)

def function(note,**kwargs):
    print("Note:",note)
    print("keyward arguments:",kwargs)
function('king size', pen='blue',num=12)

def function(**kwargs):
    print("keyward argument:",kwargs)
    for kwarg in kwargs:
        print(kwarg)
function(num=458,look='good')

def function(book):
    print("Book:",book)       
    for books in book:
        print(books)
function('maths')

def function(x,*y):
    print("x:",x)
    print("y:",y)
function(45,58,85)

def function(x,y):
    return x+y
number=[47,54]
result=function(*number)
print(result)

def function(x,y):
    print("x:",x)
    print("y:",y)
function(9,8)

def function(**kwargs):
    print("num:",kwargs)
function(num=12,age=12)
def function(*args):
    print("arguments:",args)
function('age','name','class')

def function():
    a=20
    return a
print(function())

def function():
    a=2
    b=3
    if a<=b:
        print('a is less than b')
    else:
        print('a is grater than b')
function()

def function(a,b):
    return a+b
number=[41,51]
result=function(*number)
print(result)

def function(*args):
    for arg in args:
        print(arg)
function('num','jkl')
def function(*args):
    return args
word=('ghj','guj')
result=function(*word)
print(result)

def function(*args):
    for arg in args:
        return args
word=('uyt','rty')
result=function(*word)
print(result)

def function(pen):
    for pens in pen:
        return pen
write=('blue')
result=function(write)
print(result)

def result (n):
    if n>0:
        print("positive number")
    elif n<0:
        print("negative number")
    else:
        print("zero")
result(5)
              
def result (a,b):
    if a<b:
        return("a is less than b")
    else :
        return("a is grater than b")
result=result(10,20)
print(result)

def result(mark):
    if mark>=35:
        return "pass"
    else:
        return "fail"
result = result(52)
print(result)

def result (n):
    if n%2==0:
        return "even number"
    else:
        return "odd number"
result =result(52)
print(result)

def cube (x):
    return x*x*x
print(cube(3))

cube_1=lambda x:x**3
print(cube_1(2))

cube_2=lambda x:x*5
print(cube_2(5))

cube_3=lambda x:x-45
print(cube_3(87))

cube_4=lambda x:x+73
print(cube_4(43))

x=lambda a,b:a*b
print(x(5,5))

x=lambda c,d:c**d
print(x(2,3))

x=lambda x,y:x-y
print(x(8,4))

x=lambda x,y:x+y
print (x(56,14))

numbers=[1,2,3,4,5]
doubled=list(map(lambda x:x*2,numbers))
print(doubled)

number=[2,4,6,8,10]
doubled=list(map(lambda x:x**2,number))
print(doubled)

def square(x):
    return x*x
sq=list(map(square,number))
print (sq)

def square(x):
    return x*x
sq=list(map(square,number))
print(sq)

number=[1,2,3,4,5,6]
oddnumber =list(filter(lambda x:x%2!=0, number))
print(oddnumber)

numbers=[1,2,3,4,5,6,7,8,9,10]
even_number = list(filter(lambda x:x%2==0, numbers))
print(even_number)

numbers=[1,2,3,4,5,6,7,8,9,10]
even_number = list(map(lambda x:x%2==0, numbers))
print(even_number)'''


"""a=5
while (a>0):
    print (a)
    a-=1
def rev (a):
    c=0
    while (a>0):
        r=a%10
        c=(a*10)+r
        a//=10
        return (c)
"""

def rev (a):
    c=0
    while (a>0):
        r=a%10
        c=(a*10)+r
        a//=10
        return (c)

    


    

    
                                                 

     


          
