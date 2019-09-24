'''A Python turtle program that draws two circles and determines if they overlap
Created Spring 2018
Homework04
@author: Nana Osei Asiedu Yirenkyi (na29) '''


#Gain access to the "turtle" code
import turtle

window = turtle.Screen() #Name the screen where the turtle will appear "window"

bob = turtle.Turtle()  #Create turtle and name it bob



#Prompt user to enter center coordinates and radius of circle1
print('Circle 1')

x1 = float(input('\nEnter value for x1:'))

y1 = float(input('\nEnter value for y1:'))

radius1 = float(input('\nEnter value for radius of the first circle:'))


#Prompt user to enter center coordinates and radius of circle1
print('\nCircle 2')

x2 = float(input('\nEnter value for x2:'))

y2 = float(input('\nEnter value for y2:'))

radius2 = float(input('\nEnter value for radius of the second circle:'))

circle1 = (x1,y1)

circle2 = (x2,y2)



#Drawing the two circles with turtle
bob.penup()

bob.setpos(circle1)

bob.pendown()

bob.circle(radius1)

bob.penup()

bob.setpos(circle2)

bob.pendown()

bob.circle(radius2)



#Determining if the circles are disjointed or they overlap
dist_1 = abs(x1 - x2)

dist_2 = abs(y1 - y2)


if dist_1 >= radius1 and dist_2 >= radius1:
    bob.write("The circles are disjointed.", font=("Arial", 20, "italic"))
    
elif dist_1 < radius1 and dist_2 < radius1:
    bob.write("Circle 1 contains circle 2.", font=("Arial", 20, "italic"))

else:
    bob.write("The circles overlap.", font=("Arial", 20, "italic"))

    






window.exitonclick() #keep the window open until it is clicked 