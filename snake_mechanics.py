from turtle import *
import random as r

def generate_snake():
    generated_snake = []
    snake_pieces = 3
    x = 0
    while snake_pieces > 0:
        snake_piece = Turtle()
        snake_piece.speed(0)
        snake_piece.pu()
        snake_piece.shape("square")
        generated_snake.append(snake_piece)
        snake_piece.setx(x)
        snake_pieces -= 1
        x -= 20
    return generated_snake

def movement(snake):
    prev_pos = snake[0].pos()
    snake[0].fd(20)
    for p in range(1, len(snake)):
        new_pos = prev_pos
        prev_pos = snake[p].pos()
        snake[p].goto(new_pos)

def grow_snake(snake):
    snake_piece = Turtle()
    snake_piece.speed(0)
    snake_piece.pu()
    snake_piece.shape("square")
    snake.append(snake_piece)
    movement(snake)

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
    food.setx(r.randrange(-380, 401, 20))
    food.sety(r.randrange(-280, 281, 20))
    print(food.pos())
    return food