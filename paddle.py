from turtle import Turtle
MOVE_FORWARD = 20


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(pos)

    def move_up(self):
        self.forward(MOVE_FORWARD)

    def move_down(self):
        self.backward(MOVE_FORWARD)