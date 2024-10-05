from turtle import *
from snake_mechanics import *
from ui import UI

class SnakeGame():
    def __init__(self) -> None:
        # Initial variables
        self.MOVEMENT_SPEED = 20
        self.snake_obj = Snake()

        self.food = Food()
        self.ui = UI()

        self.reset_game()

    def game_loop(self):
        if not self.collisions_detected["self"]:
            self.snake_obj.update_snake_and_move_forward()

            self.collisions_detected["food"] = self.snake_obj.check_collision_with_food(self.food)
            self.collisions_detected["self"] = self.snake_obj.check_collision_with_self()
            self.resolve_collisions()

            self.ui.loop(self.game_loop)
    
    def resolve_collisions(self) -> None:
        if self.collisions_detected["food"]:
            self.ui.update_score(1)
            self.collisions_detected["food"] = False
        
        elif self.collisions_detected["self"]:
            self.ui.game_over(self.reset_game)


    def reset_game(self):
        print("Game reset initializing...")

        # Initialize uncategorized variables
        self.collisions_detected = {"food": False, "self": False}
        print("Collisions reset.")

        # Initialize score
        self.ui.reset_score()
        print("Score reset.")

        # Set up controls
        self.ui.begin_listening(self.snake_obj)
        print("Listening begin.")
        
        # Start the game loop
        print("Game reset completed.")
        self.game_loop()

    def run(self):
        self.ui.screen.mainloop()