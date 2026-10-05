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
        neuron_sum = 0
        final_sum = 0
        sum_complete = 0
        for neuron in self.neurons:
            for weight in neuron:
                neuron_sum = weight * inputs[0] + weight * inputs[1]
                self.sum_results.append(neuron_sum)
                print(f'Neuron sum: ${neuron_sum}')
            current_sum = 0
        for sum_result in self.sum_results:
            final_sum += sum_result
        print(f'Final sum: ${final_sum}')
        #sigmoid needs a fix btw and i have an idea, which is to divide it's result by 1000
        sum_complete /= 100000
        try:
            sum_complete = 1 / (1 + math.exp(-final_sum))
        except:
            sum_complete = 0
        return sum_complete 

    def step_function(self, final_sum):
        if final_sum == 1:
            return 1
        elif final_sum == 0:
            return 0
        else:
            return 0

# FOR TESTS ONLY

test_neurons = []
current_tnv = []
for _ in range(5):
    for __ in range(2):
        current_tnv.append(random.randint(-1000,1000))
    test_neurons.append(current_tnv)
    current_tnv = []
print(test_neurons)

new_bot = bot(test_neurons, pygame.Vector2(0,0), 1)
final_sum_test = new_bot.complete_sum([random.randint(0,10000),random.randint(0,50)])
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
        "neurons": f'{getattr(cur_bot, "neurons")}'
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


