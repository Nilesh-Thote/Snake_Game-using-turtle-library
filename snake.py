from turtle import Turtle

starting_cord = [(0, 0), (-20, 0), (-40, 0)]
Distance = 20
Up = 90
Down = 270
Right = 0
Left = 180


class Snake:
    def __init__(self):
        self.turtle_obj = []
        self.create_turtle()
        self.head = self.turtle_obj[0]

    def create_turtle(self):
        for i in starting_cord:
            self.add_turtle(i)

    def add_turtle(self, position):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.turtle_obj.append(turtle)

    def extend(self):
        self.add_turtle(self.turtle_obj[-1].position())

    def move(self):
        for i in range(len(self.turtle_obj) - 1, 0, -1):
            xcord = self.turtle_obj[i - 1].xcor()
            ycord = self.turtle_obj[i - 1].ycor()
            self.turtle_obj[i].goto(xcord, ycord)
        self.head.fd(Distance)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(Down)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(Right)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(Left)
