from turtle import *
import random as r

MOVEMENT_SPEED = 20
FOOD_SPAWN_X_RANGE = 380
FOOD_SPAWN_Y_RANGE = 280

class Snake():
    # Initialize the snake with a default size of 3 segments
    def __init__(self) -> None:
        self.snake_body = []

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
            pieces_grown += 1

    # Move the snake forward and update the positions of the body segments
    def update_snake_and_move_forward(self) -> None:
        if len(self.snake_body) <= 1:
            return

        prev_pos = self.snake_body[0].pos()
        self.snake_body[0].fd(MOVEMENT_SPEED)

        for p in range(1, len(self.snake_body)):
            new_pos = prev_pos
            prev_pos = self.snake_body[p].pos()
            self.snake_body[p].goto(new_pos)

    # Check if the snake's head has collided with the food
    def check_collision_with_food(self, food) -> bool:
        head_pos = self.snake_body[0].pos()
        food_pos = food.pos()

        distance = ((head_pos[0] - food_pos[0]) ** 2 + (head_pos[1] - food_pos[1]) ** 2) ** 0.5

        if distance <= 10:
            food.refresh_location()
            self.grow(1)
            return True
        
        return False

    # Check if the snake's head has collided with the boundaries or its body
    def check_collision_with_self(self) -> bool:
        if (self.snake_body[0].xcor() > 400 or self.snake_body[0].xcor() < -400 or 
            self.snake_body[0].ycor() > 300 or self.snake_body[0].ycor() < -300):
            return True

        for p in range(1, len(self.snake_body)):
            head_pos = self.snake_body[0].pos()
            body_pos = self.snake_body[p].pos()
            
            distance = ((head_pos[0] - body_pos[0]) ** 2 + (head_pos[1] - body_pos[1]) ** 2) ** 0.5
            
            if distance < 5:
                return True
        
        return False

    def reset_snake(self) -> None:
        for snake_piece in self.snake_body:
            snake_piece.hideturtle()
        self.snake_body.clear()
        
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

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.pen(pendown=False)
        self.color("red")
        self.shape("circle")
        self.refresh_location()
    
    def refresh_location(self) -> None:
        spawn_x = r.randrange(-FOOD_SPAWN_X_RANGE, FOOD_SPAWN_X_RANGE, 20)
        spawn_y = r.randrange(-FOOD_SPAWN_Y_RANGE, FOOD_SPAWN_Y_RANGE, 20)
        self.teleport(spawn_x, spawn_y)