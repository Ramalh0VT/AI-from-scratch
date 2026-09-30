import random
import time
import pygame
import math

class bot:
    def __init__(self, neurons, pos, to_id):
        self.neurons = neurons
        self.pos = pos
        self.id = to_id
        self.alive = True
        self.sum_results = []
    #Both neuron sum ,final sum AND sigmoid function are included in the below function
    def complete_sum(self, inputs):
        current_sum = 0
        final_sum = 0
        for neuron in self.neurons:
            for weight in neuron:
                current_sum = weight * inputs[0] + weight * inputs[1]
                self.sum_results.append(current_sum)
            current_sum = 0
        for sum_result in self.sum_results:
            final_sum += sum_result
        return 1 / (1 + math.exp(-final_sum))

    def step_function(self, final_sum):
        if final_sum >= 0.9:
            return 1
        elif final_sum < 0.9:
            return 0

test_neurons = []
current_tnv = []
for _ in range(5):
    for __ in range(2):
        current_tnv.append(random.randint(-1000,1000))
    test_neurons.append(current_tnv)
    current_tnv = []
print(test_neurons)

new_bot = bot([[-72,92], [9, -39], [-500, -583],[120, 300],[942, 938]], pygame.Vector2(0,0), 1)
final_sum_test = new_bot.complete_sum([30,10])
print(final_sum_test)


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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
    screen.fill("white")
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()


