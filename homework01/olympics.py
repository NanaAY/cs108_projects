''' A turtle graphics program that draws the olympics logo
Created Spring 2018
homework01
@author: Nana Osei Asiedu Yirenkyi (na29)
'''

# #Gain access to the "turtle" code
# import turtle
# 
# #Name the screen where the turtle will appear "window"
# window = turtle.Screen()
# 
# #Create turtle and name it AY
# AY = turtle.Turtle()
# 
# #Setting the pen size to 10
# AY.pensize(10)
# 
# #ALL CIRCLES HAVE A RADIUS OF 100 PIXELS
# 
# #Drawing the blue circle
# AY.pencolor('#0000FF') #sets the color of the pen to blue
# 
# AY.circle(100, 365,) 
# 
# 
# #Drawing the yellow circle
# AY.pencolor('#FFfF00')
# 
# AY.right(90)
# 
# AY.circle(100, 620)
# 
# AY.right(90)
# 
# AY.left(90)
#  
# 
# #Drawing the black Circle
# AY.pencolor('#000000')
#  
# AY.left(90)
#  
# AY.circle(100, 550)
#  
# 
# #Drawing the green circle  
# AY.pencolor('#00FF00')
#  
# AY.left(90)
#  
# AY.circle(100, 710)        
#  
#  
# #Drawing the red circle
# AY.pencolor('#FF0000')
#  
# AY.right(270)
#  
# AY.circle(100, 360)
# 
# 
# #keep the window open until it is clicked 
# window.exitonclick()


import turtle
import random


# xcor(), ycor(), heading(), setheading()
width = 400
height = 400

# Rename turtle and window
ball = turtle.Turtle()
window = turtle.Screen()

# Make the ball
ball.shape("circle")

# Window setup
window.setup(width=1000, height=1000, startx=0, starty=0)


random_x = random.randint(-3, 3)
random_y = random.randint(-3, 3)

x_vel = random_x
y_vel = random_y

x = 0
y = 0

while True:
    ball.goto(x, y)
    x += x_vel
    y += y_vel

    if y >= height or y <= -height:
        y_vel = -y_vel
    if x >= width or x <= -width:
        x_vel = -x_vel
