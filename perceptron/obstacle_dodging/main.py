import random
import time
import pygame

class bot:
    def __init__(self, weights, pos, to_id):
        self.neurons = neurons
        self.pos = pos
        self.id = to_id
        self.alive = True
        self.sum_results = []
    
    #Both neuron sum and final sum are included in the below function
     
    def complete_sum(self, inputs):
        current_sum = 0
        for neuron in neurons:
            for weight in neuron:
                current_sum = weight * inputs[0] + weight * inputs[1]
                sum_results.append(current_sum)
            current_sum = 0
                
    def step_function(self, final_sum):
        if final_sum >= 0.9:
            return 1
        elif final_sum < 0.9:
            return 0


pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True
dt = 0

bots_array = []
cur_weights = []

for cur_id in range(500):
    for _ in range(2):
        cur_weights.append(random.randint(-1000,1000))
    cur_bot = bot(cur_weights, pygame.Vector2(0,0), cur_id +1)
    bots_array.append({
        "id": f'{getattr(cur_bot, "id")}',
        "weights": f'{getattr(cur_bot, "weights")}'
        })
    cur_weights = []

print(bots_array)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
    screen.fill("white")
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()


