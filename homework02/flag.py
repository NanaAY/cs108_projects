''''A turtle graphics program that draws the Japenese Flag & Ghanaian Flag
 according to the construction sheet
Created Spring 2018
homework02
@author: Nana Osei Asiedu Yirenkyi (na29)'''



#SCALE
UNIT = 300



#Gain access to the "turtle" code
import turtle



#Name the screen where the turtle will appear "window"
window = turtle.Screen()



#Create turtle and name it AY
AY = turtle.Turtle()



#~~~~~DRAWING THE RECTANGLE OF THE FLAG~~~~~~~~~
AY.fd(UNIT)
AY.rt(90)
AY.fd( (UNIT*2) / 3) #vertical side should be two thirds of the horizontal side
AY.rt(90)
AY.fd(UNIT)
AY.rt(90)
AY.fd( (UNIT*2) / 3)



#~~~~~DRAWING THE RED CIRCLE OF THE FLAG~~~~~~~~~
AY.penup()
AY.rt(90)
AY.fd(UNIT/2)
AY.rt(90)
AY.fd( (UNIT*2) / 15)
AY.rt(90)
AY.pendown()
AY.begin_fill()
AY.color('red')
AY.circle((UNIT*6) / 30)
AY.end_fill()
#AY.hideturtle()



#keep the window open until it is clicked 
window.exitonclick()


