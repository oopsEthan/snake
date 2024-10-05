from turtle import *

# Constants for snake movement speed
SNAKE_MOVEMENT_SPEED = 20
SCREEN_BORDER_X = 400
SCREEN_BORDER_Y = 300
COLLISION_THRESHOLD = 10

# Class representing the snake in the game
class Snake:
    # Initialize the snake with an empty list for its body segments
    def __init__(self) -> None:
        self.snake_body = []
        self.snake_head = None

    # Grow the snake by adding 'amount' of new segments
    def grow(self, amount: int) -> None:
        pieces_grown = 0
        while pieces_grown < amount:
            snake_piece = Turtle()
            snake_piece.color("white")
            snake_piece.speed(0)
            snake_piece.pu()
            snake_piece.shape("square")
            self.snake_body.append(snake_piece)

            # Designate first piece as "snake_head"
            if len(self.snake_body):
                self.snake_head = self.snake_body[0]

            pieces_grown += 1

    # Move the snake forward and update the positions of the body segments
    def update_snake_and_move_forward(self) -> None:
        if len(self.snake_body) <= 1:
            return

        prev_pos = self.snake_body[0].pos()
        self.snake_body[0].fd(SNAKE_MOVEMENT_SPEED)

        for p in range(1, len(self.snake_body)):
            new_pos = prev_pos
            prev_pos = self.snake_body[p].pos()
            self.snake_body[p].goto(new_pos)

    # Check if the snake's head has collided with the food
    def check_collision_with_food(self, food) -> bool:
        if self.snake_head.distance(food) <= COLLISION_THRESHOLD:
            food.refresh_location()
            self.grow(1)
            return True
        
        return False

    # Check for collision with the snake's own body
    def check_collision_with_self(self) -> bool:
        for p in range(1, len(self.snake_body)):
             if self.snake_head.distance(self.snake_body[p]) <= COLLISION_THRESHOLD:
                return True
        
        return False

    # Check for boundary collision
    def check_collision_with_boundaries(self) -> bool:
        if (self.snake_head.xcor() > SCREEN_BORDER_X or self.snake_head.xcor() < -SCREEN_BORDER_X or 
            self.snake_head.ycor() > SCREEN_BORDER_Y or self.snake_head.ycor() < -SCREEN_BORDER_Y):
            return True
        
        return False

    # Reset the snake's position and size
    def reset_snake(self) -> None:
        # Hide all segments and clear the snake body
        for snake_piece in self.snake_body:
            snake_piece.hideturtle()
        self.snake_head = None
        self.snake_body.clear()
        
        # Regrow the snake with 3 segments
        self.grow(3)

    # Turn the snake left by 90 degrees
    def turn_left(self) -> None:
        self.snake_body[0].lt(90)

    # Turn the snake right by 90 degrees
    def turn_right(self) -> None:
        self.snake_body[0].rt(90)

    # Print debug information when needed, called by pressing "g"
    def debug_print(self) -> None:
        pass