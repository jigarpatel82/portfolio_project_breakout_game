import random
from turtle import *
from paddle import Paddle
from brick import Brick
from ball import Ball
import time

points = 0
trial = 3

# Setting up screen
window = Screen()
window.bgcolor('black')
window.title('Breakout Game')

# Creating paddle and attaching left and right button for moving the paddle
paddle = Paddle()
paddle.create_paddle()
window.listen()
window.onkey(paddle.move_right, 'Right')
window.onkey(paddle.move_left, 'Left')
window.tracer(400)

# Creating Bricks
bricks = []
red_x = -295
red_y = 160
orange_x = -295
orange_y = 130
green_x = -295
green_y = 100
yellow_x = -295
yellow_y = 70

for i in range(14):
    i = Brick()
    i.create_bricks(x=red_x, y=red_y, brick_color='red')
    red_x += 45
    bricks.append(i)

for i in range(14, 28):
    i = Brick()
    i.create_bricks(x=orange_x, y=orange_y, brick_color='orange')
    orange_x += 45
    bricks.append(i)

for i in range(28, 42):
    i = Brick()
    i.create_bricks(x=green_x, y=green_y, brick_color='green')
    green_x += 45
    bricks.append(i)

for i in range(42, 56):
    i = Brick()
    i.create_bricks(x=yellow_x, y=yellow_y, brick_color='yellow')
    yellow_x += 45
    bricks.append(i)

# Create ball
ball = Ball()
ball.create_ball()
window.update()
game_is_on = True

# Creating turtle to update point screen
point_turtle = Turtle()
point_turtle.penup()
point_turtle.pencolor('white')
point_turtle.hideturtle()
point_turtle.setposition(-290, 200)
point_turtle.write(f'Points: {points}', font=('Courier new', 30, 'bold'))

# Creating turtle to update trial screen
trial_turtle = Turtle()
trial_turtle.penup()
trial_turtle.pencolor('white')
trial_turtle.hideturtle()
trial_turtle.setposition(120, 200)
trial_turtle.write(f'Trials: {trial}', font=('Courier new', 30, 'bold'))


while game_is_on:
    time.sleep(0.1)
    window.update()
    ball.move_forward()

    # removing brick when it touches the ball
    for brick in bricks:
        if brick.distance(ball) < 30:
            points += 20
            point_turtle.clear()
            point_turtle.write(f'Points: {points}', font=('Courier new', 30, 'bold'))
            bricks.remove(brick)
            brick.hideturtle()
            ball.setheading(345 - ball.heading() - random.randint(-5, 5))
            print(f'point:{points}')

    # bounce ball from paddle
    if ball.distance(paddle) < 40:
        ball.setheading(360 - ball.heading())

    # bounce ball from top wall
    elif ball.ycor() > 270:
        ball.setheading(360 - ball.heading())

    # bounce ball from side walls
    elif ball.xcor() < -293 or ball.xcor() > 289:
        ball.setheading(180 - ball.heading())

    # if ball pass the paddle
    elif ball.ycor() < -300:
        if trial != 1:
            trial -= 1
            trial_turtle.clear()
            trial_turtle.write(f'Trials: {trial}', font=('Courier new', 30, 'bold'))
            ball.goto(-15, 0)
            paddle.goto(0, -200)
            time.sleep(0.2)
        else:
            game_is_on = False
            window.clearscreen()
            window.bgcolor('black')
            game_over_turtle = Turtle()
            game_over_turtle.hideturtle()
            game_over_turtle.pencolor('white')
            game_over_turtle.write('GAME OVER', move=False, align='center', font=('Courier new', 40, 'bold'))

window.exitonclick()