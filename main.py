from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

s = Screen()
s.tracer(0)
s.setup(width=600, height=600)
s.bgcolor("black")
snake = Snake()
food = Food()
score = Scoreboard()
s.update()
s.listen()
s.onkeypress(key="Up", fun=snake.up)
s.onkeypress(key="Down", fun=snake.down)
s.onkeypress(key="Left", fun=snake.left)
s.onkeypress(key="Right", fun=snake.right)

gameison = True
while gameison:
    s.update()
    time.sleep(0.1)
    snake.move()

    # detection of collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_updater()

    # detection of collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameison = False
        score.game_over()

    # detection of collision with it's tail

    for turtle in snake.turtle_obj[1:]:
        if snake.head.distance(turtle) < 10:
            gameison = False
            score.game_over()

s.exitonclick()
