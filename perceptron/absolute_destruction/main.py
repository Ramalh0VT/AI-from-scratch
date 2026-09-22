import random
import time
import pygame

class ai:
    def __init__(self):
        self.weights = []
        self.pos = pygame.Vector2(0,0)
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

    def update_pos(self):
        pygame.draw.circle(screen, "red", self.pos, 40)    


pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
screen.fill("white")




pygame.quit()


