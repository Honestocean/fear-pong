from turtle import Screen 
from firstTurtle import my_turtle
from ball import Ball
import time 

screen = Screen()
screen.setup(width = 1200, height = 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

rightstartposition = (450, 0)
leftstartposition = (-450, 0)

rightpaddle = my_turtle(rightstartposition); 
leftpaddle = my_turtle(leftstartposition); 

newball = Ball()



screen.update()
screen.listen()
screen.onkeypress(rightpaddle.go_up, "Up")
screen.onkeypress(rightpaddle.go_down, "Down")

screen.onkeypress(leftpaddle.go_up, "w")
screen.onkeypress(leftpaddle.go_down, "s")

game_is_on = True 
while game_is_on: 
    time.sleep(newball.move_speed)
    screen.update()
    newball.move()

    if newball.ycor() > 280 or newball.ycor() < -280:
        newball.bounce_y()

    if newball.distance(rightpaddle) < 50 and newball.xcor() > 430:
        newball.bounce_x() 
        rightpaddle.color("white")
    
    if newball.distance(leftpaddle) < 50 and newball.xcor() < -430:
        leftpaddle.color("white")
        newball.bounce_x() 

    rightpaddle.delayed_chase( newball.ycor())    

        



screen.exitonclick()