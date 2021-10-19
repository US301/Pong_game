from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, name):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.name = name

    def update_score(self):
        self.write(arg=f"{self.score}", align="left", font=("Arial", 40, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def winner(self):
        self.color("white")
        self.goto(-100, 0)
        self.write(arg=f"{self.name} is the Winner!", align="left", font=("Arial", 20, "normal"))

# class Player1score(Scoreboard):
#     def __init__(self):
#         super().__init__()
#         self.setx(-55)
#         self.sety(250)
#
#
# class Player2score(Scoreboard):
#     def __init__(self):
#         super().__init__()
#         self.setx(40)
#         self.sety(250)





