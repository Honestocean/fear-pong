from turtle import Turtle
import time

import random

random_number = random.randint(0, 1)
# Create a turtle instance
class my_turtle(Turtle):

    def __init__(self, starting_position):
        super().__init__() 
        self.shapesize(5, 1, 1)
        self.shape("square")
        self.penup()
        self.color("green")
        self.go_to_start_postion(starting_position)
        
    
    def go_up(self):
        if self.ycor() < 260:
             newY = self.ycor() + 20
             self.goto(self.xcor(), newY)

       
    def go_down(self):
        if self.ycor() > -260:
            newY = self.ycor() - 20
            self.goto(self.xcor(), newY)
    
    def go_to_start_postion(self, starting_position):
        self.goto(starting_position)

    def delayed_chase(self, ball_y_cor): 
        random_number = random.uniform(40, 50)
        self.goto(self.xcor(), self.ycor() + (self.ycor() - ball_y_cor / 2))
   



