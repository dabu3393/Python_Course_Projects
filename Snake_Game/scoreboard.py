from turtle import Turtle

POSITION = (0, 270)
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.write_scoreboard()

    def write_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.write_scoreboard()

    def update(self):
        self.score += 1
        self.write_scoreboard()