from turtle import Turtle
import random

WIDTH = 10
HEIGHT = 10
NUM = 0


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.x = WIDTH
        self.y = HEIGHT

    def move(self):
        x_dir = self.xcor() + self.x
        y_dir = self.ycor() + self.y
        self.goto(x_dir, y_dir)

    def y_bounce(self):
        self.y *= -1

    def x_bounce(self):
        self.x *= -1

    # def current_speed(self):
    #     self.speed(self.num)
    #
    # def speed_increase(self):
    #     self.num += 1

