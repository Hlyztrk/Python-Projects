from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.square_list = []
        self.create_snake()
        self.head = self.square_list[0]

    def create_snake(self):
        for i in range(3):
            new_square = self.add_segment()
            new_square.setx(i * -MOVE_DISTANCE)
            self.square_list.append(new_square)

    def add_segment(self):
        square = Turtle("square")
        square.color("white")
        square.penup()
        return square

    def extend_snake(self):
        new_square = self.add_segment()
        new_square.setx(self.square_list[-1].xcor() * MOVE_DISTANCE)
        self.square_list.append(new_square)

    def move(self):
        for square_index in range(len(self.square_list) - 1, 0, -1):
            new_xcor = self.square_list[square_index - 1].xcor()
            new_ycor = self.square_list[square_index - 1].ycor()
            self.square_list[square_index].goto(new_xcor, new_ycor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def is_wall_in_front(self):
        if self.head.xcor() >= 290 or self.head.xcor() <= -290 or self.head.ycor() >= 290 or self.head.ycor() <= -290:
            return True
        return False

    def collide_with_itself(self):
        for square in self.square_list[1:]:
            if self.head.distance(square) < 15:
                return True
        return False


