from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(arg=f"Score {self.score}",align="center",font=("Arial",15,"bold"))

    def increaseScore(self):
        self.score = self.score + 1
        self.clear()
        self.write(arg=f"Score {self.score}", align="center", font=("Arial", 15, "bold"))

    def gameOver(self):
        self.clear()
        self.goto(0,0)
        self.write(arg =f"Game Over :(  Your Score {self.score}", align="center", font= ("Arial",20,"bold"))