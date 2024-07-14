import random
import turtle
from turtle import Turtle, Screen, TK

screen = Screen()
# Set the size, background color and title of the main window
screen.title("Turtle Race")
screen.setup(500,400)
screen.bgcolor("#fcf4bb")

# Register finish flag gif
finishflag = screen.register_shape("finish-flag-32.gif")

# Position the flags to the finish line
pos = -160
for i in range(2):
    flag = Turtle("finish-flag-32.gif")
    flag.penup()
    flag.goto(200, pos)
    pos += 330

# Create a list of colors of the turtles to be created
colors = ["red", "green", "blue", "purple", "orange", "cyan"]
# Create a list of turtles with colors provided above
list_of_turtles= []
for i in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(i)
    list_of_turtles.append(new_turtle)

# Start the race
def start_race():
    # Pop up a dialog window for input of a user guess.
    guess = turtle.textinput("Who is the winner?","Which colour of turtle will win the race?\nRed, green, blue, purple, orange or cyan")
    guess.strip().lower()
    # Set the start position for turtles
    space_between_turtles = -100
    for name in list_of_turtles:
        name.penup()
        name.goto(-230, space_between_turtles)
        space_between_turtles += 40
    # Start the race
    game_continue = True
    while game_continue:
        for name in list_of_turtles:
            name.forward(random.randint(0,10))
            if name.xcor() >= 200.0:
                game_continue = False
                if guess == name.pencolor():
                    TK.messagebox.showinfo(title="The Turtle says:", message="Yay! You win!")
                else:
                    TK.messagebox.showinfo(title="The Turtle says:", message=f"You've lost. The winner is {name.pencolor()} turtle")
                break
    play_again = screen.textinput("Play again?","Would you like to play again? Y/N")
    play_again.strip().lower()
    if play_again == 'y':
        start_race()
    else:
        turtle.bye()

start_race()

