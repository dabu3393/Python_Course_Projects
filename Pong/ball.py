from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 2
        self.y_move = 2
        self.move_speed = 1.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def speed_up(self):
        self.x_move *= self.move_speed
        self.y_move *= self.move_speed

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.home()
        self.x_move = 2
        self.y_move = 2
        self.bounce_x()
