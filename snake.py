from turtle import Turtle
POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in POSITIONS:
            tim = Turtle(shape='square')
            tim.penup()
            tim.color('white')
            tim.goto(position)
            self.segments.append(tim)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        if not self.snake_head.heading() == RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if not self.snake_head.heading() == LEFT:
            self.snake_head.setheading(RIGHT)

    def up(self):
        if not self.snake_head.heading() == DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if not self.snake_head.heading() == UP:
            self.snake_head.setheading(DOWN)
