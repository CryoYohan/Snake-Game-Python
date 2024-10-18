from turtle import Turtle
X_COR = 0
Y_COR = 260
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(X_COR,Y_COR)
        self.pencolor('white')
        self.write(arg=f'Score: {self.score}', move=True, align='center', font=( "Courier", 20, "normal"))

    def add_score(self):
        self.score+=1
        self.clear()
        self.goto(X_COR, Y_COR)
        self.write(arg=f'Score: {self.score}', move=False, align='center', font=("Courier", 20, "normal"))
