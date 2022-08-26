from turtle import *
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.hideturtle()
        self.setheading(random.randint(267, 273))

    def create_ball(self):
        self.penup()
        self.setposition(-15, 0)
        self.color('grey')
        self.showturtle()

    def move_forward(self):
        self.forward(20)

    def move_backward(self):
        self.backward(20)


