from turtle import *
from snake_mechanics import *

class SnakeGame():
    def __init__(self) -> None:
        # Initial variables
        self.SCREEN_X = 800
        self.SCREEN_Y = 600
        self.MOVEMENT_SPEED = 20
        self.snake = []
        self.dead = False
        self.food = None
        self.generated_food = False

        # Set up screen
        self.screen = Screen()
        self.screen.setup(self.SCREEN_X, self.SCREEN_Y)
        self.screen.title("Shnake")
        self.screen.tracer(0)
        
        # Initialize snake
        self.snake = generate_snake()
        self.screen.update()

        # Set up controls
        self.screen.listen()
        self.screen.onkey(self.turn_left, "a")
        self.screen.onkey(self.turn_right, "d")

        # Start the game loop
        self.game_loop()

    def turn_left(self):
        self.snake[0].lt(90)

    def turn_right(self):
        self.snake[0].rt(90)

    def game_loop(self):
        if not self.generated_food:
            self.food = generate_food()
            self.generated_food = True

        if not self.dead:
            self.snake[0].fd(self.MOVEMENT_SPEED)
            update_snake(self.snake)
            self.generated_food = check_collision(self.snake, self.food)
            self.screen.update()
            self.screen.ontimer(self.game_loop, 100)  # Continue the loop

    def run(self):
        self.screen.exitonclick()  # Keeps the window open until clicked