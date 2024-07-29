from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from Pong.ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard(-80, 250)
scoreboard2 = Scoreboard(60, 250)

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.listen()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move_ball()
    # Make left paddle move up and down
    left_paddle.move_paddle()

    # Detect the collision of the ball with top and bottom walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y_axis()

    # Detect the collision of the ball with the right and left paddles
    if ball.distance(right_paddle) < 40 or ball.distance(left_paddle) < 40:
        ball.bounce_x_axis()

    # Detect if right paddle and left misses the ball and update score for the opponent every time a player misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_score()

    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard2.update_score()


    # Detect the collision of left paddle with top and bottom walls
    if left_paddle.ycor() >= 260 or left_paddle.ycor() <= -260:
        left_paddle.paddle_bounce()


    screen.update()










 





screen.exitonclick()