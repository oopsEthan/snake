from turtle import *
import os

UI_SCORE_Y = 260
SCREEN_X = 800
SCREEN_Y = 600

# Class that handles the UI of the Snake game, such as the score display and game over screen
class UI(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.pen(pendown=False, shown=False)
        self.color("white")
        self.high_score = self.initialize_high_score()
        self.update_score(0)
        self.initialize_screen()
    
    def initialize_high_score(self) -> int:
        if os.path.exists("score_save.txt"):
            self.high_score = self.load_high_score()
        
        else:
            self.high_score = 0
            self.save_high_score()
        
        return self.high_score

    def load_high_score(self) -> int:
        with open("score_save.txt", "r") as score_save:
            high_score = score_save.read()
            high_score = int(high_score)
            return high_score
        
    def save_high_score(self) -> None:
        with open("score_save.txt", "w") as score_save:
            score_save.write(str(self.high_score))
        
    # Updates the score on the screen by the specified point_gained value
    def update_score(self, point_gained: int) -> None:
        self.clear()
        self.score += point_gained
        if self.score >= self.high_score:
            self.high_score = self.score
        self.teleport(0, UI_SCORE_Y)
        self.write(f"SCORE: {self.score}", align="center", font=("Courier", 24, "normal"))
        self.teleport(0, UI_SCORE_Y-25)
        self.write(f"HIGH SCORE: {self.high_score}", align="center", font=("Courier", 16, "normal"))

    # Resets the score back to zero on the screen
    def reset_score(self) -> None:
        self.score = 0
        self.update_score(0)

    # Displays the game over screen with the final score and resets the game on click
    def game_over(self, func) -> None:
        self.clear()
        self.teleport(0, 60)
        self.write(f"GAME OVER", True, align="center", font=("Courier", 24, "normal"))
        self.teleport(0, 0)
        self.write(f"CLICK TO PLAY AGAIN", True, align="center", font=("Courier", 16, "normal"))

        self.save_high_score()
        
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