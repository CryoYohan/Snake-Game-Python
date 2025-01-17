from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep

class Window:
    def __init__(self):
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor('black')
        self.screen.title('My Snake Game')
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.game_is_running = False
        self.listen_keys()

    def start(self):
        self.game_is_running = True
        while self.game_is_running:
            self.screen.update()
            sleep(0.1)
            self.snake.move()

            # Detect food collision
            if self.snake.snake_head.distance(self.food) < 15:
                print('nom nom nom')
                self.food.refresh()
                self.snake.extend()
                self.scoreboard.add_score()

            # Detect wall collision
            if self.snake.snake_head.xcor() > 280 or self.snake.snake_head.xcor() < -280 or self.snake.snake_head.ycor() > 280 or self.snake.snake_head.ycor() < -280:
                self.game_is_running = False
                self.scoreboard.game_over()

            # Detect Tail collision
            for segment in self.snake.segments[1:]:
                if self.snake.snake_head.distance(segment) < 10:
                    self.game_is_running = False
                    self.scoreboard.game_over()


    def listen_keys(self):
        self.screen.listen()
        self.screen.onkey(self.snake.up, 'Up')
        self.screen.onkey(self.snake.down, 'Down')
        self.screen.onkey(self.snake.left, 'Left')
        self.screen.onkey(self.snake.right, 'Right')
