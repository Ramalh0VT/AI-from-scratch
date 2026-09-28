import random
import time
import pygame

class bot:
    def __init__(self, weights, pos, to_id):
        self.weights = weights
        self.pos = pos
        self.id = to_id

    def sum_function(self, vision_array):
        sum_result = 0
        for weight in self.weights:
            sum_result += weight * vision_array[0]
            sum_result += weight * vision_array[1]
            return sum_result
    
    def step_function(self, final_sum):
        if final_sum >= 0.9:
            return 1
        elif final_sum < 0.9:
            return 0

    def update_pos(self):
        pygame.draw.circle(screen, "red", self.pos, 40)    

pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True
dt = 0

new_bot = bot([1,2,3], pygame.Vector2(0,0), 1)
print((getattr(new_bot,'id')))

bots_array = []
for i in range(500):
    cur_weights = []
    for i in range(7):
        cur_weights.append(random.randint(-1000,1000))
    cur_bot = bot(cur_weights, pygame.Vector2(0,0), i)
    bots_array.append(getattr(bot, "id"))



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
    screen.fill("white")
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()


