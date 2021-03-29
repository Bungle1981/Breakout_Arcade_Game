from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=3)
        self.penup()
        self.color("white")
        self.goto(0, -250)

    def go_right(self):
        new_y = self.ycor()
        new_x = self.xcor() + 40
        self.goto(new_x, new_y)

    def go_left(self):
        new_y = self.ycor()
        new_x = self.xcor() - 40
        self.goto(new_x, new_y)