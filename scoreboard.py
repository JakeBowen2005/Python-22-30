import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()
        

    def update_score(self):
        self.goto(-100, 225)
        self.write(self.left_score, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 225)
        self.write(self.right_score, align="center", font=("Courier", 70, "normal"))

    def plus_right(self):
        self.right_score += 1
        self.clear()
        self.update_score()

    def plus_left(self):
        self.left_score += 1
        self.clear()
        self.goto(-100, 225)
        self.update_score()

        
