from turtle import *

UI_SCORE_X = -380
UI_SCORE_Y = -280

class UI(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.update_score(0)

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
    def game_over(self) -> None:
        self.clear()
        self.teleport(0, 60)
        self.write(f"Game Over", True, align="center", font=("Courier", 24, "normal"))
        self.teleport(0, 20)
        self.write(f"Final score: {score}", True, align="center", font=("Courier", 24, "normal"))
        self.teleport(0, -100)
        self.write(f"Click to play again", True, align="center", font=("Courier", 24, "normal"))