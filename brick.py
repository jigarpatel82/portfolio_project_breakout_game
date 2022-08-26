from turtle import *

class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.speed(10)

    def create_bricks(self, x, y, brick_color):
        self.penup()
        self.color(brick_color)
        self.setposition(x, y)
        self.showturtle()
