from turtle import *

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=4)
        self.color('#86c5da')

    def create_paddle(self):
        self.hideturtle()
        self.penup()
        self.setposition(0, -200)
        self.showturtle()

    def move_right(self):
        if self.xcor() < 280:
            self.setheading(0)
            self.forward(20)

    def move_left(self):
        if self.xcor() > -281:
            self.backward(20)




