from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))

    def score_updater(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over", align="center", font=("Arial", 15, "normal"))
