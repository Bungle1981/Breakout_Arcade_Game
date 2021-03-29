from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-290,270)
        self.RefreshScore()

    def RefreshScore(self):
        self.clear()
        score = f"Score: {self.score}. High Score: {self.high_score}.   You have {self.lives} lives left!"
        self.write(arg=score,align="left", font=("Arial", 15, "bold"), move=False)

    def RemoveLive(self):
        self.lives -= 1
        self.RefreshScore()

    def GameOver(self):
        self.goto(0, 0)
        if self.score == 448:
            self.write("Maximum points achieved! Well done!!", align="center", font=('Arial', 20, 'bold'), move=False)
        if self.lives <= 0:
            self.write("No more lives! Game over!!", align="center", font=('Arial', 20, 'bold'), move=False)
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))

    def Reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.RefreshScore()