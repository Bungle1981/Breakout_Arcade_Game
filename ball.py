from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        #self.setheading(random.randint(0, 360))
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_Y(self):
        self.y_move *= -1

    def bounce_X(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.x_move = 10
        self.move_speed = 0.05
