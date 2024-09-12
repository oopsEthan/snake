from turtle import *
import random as r

def grow_snake(snake):
    snake_piece = Turtle()
    snake_piece.color("white")
    snake_piece.speed(0)
    snake_piece.pu()
    snake_piece.shape("square")
    if len(snake) != 0:
        snake_piece.setpos(snake[-1].pos())
    snake.append(snake_piece)
    update_snake(snake)

def generate_snake():
    generated_snake = []
    snake_pieces = 3
    while snake_pieces >= 0:
        grow_snake(generated_snake)
        snake_pieces -= 1
    return generated_snake

# Function for updating snakes body size
def update_snake(snake):
    prev_pos = snake[0].pos()
    for p in range(1, len(snake)):
        new_pos = prev_pos
        prev_pos = snake[p].pos()
        snake[p].goto(new_pos)

def check_collision(snake, food) -> bool:
    if (snake[0].xcor() > 400 or snake[0].xcor() < -400 or 
        snake[0].ycor() > 300 or snake[0].ycor() < -300):
        bye() # Needs to die here or something, restart

    head_pos = snake[0].pos()
    food_pos = food.pos()

    distance = ((head_pos[0] - food_pos[0]) ** 2 + (head_pos[1] - food_pos[1]) ** 2) ** 0.5

    if distance <= 10:
        food.hideturtle()
        food.goto(1000, 1000)
        grow_snake(snake)
        return False
    
    return True

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
    tur.hideturtle()
    tur.color("white")
    tur.pu()
    tur.goto(-380, -280)
    tur.pd()
    tur.write(f"Score: {score}", align="left", font=("Courier", 24, "normal"))

def update_score(tur, score):
    tur.clear()
    tur.write(f"Score: {score}", align="left", font=("Courier", 24, "normal"))