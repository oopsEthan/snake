from turtle import *

UI_SCORE_X = -380
UI_SCORE_Y = -280
SCREEN_X = 800
SCREEN_Y = 600

class UI(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.update_score(0)
        self.initialize_screen()

    # Update the score on screen by point_gained
    def update_score(self, point_gained: int) -> None:
        self.clear()
        self.score += point_gained
        self.teleport(UI_SCORE_X, UI_SCORE_Y)
        self.write(f"Score: {self.score}", align="left", font=("Courier", 24, "normal"))

    # Reset the score on screen
    def reset_score(self) -> None:
        self.score = 0
        self.update_score(0)

    # Display the game over screen
    def game_over(self, func) -> None:
        self.clear()
        self.teleport(0, 60)
        self.write(f"Game Over", True, align="center", font=("Courier", 24, "normal"))
        self.teleport(0, 20)
        self.write(f"Final score: {self.score}", True, align="center", font=("Courier", 24, "normal"))
        self.teleport(0, -100)
        self.write(f"Click to play again", True, align="center", font=("Courier", 24, "normal"))

        self.screen.onclick(lambda x, y: func())
        self.screen.update()

    def initialize_screen(self) -> None:
        # Set up screen - may move into UI?
        self.screen = Screen()
        self.screen.setup(SCREEN_X, SCREEN_Y)
        self.screen.title("Shnake")
        self.screen.tracer(0)
        self.screen.bgcolor("black")

    def loop(self, func) -> None:
        self.screen.update()
        self.screen.ontimer(func, 100)

    def begin_listening(self, snake) -> None:
        self.screen.listen()
        self.screen.onkey(snake.turn_left, "a")
        self.screen.onkey(snake.turn_right, "d")
        self.screen.onkey(snake.debug_print, "g")