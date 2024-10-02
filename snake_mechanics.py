from turtle import *
import random as r

MOVEMENT_SPEED = 20

class Snake():
    def __init__(self) -> None:
        self.snake_body = []
        self.grow(3)

    def grow(self, amount) -> None:
        pieces_grown = 0
        while pieces_grown < amount:
            snake_piece = Turtle()
            snake_piece.color("white")
            snake_piece.speed(0)
            snake_piece.pu()
            snake_piece.shape("square")
        
            if len(self.snake_body) != 0:
                snake_piece.setpos(self.snake_body[-1].pos())
            self.snake_body.append(snake_piece)

            pieces_grown += 1
        self.update_snake()

    # Function for updating snakes body size
    def update_snake(self):
        prev_pos = self.snake_body[0].pos()
        for p in range(1, len(self.snake_body)):
            new_pos = prev_pos
            prev_pos = self.snake_body[p].pos()
            self.snake_body[p].goto(new_pos)

    def check_collision_with_food(self, food) -> bool:
        head_pos = self.snake_body[0].pos()
        food_pos = food.pos()

        distance = ((head_pos[0] - food_pos[0]) ** 2 + (head_pos[1] - food_pos[1]) ** 2) ** 0.5

        if distance <= 10:
            food.hideturtle()
            food.goto(1000, 1000)
            self.grow(1)
            return False
        
        return True

    def check_collision_for_death(self):
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

    def move_forward(self):
        self.snake_body[0].fd(MOVEMENT_SPEED)
        self.update_snake()

    def turn_left(self):
        self.snake_body[0].lt(90)

    def turn_right(self):
        self.snake_body[0].rt(90)

def generate_food() -> Turtle:
    food = Turtle()
    food.pu()
    food.color("red")
    food.shape("circle")
    food.setx(r.randrange(-380, 380, 20))
    food.sety(r.randrange(-280, 280, 20))
    print(food.pos())
    return food

def init_score_turtle(tur, score):
    tur.clear()
    tur.hideturtle()
    tur.color("white")
    tur.pu()
    tur.goto(-380, -280)
    tur.pd()
    tur.write(f"Score: {score}", align="left", font=("Courier", 24, "normal"))

def update_score(tur, score):
    tur.clear()
    tur.write(f"Score: {score}", align="left", font=("Courier", 24, "normal"))

def game_over(tur, score):
    tur.clear()
    tur.goto(0, 60)
    tur.write(f"Game Over", True, align="center", font=("Courier", 24, "normal"))
    tur.goto(0, 20)
    tur.write(f"Final score: {score}", True, align="center", font=("Courier", 24, "normal"))
    tur.goto(0, -100)
    tur.write(f"Click to play again", True, align="center", font=("Courier", 24, "normal"))