from snake_obj import Snake
from food_obj import Food
from ui_handler import UI

# Class that manages the Snake game, including the snake, food, UI, and game state
class SnakeGame:
    # Initializes the snake, food, and UI, and resets the game
    def __init__(self) -> None:
        self.snake_obj: Snake = Snake()
        self.food: Food = Food()
        self.ui: UI = UI()

        self.reset_game()

    # The main game loop: moves the snake, checks for collisions, and handles game progression
    def game_loop(self) -> None:
        if not self.collisions_detected["body"] and not self.collisions_detected["boundary"]:
            self.snake_obj.update_snake_and_move_forward()

            self.collisions_detected["food"] = self.snake_obj.check_collision_with_food(self.food)
            self.collisions_detected["body"] = self.snake_obj.check_collision_with_body()
            self.collisions_detected["boundary"] = self.snake_obj.check_collision_with_boundaries()

            self.resolve_collisions()

            self.ui.loop(self.game_loop)
    
    # Resolves collisions, such as eating food or hitting a wall or itself
    def resolve_collisions(self) -> None:
        if self.collisions_detected["food"]:
            self.ui.update_score(1)
            self.collisions_detected["food"] = False
        
        elif self.collisions_detected["body"] or self.collisions_detected["boundary"]:
            self.ui.game_over(self.reset_game)

    # Resets the game by resetting the snake, collisions, score, and input listening
    def reset_game(self, x: int = None, y: int = None) -> None:
        self.snake_obj.reset_snake()
        self.food.refresh_location()
        self.collisions_detected = {"food": False, "body": False, "boundary": False}

        self.ui.reset_score()
        self.ui.begin_listening(self.snake_obj)
        
        self.game_loop()

    # Starts the main game loop by activating the UI screen's mainloop
    def run(self) -> None:
        self.ui.screen.mainloop()