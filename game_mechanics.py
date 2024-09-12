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
        self.score = 0

        # Set up screen
        self.screen = Screen()
        self.screen.setup(self.SCREEN_X, self.SCREEN_Y)
        self.screen.title("Shnake")
        self.screen.tracer(0)
        self.screen.bgcolor("black")

        # Set difficulty
        self.difficulty = self.screen.textinput("Difficulty", "Choose your difficulty:\n-> Easy\n-> Normal\n-> Hard\n-> Impossible").lower()
        self.difficulty_set = self.assign_difficulty(self.difficulty)
        while not self.difficulty_set:
            self.difficulty = self.screen.textinput("Invalid Choice!", "Choose your difficulty:\n-> Easy\n-> Normal\n-> Hard\n-> Impossible").lower()
            self.difficulty_set = self.assign_difficulty(self.difficulty)

        # Initialize snake
        self.snake = generate_snake()
        self.screen.update()

        # Set up score turtle
        self.score_turtle = Turtle()
        init_score_turtle(self.score_turtle, self.score)

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
            if not self.generated_food:
                self.score += 1
                update_score(self.score_turtle, self.score)
            self.screen.update()
            self.screen.ontimer(self.game_loop, self.game_speed)  # Continue the loop

    def assign_difficulty(self, diff) -> bool:
        if diff == "easy":
            self.game_speed = 150
        elif diff == "normal":
            self.game_speed = 100
        elif diff == "hard":
            self.game_speed = 50
        elif diff == "impossible":
            self.game_speed = 25
        else:
            return False
        return True

    def run(self):
        self.screen.exitonclick()  # Keeps the window open until clicked