''' This program drives a ball shaped turtle around a canvas
Created Spring 2018
homework05
@author: Nana Osei Asiedu Yirenkyi (na29)
'''

# Gain access to turtle, math and random
import turtle
import random


# Give the name "window" to the screen where the turtle will appear
window = turtle.Screen()

window.setup(width=1000,height=1000)

width = 490
height = 490

# name turtle to bob and change its shape
bob = turtle.Turtle()

bob.shape('circle')

bob.setheading(random.randint(1,50))

x_vel = random.randint(4,6)

y_vel = random.randint(5,10)

x = 0
y = 0

while True:
    bob.goto(x, y)
    x += x_vel
    y += y_vel
    
    if y >= height or y <= -height:
        y_vel = -y_vel
    if x >= width or x <= -width:
        x_vel = -x_vel 
        
    
    
    