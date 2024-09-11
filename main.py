from turtle import *
from snake_mechanics import *

SCREEN_X = 800
SCREEN_Y = 600

snake = []
dead = False
food = None
generated_food = False

screen = Screen()

screen.tracer(0)
snake = generate_snake()
screen.update()

screen.setup(SCREEN_X, SCREEN_Y)

def turn_left():
    snake[0].lt(90)

def turn_right():
    snake[0].rt(90)

# ETHAN IN THE FUTURE ->
# - need collision logic to acquire score
# - need to code in snake pieces growing in length
# - need score displaying on screen
# - background color/title change, etc for vanity

screen.listen()
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")

def game_loop():
    global dead
    global generated_food
    global food

    if not generated_food:
        food = generate_food()
        generated_food = True
    if not dead:
        movement(snake)
        generated_food = check_collision(snake, food)
        screen.update()
        screen.ontimer(game_loop, 100)

game_loop()

screen.exitonclick()