from turtle import Turtle

UP = 90
DOWN = 270


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.move_up()
        self.move_down()

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)


class Player1(Player):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setx(-370)
        self.sety(0)
        self.showturtle()


class Player2(Player):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setx(370)
        self.sety(0)
        self.showturtle()