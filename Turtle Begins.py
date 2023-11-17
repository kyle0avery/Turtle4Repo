'''
Turtle Begins

Turtle Leaves House  *input - ask what turtle will collect at the beach, shells, trash, or fish

-need list 



'''


import turtle
import time
beach_items = ["rocks", "shells", "nothing"]


#mainly set up first 
turtle.shape('turtle')
turtle.pensize(15)
turtle.setup(2880,1800,0,0)
turtle.speed(3)
turtle.penup()
turtle.goto(-400,0)

#drawing turtlehouse
turtle.pensize(2)
turtle.pencolor("black")
turtle.pendown()
turtle.setheading(0)
turtle.forward(50)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(15)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(15)
turtle.setheading(270)
turtle.forward(100)
turtle.left(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.goto(-340,-40)
turtle.pendown()
turtle.dot(30,"black")
turtle.penup()


#####starting the journey 
time.sleep(3)
turtle.setheading(0)



#####   inout && list #######
turtle.write("        It's a beautiful day outside. I think I'll go to the beach and collect some new furntiure What should I choose?  ",False,"left",14)
user_prompt = str("Choose what Turtle should collect: ") + str(beach_items)
user_input = input(user_prompt)
time.sleep(3)
turtle.clear()
user_choice = "      Ok! " + user_input + " it is!"
turtle.write(user_choice,False,"left",14)


#movingg off screen & clearing screen for next funct
turtle.penup()
turtle.forward(600)
turtle.clear()
turtle.goto(0,0)




time.sleep(4)

