from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 260)
        self.write_score()

    def write_score(self):
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.home()
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)
