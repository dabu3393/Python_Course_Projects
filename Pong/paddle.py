from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, paddle_coordinates):
        super().__init__()
        self.coordinates = paddle_coordinates
        self.create_paddle()
        self.penup()
        self.goto(paddle_coordinates)

    def create_paddle(self):
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
