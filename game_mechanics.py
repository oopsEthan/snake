from turtle import *
from snake_mechanics import *

class SnakeGame():
    def __init__(self) -> None:
        # Initial variables
        self.SCREEN_X = 800
        self.SCREEN_Y = 600
        self.MOVEMENT_SPEED = 20
        self.snake_obj = Snake()

        self.food = None
        self.score_turtle = None

        # Set up screen
        self.screen = Screen()
        self.screen.setup(self.SCREEN_X, self.SCREEN_Y)
        self.screen.title("Shnake")
        self.screen.tracer(0)
        self.screen.bgcolor("black")

        self.set_up_game()

    def game_loop(self):
        if not self.generated_food:
            self.food = generate_food()
            self.generated_food = True

        if not self.dead:
            self.snake_obj.move_forward()
            self.dead = self.snake_obj.check_collision_for_death()
            self.generated_food = self.snake_obj.check_collision_with_food(self.food)
            if not self.generated_food:
                self.score += 1
                update_score(self.score_turtle, self.score)
            self.screen.update()
            self.screen.ontimer(self.game_loop, self.game_speed)  # Continue the loop
        
        else:
            game_over(self.score_turtle, self.score)
            self.screen.onclick(lambda x, y: self.set_up_game())

    def set_up_game(self):
        # Initialize snake
        if self.snake_obj:
            for snake_piece in self.snake_obj.snake_body:
                snake_piece.hideturtle()
                del snake_piece
            self.snake_obj.snake_body.clear()
        self.snake_obj.grow(3)
        self.screen.update()
        
        # Initialize uncategorized variables
        self.dead = False
        self.score = 0

        # Initialize food
        self.generated_food = False
        if self.food != None:
            self.food.hideturtle()
            self.food.goto(1000, 1000)

        # Initialize score
        if self.score_turtle == None:
            self.score_turtle = Turtle()
        init_score_turtle(self.score_turtle, self.score)

        # Determine difficulty
        self.difficulty = self.screen.textinput("Difficulty", "Choose your difficulty:\n-> Easy\n-> Normal\n-> Hard\n-> Impossible").lower()
        self.difficulty_set = self.assign_difficulty(self.difficulty)
        while not self.difficulty_set:
            self.difficulty = self.screen.textinput("Invalid Choice!", "Choose your difficulty:\n-> Easy\n-> Normal\n-> Hard\n-> Impossible").lower()
            self.difficulty_set = self.assign_difficulty(self.difficulty)

        # Set up controls
        self.screen.listen()
        self.screen.onkey(self.snake_obj.turn_left, "a")
        self.screen.onkey(self.snake_obj.turn_right, "d")
        
        # Start the game loop
        self.game_loop()

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
        self.screen.mainloop()