from turtle import Turtle
FONT = ("Courier New", 15, "bold")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("magenta")
        self.goto(-60, 270)
        self.write(f"Score: {self.score}", font=FONT)

    def update_score(self):
        self.score += 1
        self.undo()
        self.write(f"Score: {self.score}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER",align="center", font=FONT)