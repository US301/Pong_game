from turtle import Turtle

WALL_WIDTH = 5
STARTING_Y = 290
FORWARD = 12


class Wall(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.color("white")
        self.width(WALL_WIDTH)
        self.penup()
        self.goto(x=0, y=STARTING_Y)
        self.right(90)

    def draw(self):
        for count in range(round(STARTING_Y * 2 / (FORWARD * 2))):
            self.pendown()
            self.forward(12)
            self.penup()
            self.forward(12)
