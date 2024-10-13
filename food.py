from turtle import Turtle
import random


class Food:
    def __init__(self):
        self.food_is_there = False
        self.food = Turtle("circle")

    def createFood(self):
        self.food.color("blue")
        self.food.shapesize(0.5, 0.5, 0)
        self.food.penup()
        self.food.goto(random.randint(-280, 280), random.randint(-280, 280))

    def collideFood(self):
        self.food.goto(random.randint(-280, 280), random.randint(-280, 280))
