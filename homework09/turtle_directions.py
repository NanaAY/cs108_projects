'''A python program that prompts the user for a file name containing directions for a turtle,
 and then uses turtle graphics to execute the directions.
Created Spring 2018
homework09
@author: Nana Osei Asiedu Yirenkyi (na29) '''


import turtle #gains access to the turtle code


bob = turtle.Turtle() #names the turtle bob

window = turtle.Screen() #Name the screen where the turtle will appear "window"

instruction_file = input("Enter the name of the instruction file: ") #Prompts the user for the name of the instruction file


with open(instruction_file) as file:
    line = file.readline()
    
    while line != '':
        
        if "pendown" in line:
            bob.pendown()
            
        if "penup" in line:
            bob.penup()
            
        if "color" in line:
            strip_spaces = str.strip(line)  # Gets rid of spaces in the beginning and end
            values = strip_spaces.split(' ')  # Splits the color from the 'color'
            color = values[1]
            bob.color(color)  # Sets color to the first index on list
            bob.goto(50, 50)  # Runs the turtle
            
        if "goto" in line:
            strip_spaces = str.strip(line)  # Gets rid of spaces in the beginning and end
            values = strip_spaces.split(' ')  
            x = int(values[1])
            y = int(values[2])
            bob.goto(x, y)  # goes to the specified points
            
        if "point" in line:
            strip_spaces = str.strip(line)  # Gets rid of spaces in the beginning and end
            values = strip_spaces.split(' ')  
            size = int(values[1])  # Sets size to the first index on list
            bob.dot(size)  # goes to the specified points
            
        if line.startswith("#"):
            strip_spaces = str.strip(line)  # Gets rid of spaces in the beginning and end
            print(line[0], line[2:])  # goes to the specified points
            
        line = file.readline()  # reads the next line
        
window.exitonclick() #exits program upon click
