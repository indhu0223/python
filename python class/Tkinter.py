"""import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("sample")
 
widgets are added here

root.mainloop()"""

"""from tkinter import *
root=Tk()
root.title("My First GUI")
label=Label(root,text="Hello Hii")
label.pack()
root.mainloop()

import tkinter as tk
r=tk.Tk()
r.title("Counting Seconds")
button=tk.Button(r,text="Stop" , width=25, command=r.destroy)
button.pack()
mainloop()"""


"""from tkinter import *
root=Tk()
root.title("My First GUI")
label=Label(root,text="Hello World")
label.pack()
root.mainloop()


import tkinter as tk
r=tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r,text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()"""

"""from tkinter import *
master=Tk()
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
mainloop()"""


"""from tkinter import *
root=Tk()
T=Text(root,height=2, width=30)
T.pack()
T.insert(END,'HI\nBEST WEBSITE\n')
mainloop()"""

"""from tkinter import *
root=Tk()
T=Text(root,height=4, width=30)
T.pack()
T.insert(END,'HI\nBEST\nIN\nMAYILADUTHURAI\n')
mainloop()"""

"""from tkinter import *
root =Tk()
v=IntVar()
Radiobutton(root, text='Yes', variable=v,value=1).pack(anchor=W)
Radiobutton(root, text='No',variable=v,value=2).pack(anchor=W)
mainloop()"""

"""from tkinter import *
master=Tk()
var1=IntVar()
Checkbutton(master, text='Male',variable=var1).grid(row=0,sticky=W)
var2=IntVar()
Checkbutton(master, text='Female',variable=var2).grid(row=1,sticky=W)
mainloop()"""

"""import tkinter as tk
root=tk.Tk()
root.title("Pack Example")
button1 = tk.Button(root, text="Button1")
button2 = tk.Button(root, text="Button2")
button3 = tk.Button(root, text="Button3")
button1.pack()
button2.pack()
button3.pack()
root.mainloop()"""

"""import tkinter as tk
root=tk.Tk()
root.title("Grid Example")
label1 = tk.Label(root,text="Label1")
label2 = tk.Label(root,text="Label2")
label3 = tk.Label(root,text="Label3")
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=1,column=0,columnspan=2)
root.mainloop()"""

"""import tkinter as tk
root=tk.Tk()
root.title("Grid Example")
label1 = tk.Label(root,text="Label1")
label2 = tk.Label(root,text="Label2")
label3 = tk.Label(root,text="Label3")
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=1,column=0,rowspan=2)
root.mainloop()"""

"""from tkinter import *
root=Tk()
ourMessage='My Message'
messagevar=Message(root,text=ourMessage)
messagevar.config(bg='pink')
messagevar.pack()
root.mainloop()"""

"""import tkinter as tk 
root = tk.Tk()
root.title("place Example")
label=tk.Label(root,text="Label")
label.place(x=500,y=110)
label.pack()
root.mainloop()"""


"""import tkinter as tk
from tkinter import ttk
def select(event):
    selected_item=combo_box.get()
    label.config="selected Item: " + selected_item
root=tk.Tk()
root.title("Combobox Example")
label=tk.Label(root,text="Selected Item")
label.pack()
combo_box = ttk.Combobox(root,values=["Tamil","English","Maths"], state= 'readonly')
combo_box.pack()
combo_box.set("Language")
combo_box.bind("<<combobox selected>>", select)
root.mainloop()"""


"""from tkinter import *
root = Tk()
Lb=Listbox(root)
Lb.insert(1, 'A')
Lb.insert(2,'A1')
Lb.insert(3,'b')
Lb.insert(4,'C')
Lb.insert(5,'C1')
Lb.insert(6,'Any Other')
Lb.grid()
root.mainloop()"""

"""from tkinter import *
root=Tk()
ourMessage = "Hello"
messagevar = Message(root, text=ourMessage)
messagevar.config(bg='green')
messagevar.pack()
root.mainloop()"""

