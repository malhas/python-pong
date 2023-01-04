from turtle import Turtle
import random
MOVE_XFORWARD = 10
MOVE_YFORWARD = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xpace = MOVE_XFORWARD 
        self.ypace = MOVE_YFORWARD

    def move(self):
        self.goto(self.xcor() + self.xpace, self.ycor() + self.ypace)

    def wall_bounce(self):
        self.ypace = -self.ypace

    def paddle_bounce(self):
        self.xpace = -self.xpace

    def restart(self):
        self.goto(0, 0)
        self.paddle_bounce()

