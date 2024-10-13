from turtle import  Turtle
class Snake:
    def __init__(self,Screen):
        self.snakes = []
        self.s = Screen
        self.createSnake()
        self.head = self.snakes[0]
    def createSnake(self):
        for i in range(3):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(-i * 20, 0)
            self.snakes.append(snake)
    def growSnake(self):
        snake = Turtle("square")
        snake.penup()
        snake.goto(self.snakes[-1].position())
        self.snakes.append(snake)
        snake.color("white")
    def Up(self):
        if(self.snakes[0].heading() != 270):
            self.snakes[0].setheading(90)

    def Left(self):
        if (self.snakes[0].heading() != 0):
            self.snakes[0].setheading(180)

    def Down(self):
        if (self.snakes[0].heading() != 90):
            self.snakes[0].setheading(270)

    def Right(self):
        if (self.snakes[0].heading() != 180):
            self.snakes[0].setheading(0)

    def moveSnake(self):
        for snake in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake - 1].xcor()
            new_y = self.snakes[snake - 1].ycor()
            self.snakes[snake].goto(new_x, new_y)
        self.s.listen()
        self.s.onkey(key="Up", fun=self.Up)
        self.s.onkey(key="Down", fun=self.Down)
        self.s.onkey(key="Left", fun=self.Left)
        self.s.onkey(key="Right", fun=self.Right)
        self.snakes[0].forward(20)
