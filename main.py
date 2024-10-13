import random
import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from Score import Score

s = Screen()
s.bgcolor("black")
s.title("Snake Game")
s.setup(height=600, width=600)
s.tracer(0)
game_is_on = True
snake_o = Snake(s)
food = Food()
score = Score()
running = True
food.createFood()
s.listen()


def pause():
    global running
    if(running):
        running= False
    else:
        running = True
    #running = (True, False)[running]
    print(running)


while game_is_on:
    s.onkey(key="space", fun=pause)
    s.update()
    time.sleep(0.1)
    if running:
        snake_o.moveSnake()
        if snake_o.head.distance(food.food) < 15:
            food.collideFood()
            score.increaseScore()
            snake_o.growSnake()
        if snake_o.head.xcor() > 290 or snake_o.head.xcor() < -290 or snake_o.head.ycor() > 290 or snake_o.head.ycor() < -290:
            score.gameOver()
            game_is_on = False
        for i in range(1, len(snake_o.snakes)):
            if snake_o.head.distance(snake_o.snakes[i]) < 10:
                score.gameOver()
                game_is_on = False
    s.onkey(key="space", fun=pause)
s.exitonclick()
