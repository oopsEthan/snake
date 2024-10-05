from turtle import *

UI_SCORE_X = -380
UI_SCORE_Y = -280
SCREEN_X = 800
SCREEN_Y = 600

# Class that handles the UI of the Snake game, such as the score display and game over screen
class UI(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.update_score(0)
        self.initialize_screen()

    # Updates the score on the screen by the specified point_gained value
    def update_score(self, point_gained: int) -> None:
        self.clear()
        self.score += point_gained
        self.teleport(UI_SCORE_X, UI_SCORE_Y)
        self.write(f"Score: {self.score}", align="left", font=("Courier", 24, "normal"))

    # Resets the score back to zero on the screen
    def reset_score(self) -> None:
        self.score = 0
        self.update_score(0)

    # Displays the game over screen with the final score and resets the game on click
    def game_over(self, func) -> None:
        self.clear()
        self.teleport(0, 60)
        self.write(f"Game Over", True, align="center", font=("Courier", 24, "normal"))
        self.teleport(0, 20)
        self.write(f"Final score: {self.score}", True, align="center", font=("Courier", 24, "normal"))
        self.teleport(0, -100)
        self.write(f"Click to play again", True, align="center", font=("Courier", 24, "normal"))

        self.screen.listen()
        self.screen.onclick(func)
        self.screen.update()

    # Initializes the game screen with title, size, and background color
    def initialize_screen(self) -> None:
        self.screen = Screen()
        self.screen.setup(SCREEN_X, SCREEN_Y)
        self.screen.title("Shnake")
        self.screen.tracer(0)
        self.screen.bgcolor("black")

    # Updates the screen and schedules the next function call in the game loop
    def loop(self, func) -> None:
        self.screen.update()
        self.screen.ontimer(func, 100)

    # Begins listening for key inputs to control the snake's movements
    def begin_listening(self, snake) -> None:
        self.screen.listen()
        self.screen.onkey(snake.turn_left, "a")
        self.screen.onkey(snake.turn_right, "d")
        self.screen.onkey(snake.debug_print, "g")