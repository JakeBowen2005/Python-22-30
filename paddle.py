import turtle as t

class Paddle(t.Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        y = self.ycor() + 33
        self.goto(x=self.xcor(), y=y)

    def down(self):
        y = self.ycor() - 33
        self.goto(x=self.xcor(), y=y)