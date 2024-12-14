import turtle as t
import time

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("slow")
        self.x_move = 1.5
        self.y_move = 1.5
        
    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x=x, y=y)

    def change_y(self):
        self.y_move *= -1

    def change_x(self):
        self.x_move *= -1
        
    def reset(self):
        time.sleep(0.5)
        self.goto(x=0, y=0)
        self.x_move = 1
        self.y_move = 1
        self.change_x()

    def increase_speed(self):
        self.x_move *= 1.1
        self.y_move *= 1.1
