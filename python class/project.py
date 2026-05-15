"""from tkinter import *
import tkinter as tk
root=Tk()
root.title("Form")
label = Label(root,text="School Admission form").grid(columnspan=2)
Label(root,text="Student Name").grid(row=5)
Label(root,text="Date of birth").grid(row=6)
Label(root,text="Genter").grid(row=7)
Label(root,text="Father Name").grid(row=8)
Label(root,text="Mother Name").grid(row=9)
Label(root,text="Email id").grid(row=10)
Label(root,text="Address").grid(row=11)
Label(root,text="Phone.No").grid(row=12)
Label(root,text="Parent.No").grid(row=13)
Label(root,text="School Location").grid(row=14)
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
e4=Entry(root)
e5=Entry(root)
e6=Entry(root)
e7=Entry(root)
e8=Entry(root)
e1.grid(row=5,column=1)                                   
e2.grid(row=6,column=1)
e3.grid(row=7,column=1)
e4.grid(row=8,column=1)
e5.grid(row=9,column=1)
e6.grid(row=10,column=1)
e7.grid(row=11,column=1)
e8.grid(row=12,column=1)
var1 = IntVar()
Checkbutton(root,text='Male',variable= var1).grid(row=7,column=1,sticky=W)
var2 = IntVar() 
Checkbutton(root,text='Female',variable= var2).grid(row=7,column=2,sticky=W)
v = IntVar()
Radiobutton(root,text="city",variable=v,value=1).grid(row=14,column=1,sticky=W)
Radiobutton(root,text="state",variable=v,value=2).grid(row=14,column=2,sticky=W)
mainloop()"""

import pygame
import random

pygame.init()

width = 800
height = 600

white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)

screen = pygame.display.set_mode ((width,height))
pygame.display.set_caption ("Snake Game")

x = 300
y = 200
move_x = 5
move_y = 5
food_block = 20 
snake_block = 30

food_x = random.randrange (0,width,10)
food_y = random.randrange (0,height,10)

snake_list = []
snake_length = 1

clock = pygame.time.Clock()

font=pygame.font.SysFont(None,35)
text=font.render ("score: "+str(10), True, white)
screen.blit(text,[10,10])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys [pygame.K_LEFT] and move_x >0:
        move_x = -snake_block
    elif keys [pygame.K_RIGHT] and move_x < width - snake_block:
        move_x = +snake_block
    elif keys [pygame.K_UP] and move_x > 0:
        move_y = -snake_block
    elif keys [pygame.K_DOWN] and move_x < width - snake_block:
        move_y = +snake_block

                        
    food_rect = pygame.Rect (food_x,food_y,food_block,food_block)
    snake_rect =pygame.Rect (move_x,move_y,snake_block,snake_block)

    if snake_rect.colliderect(food_rect):
        score += 1
        food_x = random.randint(0, width - food_block)

    pygame.draw.rect(screen, green, snake_rect)
    pygame.draw.rect(screen, red, food_rect)
    pygame.display.flip()
    clock.tick (10)
pygame.quit()
        


    

   





