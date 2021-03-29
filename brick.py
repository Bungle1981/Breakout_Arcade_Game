from turtle import Turtle

class Wall():
    def __init__(self):
        self.bricks = []
        for a in range(0, 8):
            if a == 0:
                positionx = -270
                positiony = 255
                for brick in range (0, 14):
                    newBrick = Brick(color="red", points=7,  position=(positionx, positiony))
                    self.bricks.append(newBrick)
                    positionx += 41
                positiony -= 13
            if a == 1:
                positionx = -270
                for brick in range (0, 14):
                    newBrick = Brick(color="red", points=7, position=(positionx, positiony))
                    self.bricks.append(newBrick)
                    positionx += 41
                positiony -= 13
            if a == 2:
                positionx = -270
                for brick in range (0, 14):
                    newBrick = Brick(color="orange",  points=5, position=(positionx, positiony))
                    self.bricks.append(newBrick)
                    positionx += 41
                positiony -= 13
            if a == 3:
                positionx = -270
                for brick in range (0, 14):
                    newBrick = Brick(color="orange", points=5, position=(positionx, positiony))
                    self.bricks.append(newBrick)
                    positionx += 41
                positiony -= 13
            if a == 4:
                positionx = -270
                for brick in range (0, 14):
                    newBrick = Brick(color="green", points=3,  position=(positionx, positiony))
                    self.bricks.append(newBrick)
                    positionx += 41
                positiony -= 13
            if a == 5:
                positionx = -270
                for brick in range (0, 14):
                    newBrick = Brick(color="green", points=3, position=(positionx, positiony))
                    self.bricks.append(newBrick)
                    positionx += 41
                positiony -= 13
            if a == 6:
                positionx = -270
                for brick in range (0, 14):
                    newBrick = Brick(color="yellow", points=1, position=(positionx, positiony))
                    self.bricks.append(newBrick)
                    positionx += 41
                positiony -= 13
            if a == 7:
                positionx = -270
                for brick in range (0, 14):
                    newBrick = Brick(color="yellow", points=1, position=(positionx, positiony))
                    self.bricks.append(newBrick)
                    positionx += 41

class Brick(Turtle):
    def __init__(self, color, position, points):
        super().__init__()
        self.shape("square")
        self.points = points
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=1.9)
        self.color(color)
        self.speed("fastest")
        self.goto(position)