"""import tkinter as tk
root = tk.Tk()
root.title("place Example")
label=tk.Label(root,text="Label")
label.place(x=500,y=456)
label.pack()
root.mainloop()"""

"""import tkinter as tk
from tkinter import ttk
def select(event):
    selected_item=combo_box.get()
    label.config="selected Item: " + selected_item
root = tk.Tk()
#root.title = ("Combobox Example")
label=tk.Label(root, text="Selected item")
label.grid()
combo_box = ttk.Combobox(root, values=["BSc","BBA","BCom"],state= 'readonly')
combo_box.grid()
combo_box.set("crouse")
#combo_box.bind("<<combobox selected>>",select)
root.mainloop()"""


"""from tkinter import *
import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.title ("Form")
label=Label(root, text="Register Form").grid(columnspan=2)
Label(root,text='First Name').grid(row=5)
Label(root,text='Last Name').grid(row=6)
Label(root,text='Email').grid(row=7)
Label(root,text='User Name').grid(row=8)
Label(root,text='password').grid(row=9)
Label(root,text='Address').grid(row=10)
Label(root,text='Phone No').grid(row=11)
Label(root,text='Gender').grid(row=12)
Label(root,text='Crouse Completed').grid(row=13)
label=tk.Label(root, text="Selected crouse").grid(row=14)
label=tk.Label(root,text="crouse Name").grid(row=15)
button = tk.Button(root,text='Stop', width=25, command=root.destroy).grid(row=16,column=1)
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
e4=Entry(root)
e5=Entry(root)
e6=Entry(root)
e7=Entry(root)
e1.grid(row=5,column=1)
e2.grid(row=6,column=1)
e3.grid(row=7,column=1)
e4.grid(row=8,column=1)
e5.grid(row=9,column=1)
e6.grid(row=10,column=1)
e7.grid(row=11,column=1)
var1=IntVar()
Checkbutton(root,text='Male',variable=var1).grid(row=12,column=1,sticky=W)
var2=IntVar()
Checkbutton(root,text='Female',variable=var2).grid(row=12,column=2,sticky=W)
v=IntVar()
Radiobutton(root,text='yes',variable=v,value=1).grid(row=13,column=1,sticky=W)
Radiobutton(root,text='No',variable=v,value=2).grid(row=13,column=2,sticky=W)
combo_box = ttk.Combobox(root, values=["BSc","BBA","BCom"],state= 'readonly').grid(row=14,column=1,sticky=W)
combo_box = ttk.Combobox(root, values=["Tamil","English","Maths"], state= 'readonly').grid(row=15,column=1,sticky=W)
mainloop()"""


"""from tkinter import *
root=Tk()
Label(root,text='First Name').grid(row=0)
Label(root,text='Last Name').grid(row=1)
Label(root,text='Father Name').grid(row=2)
Label(root,text='Address').grid(row=3)
Label(root,text='Email').grid(row=4)  
Label(root,text='Phone No').grid(row=5) 
Label(root,text='Gender').grid(row=6)
Label(root,text='10th pass').grid(row=7)
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
e4=Entry(root)
e5=Entry(root)
e6=Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)
e5.grid(row=4,column=1)
e6.grid(row=5,column=1)
var1=IntVar()
Checkbutton(root,text='Male',variable=var1).grid(row=6,column=1,sticky=W)
var2=IntVar()
Checkbutton(root,text='Female',variable=var2).grid(row=6,column=2,sticky=W)
v=IntVar()
Radiobutton(root,text='yes',variable=v,value=1).grid(row=7,column=1,sticky=W)
Radiobutton(root,text='No',variable=v,value=2).grid(row=7,column=2,sticky=W)
mainloop()"""

