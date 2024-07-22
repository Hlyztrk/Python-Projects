from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("magenta")
        self.penup()
        self.shapesize(0.5)
        self.refresh()
    def refresh(self):
        random_xcor = random.randint(-280, 280)
        random_ycor = random.randint(-280, 270)
        self.goto(random_xcor, random_ycor)
