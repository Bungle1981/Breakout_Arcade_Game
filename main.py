from turtle import Screen, Turtle
import time
from scoreboard import Scoreboard
from brick import Brick, Wall
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

scoreboard = Scoreboard()
wall = Wall()
paddle = Paddle()
ball = Ball()

screen.update()
screen.listen()
screen.onkey(paddle.go_left, "a")
screen.onkey(paddle.go_right, "d")
game_is_on = True
while game_is_on == True:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if scoreboard.score == 448:
        scoreboard.GameOver()
        game_is_on = False
    if scoreboard.lives <= 0:
        game_is_on = False
        scoreboard.GameOver()
    for brick in wall.bricks:
        if ball.distance(brick) < 20:
            brick.goto(1000,1000)
            scoreboard.score += brick.points
            scoreboard.RefreshScore()
            ball.bounce_Y()
            ball.move_speed *= 0.999
    if ball.distance(paddle) < 40 and ball.ycor() < -235:
        ball.bounce_Y()
    if ball.ycor() > 290: #bounce on vertical limit
        ball.bounce_Y()
    if ball.xcor() > 285 or ball.xcor() < -290: #bounce on horizontal screen limit
        ball.bounce_X()
    if ball.ycor() < -290: #if ball goes outside of play
        scoreboard.RemoveLive()
        ball.reset_ball()

screen.exitonclick()





