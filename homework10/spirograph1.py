''' This program draws a spirograph
Created Spring 2018
lab05
@author: Nana Osei Asiedu Yirenkyi (na29) & Joshua maher(jdm47)
'''
#Gaining access to the math and turtle code.
import turtle
import math

print('This program draws a spirograh.\nA spirograph is a picture drawn by rolling a circle inside or outside of another circle.')

#Giving the name 'window' to the screen where the turtle will appear.
window = turtle.Screen()
        
#Naming the turtle 'AY'.
bob =turtle.Turtle()

while True:
    choice = input('\nWould you like to draw a spirograph? (Y or N):')
    if (choice == 'n') or (choice == 'N'):
        print('\nGoodbye')
        break
    
    while (choice == 'y') or (choice == 'Y'):
        try:
            #Prompting the user for the values of 'mov_rad', 'fix_rad', 'pen_offset' 
            mov_rad = float(input("\nEnter a moving radius:"))
            
            fix_rad = float(input("\nEnter a fixed radius:"))
            
            pen_offset = float(input("\nEnter the pen off set:"))
            
        except ValueError as excpt:
            print('\nINVALID VALUE. MUST BE A FLOAT. TRY AGAIN.')
            choice = input('\nWould you like to draw a spirograph? (Y or N):')
            break
            
    try:
        #Prompting the user for the value of pen color.
        color = input('\nEnter a color of your choice:')
        
    except ValueError as ecept:
        print('\nINVALID VALUE. ENTER A VALID COLOR')
        #Prompting the user for the value of pen color.
        color = input('\nEnter a color of your choice:')
        
            
            
    
        #Drawing the spirograph
        time = 0.0
        bob.penup()
        
        #Parametric equations used in drawing the spirograph
        x = (fix_rad + mov_rad)*math.cos(time) + pen_offset*math.cos(((fix_rad + mov_rad)*time) / mov_rad)
        
        y = (fix_rad + mov_rad)*math.sin(time) + pen_offset*math.sin(((fix_rad + mov_rad)*time) / mov_rad)
        
        #Repositioning the turtle and setting the color
        
        bob.goto(x,y)
        
        bob.pendown()
        
        bob.color(color)
        
        
    
        #Drawing the spirograph      
        while time < 100:
            time += 0.1
            
            x = (fix_rad + mov_rad)*math.cos(time) + pen_offset*math.cos(((fix_rad + mov_rad)*time) / mov_rad)
            
            y = (fix_rad + mov_rad)*math.sin(time) + pen_offset*math.sin(((fix_rad + mov_rad)*time) / mov_rad)
            
            bob.goto(x,y)
