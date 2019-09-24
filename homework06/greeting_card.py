''' A program uses functions to draw a greeting card, such as a Get-well Card, a Mother's Day card, etc. 
Created Spring 2018
Homework 06
@author: Nana Osei Asiedu (na29)'''

import turtle
import math

window = turtle.Screen()

bob = turtle.Turtle()


def card_outline():
    '''This function draws the square outline of the card'''
    
    #repositioning the turtle
    bob.penup()
    bob.goto(0,0)
    bob.bk(300)
    bob.left(90)
    bob.fd(300)
    bob.rt(90)
    bob.pendown()
   
    #drawing the square
    bob.fd(600)
    bob.rt(90)
    bob.fd(600)
    bob.rt(90)
    bob.fd(600)
    bob.rt(90)
    bob.fd(600)
    

def border_triangles():
    '''This function draws triangles around the border of the card'''
    bob.right(135)
    
    def draw():
        '''this function contains code on how the triangles should be drawn'''
        i=0
        while i < 5:
            bob.color('maroon')
            bob.begin_fill()
            bob.fd(60*math.sqrt(2))
            bob.lt(90)
            bob.fd(60*math.sqrt(2))
            bob.rt(90)
            bob.end_fill()
            i += 1
    
    def reposition():
        '''this function repositions the turtle'''
        bob.penup()
        bob.rt(90)
    #     bob.fd(60*math.sqrt(2))
    #     bob.lt(90)
        bob.pendown()
    
    #drawing across the top border
    draw()
    #repositioning the turtle
    reposition()
    #drawing across the right border
    draw()
    #repositioning the turtle
    reposition()
    #drawing across the bottom border
    draw()
    #repositioning the turtle
    reposition()
    #drawing across the left border
    draw()


def message():
    '''This function prints the message of the card'''
    bob.penup()
    bob.goto(0,-170)
    bob.color('gold')
    bob.write(" HAPPY BIRTHDAY!!!\n Wishing you all the best\n for today and in the future.", align='center', font=("Zapfino", 30, "italic"))
    
    







#calls to the functions defined above
card_outline()
border_triangles()
message()







window.exitonclick()