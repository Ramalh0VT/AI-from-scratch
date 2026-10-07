import random
import time
import pygame
import math

# AI CLASSES
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
        final_sum = final_sum / 1000000
        print(final_sum)
        try:
            sum_complete = 1 / (1 + math.exp(-final_sum))
        except:
            sum_complete = 0
        return sum_complete 

    def step_function(self, final_sum):
        if final_sum >= 0.6:
            return 1
        elif final_sum < 0.6:
            return 0
        else:
            return 0
# GAME OBJECTS CLASSES

class cloud(pygame.sprite.Sprite):
    def __init__(self,image,x_pos,y_pos):
        super().__init__()
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

        def update(self):
            self.rect.x -= 1
#the dinossaurs that will be in the game
class ai_holder(pygame.sprite.Sprite)
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.running_sprites = []
        self.ducking_sprites = [] 
        self.running_sprites.append(pygame.transform.scale(pygame.image.load("./assets/Dino1.png"), (80,100)))
        self.running_sprites.append(pygame.transform.scale(pygame.image.load("./assets/Dino2.png"), (80,100)))
        self.ducking_sprites.append(pygame.transform.scale(pygame.image.load("./assets/DinoDucking1.png"), (110,60)))
        self.ducking_sprites.append(pygame.transform.scale(pygame.image.load("./assets/DinoDucking2.png"), (110,60)))

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.current_image = 0
        self.image = running_sprites[self.current_image]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.velocity = 40
        self.gravity = 6.5
        self.ducking = False


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
print(new_bot.step_function(final_sum_test))

pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True
dt = 0

pygame.display.set_caption("AI dinossaur game")

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
print(bots_array)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
    screen.fill("white")
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()


