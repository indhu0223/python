from turtle import *
'''forward (100)
left (120)
forward (100)
right (60)
backward (90)

color ('blue')
width (3)
forward (100)
left (120)
forward (100)
print (pos())
home()
done()

forward (200)
left (60)
forward (100)
print (pos())
home()


forward (50)
left (60)
forward (100)
right (40)
print (pos())
home()

color ('red')
width (4)
forward (200)
left (120)
forward (200)
right (120)
backward(200)
home()

color ('green')
width (2)
forward (100)
left (90)
forward (100)
right (90)
backward(100)
home()

color ('red')
fillcolor ('black')
begin_fill()
for i in range (4):
    forward (100)
    right (90)
end_fill ()
forward (200)
done()

hideturtle()
forward (100)
right(85)
showturtle()
forward (96)
clear()
forward(100)
done()

shape ("turtle")
forward (200)
done()

forward (85)
left(30)
forward(90)
reset()
forward(50)
done()

for i in range(4):
    forward (100)
    right (90)
    clearscreen()

circle(50)
clearscreen()

right(74)
forward(100)
for i in range (4):
    right(144)
    forward(100)

side = 6
for i in range (6):
    forward (80)
    right (360/6)
clearscreen()  

color('blue')
fillcolor('pink')
begin_fill()
for i in range (2):
    forward (130)
    right(60)
    forward (50)
    right(120)
end_fill()
done()

color ('black')
width(3)
fillcolor('green')
begin_fill()
side = 6
for i in range (6):
    forward (80)
    right (360/6)
end_fill()


color ('black')
width(2)
fillcolor('pink')
begin_fill()
right(74)
forward(100)
for i in range (4):
    right(144)
    forward(100)
end_fill()


color ('black')
width(3)
fillcolor('red')
begin_fill()
circle(120)
end_fill()


color('black')
width(2)
fillcolor('black')
begin_fill()
for i in range(4):
    forward (100)
    right (90)
end_fill()



color('black')
width(2)
fillcolor(' green')
begin_fill()
circle(60)
end_fill()
done()

color('pink')
width(2)
fillcolor('black')
begin_fill()
for i in range (4):
    forward(100)
    right(90)
end_fill()'''


'''import turtle
wn=turtle.Screen()
wn.bgcolor("pink")
skk=turtle.Turtle()
skk.color("black")
def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size = size+5

sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(126)
sqrfunc(146)

import turtle
loadwindow = turtle.Screen()
turtle.speed(0)
for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
turtle.exitonclick()

import turtle
colors=['red','purple','blue','green','orange','yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range (360):
     t.speed(0)
     t.pencolor(colors[x%6])
     t.width(x//100+1)
     t.forward(x)
     t.left(59)'''

'''from turtle import *
color('red')
fillcolor('yellow')
begin_fill()
while True:
    speed(0)
    forward(200)
    left(155)
    if abs (pos())<1:
        break
end_fill()
#clearscreen()
exitonclick()

import turtle
screen=turtle.Screen()
screen.title("click the screen!")

my_turtle=turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")
my_turtle.penup()

def move_to_click(x,y):
    my_turtle.goto(x,y)
    print(f"Turtle moved to : ({x},{y})")

screen.onclick(move_to_click)
screen.mainloop()'''
'''
color('blue')
width(2)
fillcolor('red')
begin_fill()
for i in range(5):
    forward(100)
    right(70)
end_fill()
home()

color('green')
width(1)
fillcolor('pink')
begin_fill()
for i in range(6):
    forward(50)
    left(60)
end_fill()

color('blue')
fillcolor('pink')
begin_fill()
for i in range (2):
    forward (100)
    right(60)
    forward (100)
    right(120)
end_fill()
done()

color('black')
fillcolor('green')
begin_fill()
for i in range(2):
    forward(200)
    left(120)
    forward(100)
    left(60)
end_fill()
done()

color('black')
width(3)
fillcolor('green')
begin_fill()
circle(60)
end_fill()

color('blue')
width(2)
fillcolor('blue')
begin_fill()
for i in range(4):
    forward(80)
    right(90)
end_fill()
down()

color('blue')
fillcolor('black')
begin_fill()
while True:
    speed(0)
    forward(300)
    left(146)
    if abs(pos())<1:
        break
end_fill()

color('blue')
fillcolor('pink')
begin_fill()
for i in range(8):
    forward(200)
    right(156)
end_fill()
home()
done()'''

"""color('red')
forward(100)
back(50)
right(90)
forward(100)
right(90)
forward(50)
back(50)
right(180)
forward(50)
down()

color('pink')
right(90)
forward(100)
back(100)
left(45)
forward(130)
left(130)
forward(100)
down()

color('pink')
right(90)
forward(100)
back(50)
left(90)
forward(100)
right(90)
forward(55)
back(110)

color('pink')
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(50)

color('pink')
right(120)
forward(100)
back(120)
left(60)
forward(120)
back(60)
right(120)
forward(60)"""


"""import turtle
wn=turtle.Screen()
wn.bgcolor("light blue")
skk=turtle.Turtle()
skk.color("black")
def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size=size+5
sqrfunc(6)
sqrfunc(16)
sqrfunc(26)
sqrfunc(36)
sqrfunc(46)
sqrfunc(66)
sqrfunc(76)
sqrfunc(86)
sqrfunc(96)
sqrfunc(126)
sqrfunc(166)"""

"""import turtle
wn=turtle.Screen()
wn.bgcolor("pink")
skk=turtle.Turtle()
skk.color("black")
def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size = size+5

sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(126)
sqrfunc(146)"""

import turtle
loadwindow=turtle.Screen()
turtle.speed(0)
for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
turtle.exitonclick()

color('red')
right