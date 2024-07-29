from turtle import Turtle

FONT = ("Helvetica", 25)


class Scoreboard(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(xcor, ycor)
        self.write(f"{self.score}", font=FONT)

    def update_score(self):
        self.score += 1
        self.undo()
        self.write(f"{self.score}", font=FONT)
