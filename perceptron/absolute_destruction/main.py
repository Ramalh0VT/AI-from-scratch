import random
import time
import pygame

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