"""from tkinter import *
root = Tk()
def b1():
    result.insert(0,1)
def p():
    t=result.get()+"+"
    # print(t)
    result.config(Text=t)
result = Entry(root)
result.grid(row=0,columnspan=4)
button1 = Button(root, text=1, width=10, command=b1)
button1.grid(row=1,column=0)
button2 = Button(root, text=2, width=10, command=root.destroy)
button2.grid(row=1,column=1)
button3 = Button(root, text=3, width=10, command=root.destroy)
button3.grid(row=1,column=2)
buttonp = Button(root, text='+', width=10, command=p)
buttonp.grid(row=1,column=3)
button4 = Button(root, text=4, width=10, command=root.destroy)
button4.grid(row=2,column=0)
button5 = Button(root, text=5, width=10, command=root.destroy)
button5.grid(row=2,column=1)
button6 = Button(root, text=6, width=10, command=root.destroy)
button6.grid(row=2,column=2)
buttons = Button(root, text='-',width=10, command=root.destroy)
buttons.grid(row=2,column=3)
button7 = Button(root, text=7, width=10, command=root.destroy)
button7.grid(row=3,column=0)
button8 = Button(root, text=8, width=10, command=root.destroy).grid(row=3,column=1)
button9 = Button(root, text=9, width=10, command=root.destroy).grid(row=3,column=2)
buttonm = Button(root, text='*',width=10, command=root.destroy).grid(row=3,column=3)
buttonh = Button(root, text='#',width=10, command=root.destroy).grid(row=4,column=0)
button0 = Button(root, text=0, width=10, command=root.destroy).grid(row=4,column=1)
buttond = Button(root, text='/', width=10, command=root.destroy).grid(row=4,column=2)
buttone = Button(root, text='=',width=10, command=root.destroy).grid(row=4,column=3)
mainloop()"""

"""import tkinter as tk 
def click(value):
    current = entry.get()
    entry.delete (0,tk.END)
    entry.insert(0,str(current)+str(value)) 
def clear():
    entry.delete(0,tk.END)
def calculate():
    try:
        result = eval (entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")

root = tk.Tk()
root.title("simple calculator")
root.geometry("180x180")

entry=tk.Entry(root,justify="right")
entry.pack(pady=10)

frame=tk.Frame(root)
frame.pack()

buttons=[
    ('1','2','3','+'),
    ('4','5','6','-'),
    ('7','8','9','*'),
    ('.','0','=','/')
]

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand = True, fill="both")
    for btn in row:
        if btn == "=":
            button = tk.Button (row_frame, text=btn, 
                                command=calculate)
        else:button = tk.Button (row_frame, text=btn,
                                  command=lambda b=btn: click(b))
        button.pack(side="left")

clear_btn = tk.Button (root, text="clear", command=clear)
clear_btn.pack(padx=20,pady=10)

root.mainloop()"""

"""import random
words = ["python", "developer","coding","challenge"]
word = random.choice(words)
guessed = ["_" for _ in word]
attempts = 6

while attempts > 0 and "_" in guessed:
    print("word: ", " ". join (guessed))
    guess = input ("Guess a letter: ")
    if guess in word:
        for i in range (len(word)):
            if word [i] == guess:
                guessed [i] =guess
    else:
        attempts -=1
        print(f"Incorrect ! {attempts} attempts left.")
    if "_" not in guessed:
        print("Congrats ! you found the word: ", word)
    else:
        print("Game over! The word was: ",word)"""

questions = {
    "What is the capital of france ?": "Paris",
    "What planet is known as the Red planet ?": "Mars",
    "What is 5+6 ?":"11"
}
score = 0
for question, answer in questions. items():
    user_answer = input (question +" ").strip(). capitalize()
    if user_answer == answer:
        print("correct!")
        score +=1
    else:
        print(f"worng the correct answer is {answer}.")
    print(f"find score:{score}/{len(questions)}")

questions={
    "What is 73-21 ?": "52"
    "What is 5+9 ?": "14"
}
score = 0
for question, answer in questions. items():
    user_anser = input (question +" ").strip().capitalize()
    if user_answer == answer:
        print("correct!")
        score +=1
    else:
        print(f"Worng the correct answer is {answer}.")
    print(f"find score:{score}/{len(questions)}")
