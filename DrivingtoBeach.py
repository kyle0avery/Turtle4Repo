'''
Turtle Drives to beach  *nested  loop - dodge obstacle in traffic
have random objects to dodge 
screen can be 2880 x 1800
range must meet 1800 for distance to meet full screen
top of road y = 200
middle of road 100
bottom of road y=0
'''
import turtle  
import time
import random

#set up first ----DELTETE BEFORE SENDING FUNCTION TO MAIN
turtle.setup(2880,1800,0,0)
time.sleep(3)
turtle.shape('turtle')
turtle.pensize(3)
turtle.speed(5)
turtle.penup()
turtle.goto(-700,-400)

screen_hedge = int()
screen_ledge = int()
road_length = int()
screen_hedge = 1750
screen_ledge = 2700
road_length = 0

##### drawing bottom of road | bottom of road y=0 | -1440 - 1440
turtle.goto(-1440,0)
turtle.setheading(0) #east
turtle.pendown()

while road_length < screen_hedge:
    turtle.forward(300)
    turtle.setheading(25)
    turtle.forward(100)
    turtle.setheading(30)
    turtle.forward(50)
    turtle.setheading(0)
    turtle.forward(300)
    road_length = road_length + 800


##### drawing top of road | top of road y = 200 | -1440 - 1440
turtle.penup()
turtle.goto(-1440,200)
turtle.setheading(0) #east
turtle.pendown()
road_length = 0
while road_length < screen_hedge:
    turtle.forward(300)
    turtle.setheading(25)
    turtle.forward(100)
    turtle.setheading(30)
    turtle.forward(50)
    turtle.setheading(0)
    turtle.forward(300)
    road_length = road_length + 800


##### drawing middle of road | top of road y = 100 | -1440 - 1440
#### think of way to make dotted
### every 25 | if(num%2) != 0:
##what for variable of forward distance 
#!!!!!!!!! 9:02 inner can control penup/down
turtle.penup()
turtle.goto(-1440,100)
turtle.setheading(0) #east
turtle.penup()
road_length = 0
while road_length < screen_hedge: # use inner loop to control pen up and dpwn only 
    dist_count = 0
    while dist_count < 300:
        turtle.forward(25)
        if (dist_count%2) == 0:
            turtle.pendown()
        else:
            turtle.penup()
        dist_count = dist_count + 25
    turtle.setheading(25)
    turtle.forward(100)
    turtle.setheading(30)
    turtle.forward(50)
    turtle.setheading(0)
    turtle.forward(300)
    road_length = road_length + 800


# set obstacles in road  with stamp method
turtle.setheading(180)
turtle.goto(300,200)
turtle.stamp()
turtle.forward(50)
turtle.stamp()
turtle.setheading(90)
turtle.forward(100)
turtle.setheading(180)
turtle.forward(50)
turtle.stamp()
turtle.forward(100)
turtle.stamp()
time.sleep(1)
turtle.goto(0,0)
turtle.write("     Oh no!",False,"left",14)
time.sleep(1)
turtle.goto(0,-100)
turtle.write("Looks like I wasted all my loops on setup and forgot to save some for navigation.",False,"left",14)
time.sleep(1)
turtle.goto(0,-200)
turtle.write("     Guess I better just skip ahead..",False,"left",14)
time.sleep(3)


