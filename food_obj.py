from turtle import *
import random as r

# Constants for food spawn range
FOOD_SPAWN_X_RANGE = 380
FOOD_SPAWN_Y_RANGE = 280

# Class representing the food in the game
class Food(Turtle):
    # Initialize the food and place it at a random location
    def __init__(self) -> None:
        super().__init__()
        self.pen(pendown=False)
        self.color("red")
        self.shape("circle")
        self.refresh_location()
    
    # Move the food to a new random location
    def refresh_location(self) -> None:
        spawn_x = r.randrange(-FOOD_SPAWN_X_RANGE, FOOD_SPAWN_X_RANGE, 20)
        spawn_y = r.randrange(-FOOD_SPAWN_Y_RANGE, FOOD_SPAWN_Y_RANGE, 20)
        self.teleport(spawn_x, spawn_y)