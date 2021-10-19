
from turtle import Turtle, Screen
from wall import Wall
from players import Player, Player1, Player2
from ball import Ball
from scoreboard import Scoreboard
import time

game_on = True

# Screen Description

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Creating Objects of Classes

wall = Wall()
player_1 = Player1()
player_2 = Player2()
ball = Ball()
score1 = Scoreboard("Player 1")
score2 = Scoreboard("Player 2")
score1.goto(-55, 250)
score2.goto(40, 250)
x = 0.1

screen.listen()

screen.onkey(key="Up", fun=player_1.move_up)
screen.onkey(key="Down", fun=player_1.move_down)
screen.onkey(key="w", fun=player_2.move_up)
screen.onkey(key="s", fun=player_2.move_down)

while game_on is True:
    screen.update()
    time.sleep(x)
    # ball.current_speed()
    ball.move()
    score1.update_score()
    score2.update_score()
    if ball.ycor() > 278 or ball.ycor() < -270:
        ball.y_bounce()
    if ball.distance(player_2) < 50 and ball.xcor() > 340 or ball.distance(player_1) < 50 and ball.xcor() < -340:
        ball.x_bounce()
        x *= 0.1
    if ball.xcor() > 420:
        score1.increase_score()
        ball.hideturtle()
        ball.setposition(0, 0)
        ball.x_bounce()
        ball.showturtle()
    elif ball.xcor() < -420:
        score2.increase_score()
        ball.hideturtle()
        ball.setposition(0, 0)
        ball.x_bounce()
        ball.showturtle()
    if score1.score == 10:
        ball.hideturtle()
        wall.hideturtle()
        score1.winner()
        game_on = False
    if score2.score == 10:
        ball.hideturtle()
        wall.hideturtle()
        score2.winner()
        game_on = False


screen.exitonclick()










# See PyCharm help at https://www.jetbrains.com/help/pycharm/
