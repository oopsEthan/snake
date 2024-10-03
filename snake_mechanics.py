from turtle import *
import random as r

MOVEMENT_SPEED = 20

class Snake():
    # Initialize the snake with a default size of 3 segments
    def __init__(self) -> None:
        self.snake_body = []
        self.snake_body.append(None)
        self.grow_head()
        self.grow(3)

    def grow_head(self):
        snake_piece = Turtle()
        snake_piece.color("white")
        snake_piece.speed(0)
        snake_piece.pu()
        snake_piece.shape("square")
        self.snake_body[0] = snake_piece

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

        print(f"Attempting to move snake, body length: {len(self.snake_body)}")
        prev_pos = self.snake_body[0].pos()
        print(f"Moving head from {prev_pos}")
        self.snake_body[0].fd(MOVEMENT_SPEED)

        for p in range(1, len(self.snake_body)):
            new_pos = prev_pos
            prev_pos = self.snake_body[p].pos()
            self.snake_body[p].goto(new_pos)

    # Check if the snake's head has collided with the food
    def check_collision_with_food(self, food: Turtle) -> bool:
        head_pos = self.snake_body[0].pos()
        food_pos = food.pos()

        distance = ((head_pos[0] - food_pos[0]) ** 2 + (head_pos[1] - food_pos[1]) ** 2) ** 0.5

        if distance <= 10:
            food.hideturtle()
            food.goto(1000, 1000)
            self.grow(1)
            return False
        
        return True

    # Check if the snake's head has collided with the boundaries or its body
    def check_collision_for_death(self) -> bool:
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

    # Turn the snake left by 90 degrees
    def turn_left(self) -> None:
        self.snake_body[0].lt(90)

    # Turn the snake right by 90 degrees
    def turn_right(self) -> None:
        self.snake_body[0].rt(90)

    # Print debug information when needed, called by pressing "g"
    def debug_print(self) -> None:
        pass

# Generate a food item at a random position
def generate_food() -> Turtle:
    food = Turtle()
    food.pu()
    food.color("red")
    food.shape("circle")
    food.setx(r.randrange(-380, 380, 20))
    food.sety(r.randrange(-280, 280, 20))
    print(food.pos())
    return food

# Initialize the score display turtle
def init_score_turtle(tur: Turtle, score: int) -> None:
    tur.clear()
    tur.hideturtle()
    tur.color("white")
    tur.pu()
    tur.goto(-380, -280)
    tur.pd()
    tur.write(f"Score: {score}", align="left", font=("Courier", 24, "normal"))

# Update the score on the screen
def update_score(tur: Turtle, score: int) -> None:
    tur.clear()
    tur.write(f"Score: {score}", align="left", font=("Courier", 24, "normal"))

# Display the game over screen
def game_over(tur: Turtle, score: int) -> None:
    tur.clear()
    tur.goto(0, 60)
    tur.write(f"Game Over", True, align="center", font=("Courier", 24, "normal"))
    tur.goto(0, 20)
    tur.write(f"Final score: {score}", True, align="center", font=("Courier", 24, "normal"))
    tur.goto(0, -100)
    tur.write(f"Click to play again", True, align="center", font=("Courier", 24, "normal"))