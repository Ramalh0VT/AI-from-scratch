import random
import time
import pygame

class ai:
    def __init__(self):
        self.weights = []
        for i in range(7):
            self.weights.append(random.randint(-1000,1000))

    def sum_function(self, vision_array):
        sum_result = 0
        for weight in self.weights:
        sum_result += weight * vision_array[0]
        sum_result += weight * vision_array[1]
        return sum_result
    
    def step_function(self, final_sum):
        if final_sum > 0:
            return True
        elif final_sum <= 0:
            return False
        
    




pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(0,0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    pygame.draw.circle(screen, "red", player_pos, 50)   
pygame.quit()



"""
weights = []
inputs = [0, 0]

for i in range(7):
    weights.append(random.randint(-1000,1000))

def jump():
    print("jumped")

def sum_function():
    the_sum = 0
    for weight in weights:
            the_sum += (weight * inputs[0])
            the_sum += (weight * inputs[1])
    if the_sum > 0:
        step_function()
    else:
        print("didn't jump")
    print(f'sum: ${the_sum}')
    
    
def step_function():
        jump()

print(weights)
print(inputs)

while True:
    inputs[0] += 1
    inputs[1] += 1
    print(inputs)
    sum_function()
    time.sleep(1)
"""

