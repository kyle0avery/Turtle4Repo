#Turtle Goes To Beach - Notes

import turtle  
import time
import random

'''
Turtle Leaves House  *input - ask what turtle will collect at the beach, shells, trash, or fish
Turtle Drives to beach  *nested  loop - dodge obstacle in  traffic
Turtle picks up trash *  for count (range=trash items) Loop -> until trash collected 
Turtle returns home * 



functions = 5/3
main funct to call - duh
list - present as options for activity at beach
single loop - picking up trash

Note: I seriously DO NOT like group projects. I greatly apologize. -VA
'''

def drawSquare(x,y,width,height,thick,linecolor,fillcolor): #Creating a function with lots of variables to make drawing shapes much easier
    turtle.penup() #Begin prep for Square
    turtle.setheading(0) #Reset angle for shape
    turtle.goto(x,y) #Move turtle to desired position
    turtle.backward(width/2) #Move backward half width to center object
    turtle.pensize(thick) #Set pen size to desired size
    turtle.pencolor(linecolor) #Set colors
    turtle.fillcolor(fillcolor)
    turtle.begin_fill() #Starting fill
    turtle.pendown()
    for i in range(2): #Actual drawing starts here, repeats twice to create square/rectangle
        turtle.forward(width) #Draw sqaure width
        turtle.left(90)
        turtle.forward(height) #Draw shape height
        turtle.left(90)
    turtle.end_fill() #Finish

#turtle.write("The End", align="center")
    
def drawTriangle(x,y,length,thick,linecolor,fillcolor):
    turtle.penup() 
    turtle.setheading(0) 
    turtle.goto(x,y)
    turtle.backward(length/2)
    turtle.pensize(thick)
    turtle.pencolor(linecolor)
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    turtle.pendown()
    for i in range(3):
        turtle.forward(length)
        turtle.left(120) #Making the angle always 120 degrees. Will always result in Equilateral Triangle
    turtle.end_fill()
    

def drawCloud(dotC): #Routine for drawing Clouds
    for i in range(dotC):
        turtle.dot(random.randint(30,80),"White")
        turtle.fd(random.randint(10,30))
        
turtle.speed(0)

#Draw Scenery Code
turtle.penup()
turtle.setup(640,480,0,0) #I really think the screen resolution should be much lower. The original size is larger than my screen.
turtle.bgcolor("#00FFFF")
drawSquare(0,-240,670,275,3,"Blue","Blue")#DrawOcean
turtle.goto(-320,-25)
turtle.pendown()
turtle.pencolor("#D5F2A1")
turtle.fillcolor("#DAF7A6")
turtle.begin_fill()
for i in range(10): # Generate random sand
    turtle.seth(random.randint(-5,5))
    turtle.forward(65)
turtle.goto(320,-240)
turtle.goto(-320,-240)
turtle.end_fill()
turtle.penup()
for i in range(4): #Draw random clouds
    turtle.goto(random.randint(-320,240), random.randint(50,200))
    turtle.seth(random.randint(-20,20))
    drawCloud(5)
turtle.fillcolor("#000000")
turtle.goto(-250, -150)
for i in range(5): #Draw garbage
    turtle.seth(random.randint(-359,359))
    turtle.stamp()
    turtle.seth(0)
    turtle.forward(120)
turtle.goto(319, 239)
turtle.dot(180,"Yellow")
turtle.goto(-340, -60)

#"Animation" Code
turtle.shape("turtle")
time.sleep(1)
turtle.speed(2)
turtle.goto(0, -70)
time.sleep(1)
turtle.right(180)
time.sleep(0.5)
turtle.left(180)
time.sleep(1)
turtle.pencolor("#000000")
turtle.write("Now that I have arrived at the beach... Now what to do?",False,"left", font=('Arial', 8 , 'bold'))
inp = input("What should the turtle do now? Clean up the garbage [G], or build a sandcastle? [C]")
turtle.pencolor("#DAF7A6")
turtle.write("Now that I have arrived at the beach... Now what to do?",False,"left", font=('Arial', 8 , 'bold'))
if inp == "G":
    turtle.speed(1)
    turtle.seth(-125)
    turtle.goto(-260, -150)
    turtle.dot(80, "#DAF7A6")
    for i in range(4): #"Clean" garbage
        turtle.seth(0)
        turtle.forward(120)
        turtle.dot(80, "#DAF7A6")
elif inp == "C": #Build Sandcastles
    drawSquare(-35,-120,95,142,3,"#C2B280","#B9A977")
    drawSquare(60,-120,95,75,3,"#C2B280","#B9A977")
    drawTriangle(-35,22,105,3,"#C2B280","#B9A977")
    drawTriangle(60,-45,105,3,"#C2B280","#B9A977")
#Ending
turtle.penup()
turtle.pencolor("#000000")
turtle.fillcolor("#000000")
turtle.goto(-260, -120)
time.sleep(0.5)
turtle.write("I think that's enough for today. Time to head home.",False,"left", font=('Arial', 8 , 'bold'))
time.sleep(2)
turtle.pencolor("#DAF7A6")
turtle.write("I think that's enough for today. Time to head home.",False,"left", font=('Arial', 8 , 'bold'))
turtle.right(180)
turtle.speed(1)
turtle.goto(-340, -120)


