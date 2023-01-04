from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import scoreboard
import time

PLAYER1_XPOS = (350, 0)
PLAYER2_XPOS = (-350, 0)

screen = Screen()
screen.tracer(0)
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)

player_paddle = Paddle(PLAYER1_XPOS)
pc_paddle = Paddle(PLAYER2_XPOS)
pong = Ball()
sb = scoreboard()

screen.update()

screen.listen()
screen.onkey(fun=player_paddle.move_up, key="Up")
screen.onkey(fun=player_paddle.move_down, key="Down")
screen.onkey(fun=pc_paddle.move_up, key="w")
screen.onkey(fun=pc_paddle.move_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    pong.move()
    if pong.ycor() > 280 or pong.ycor() < - 280:
        pong.wall_bounce()
    if (pong.xcor() > 330 or pong.xcor() < - 330) and (pong.distance(player_paddle) < 50 or  pong.distance(pc_paddle) < 50):
        pong.paddle_bounce()
    elif pong.xcor() > 380:
        sb.inc_pc_score()
        pong.restart()
    elif pong.xcor() < -380:
        sb.inc_player_score()
        pong.restart()


screen.exitonclick()