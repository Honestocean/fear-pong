from turtle import Turtle 

START_SPEED = 0.02 

class Ball(Turtle):

    def __init__(self):
        super().__init__() 
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 3       
        self.y_move = 3
        self.move_speed = START_SPEED 
        
    
    def move(self): 
        new_X = self.xcor() + self.x_move
        new_Y = self.ycor() + self.y_move
        self.goto(new_X, new_Y)

    def bounce_y(self): 
        self.y_move *= -1    
    
    def bounce_x(self): 
        self.x_move *= -1
        self.move_speed *= 0.9
    
    def reset_position(self): 
        self.goto(0,0)
        self.move_speed = START_SPEED
        self.bounce_x()

