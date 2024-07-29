import time
from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(xcor,ycor)
        self.y_move = 20
        self.screen = Screen()

    def go_up(self):
        self.sety(self.ycor() + self.y_move)
        self.screen.update()
    def go_down(self):
        self.sety(self.ycor() - self.y_move)
        self.screen.update()

    def move_paddle(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)

    def paddle_bounce(self):
        self.y_move *= -1

