from turtle import *
from snake_mechanics import *
from ui import UI

class SnakeGame():
    def __init__(self) -> None:
        # Initial variables
        self.SCREEN_X = 800
        self.SCREEN_Y = 600
        self.MOVEMENT_SPEED = 20
        self.snake_obj = Snake()

        self.food = Food()
        self.ui = UI()

        # Set up screen - may move into UI?
        self.screen = Screen()
        self.screen.setup(self.SCREEN_X, self.SCREEN_Y)
        self.screen.title("Shnake")
        self.screen.tracer(0)
        self.screen.bgcolor("black")

        self.reset_game()

    def game_loop(self):
        if not self.collisions_detected["self"]:
            self.snake_obj.update_snake_and_move_forward()

            self.collisions_detected["food"] = self.snake_obj.check_collision_with_food(self.food)
            self.collisions_detected["self"] = self.snake_obj.check_collision_with_self()
            self.resolve_collisions()

            self.screen.update()
            self.screen.ontimer(self.game_loop, 100)
    
    def resolve_collisions(self) -> None:
        if self.collisions_detected["food"]:
            self.ui.update_score(1)
            self.collisions_detected["food"] = False
        
        elif self.collisions_detected["self"]:
            self.ui.game_over()
            self.screen.onclick(lambda x, y: self.reset_game())

    def reset_game(self):
        self.screen.update()
        
        # Initialize uncategorized variables
        self.collisions_detected = {"food": False, "self": False}

        # Initialize score
        self.ui.reset_score()

        # Set up controls
        self.screen.listen()
        self.screen.onkey(self.snake_obj.turn_left, "a")
        self.screen.onkey(self.snake_obj.turn_right, "d")
        self.screen.onkey(self.snake_obj.debug_print, "g")
        
        # Start the game loop
        self.game_loop()

    def run(self):
        self.screen.mainloop()