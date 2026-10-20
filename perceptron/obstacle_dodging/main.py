import random
import time
import pygame
import math
import sys
#Variables and assets used across the code

pygame.init()
screen = pygame.display.set_mode((640,360))
clock = pygame.time.Clock()
running = True
dt = 0
font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 14)

pygame.display.set_caption("AI dinossaur training")

game_speed = 4
jump_count = 10
best_ai_score = 0
end = False
obstacle_timer = 0
obstacle_spawn = False
obstacle_cooldown = 800

ground = pygame.image.load("assets/ground.png")
ground = pygame.transform.scale(ground,(640, 360))
print(ground)
ground_x = 0
ground_rect = ground.get_rect(center=(320,200))
cloud = pygame.image.load("assets/cloud.png")
cloud = pygame.transform.scale(cloud,(100,40))

cloud_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
ptero_group = pygame.sprite.Group()
ai_group = pygame.sprite.Group()

# AI CLASSES
class bot(pygame.sprite.Sprite):
    def __init__(self, neurons, x_pos, y_pos, to_id): 
        super().__init__()
        self.neurons = neurons
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.id = to_id
        self.alive = True
        self.sum_results = []
        
        self.running_sprites = []
        self.benting_sprites = [] 
        self.running_sprites.append(pygame.transform.scale(pygame.image.load("./assets/Dino1.png"), (80,100)))
        self.running_sprites.append(pygame.transform.scale(pygame.image.load("./assets/Dino2.png"), (80,100)))
        self.benting_sprites.append(pygame.transform.scale(pygame.image.load("./assets/DinoBenting1.png"), (110,60)))
        self.benting_sprites.append(pygame.transform.scale(pygame.image.load("./assets/DinoBenting2.png"), (110,60)))

        self.current_image = 0
        self.image = self.running_sprites[self.current_image]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.velocity = 40
        self.gravity = 6.5
        self.bented = False

        def jump(self):
            jump_sfx:play()
            if self.rect.centery >= 360:
                while self.rect.centery - self.velocity > 40:
                    self.rect.centery -= 1
        def bent(self):
            self.benting = True
            self.rect.centery = 380
        
        def unbent(self):
            self.benting = False
            self.rect.centery = 360

        def fall(self):
            if self.rect.centery <= 360:
                self.rect.centery += self.gravity

        def apply_animations(self):
            self.current_image += 0.05
            if self.current_image >= 2:
                self.current_image = 0

            if self.benting:
                self.image = self.benting_sprites[int(self.current_image)]
            else:
                self.image = self.running_sprites[int(self.current_image)]
    # LOGIC FOR APPLYING WEIGHTS / STEP FUNCTIONING
    #Both neuron sum ,final sum AND sigmoid function are included in the below function
    def complete_sum_jump(self, inputs):
        neuron_sum = 0
        final_sum = 0
        sum_complete = 0
        for neuron in self.neurons:
            for weight in neuron:
                neuron_sum = weight * inputs[0] + weight * inputs[1]
                self.sum_results.append(neuron_sum)
            current_sum = 0
        for sum_result in self.sum_results:
            final_sum += sum_result
        final_sum = final_sum / 1000000
        try:
            sum_complete = 1 / (1 + math.exp(-final_sum))
        except:
            sum_complete = 0
        return sum_complete 

    def step_function_jump(self, final_sum):
        if final_sum >= 0.6:
            return 1
        elif final_sum < 0.6:
            return 0
        else:
            return 0

    def complete_sum_benting(self, inputs):
        neuron_sum = 0
        final_sum = 0
        sum_complete = 0
        for neuron in self.neurons:
            for weight in neuron:
                neuron_sum = weight * inputs[0] + weight * inputs[1]
                self.sum_results.append(neuron_sum)
            current_sum = 0
        for sum_result in self.sum_results:
            final_sum += sum_result
        final_sum = final_sum / 1000000
        try:
            sum_complete = 1 / (1 + math.exp(-final_sum))
        except:
            sum_complete = 0
        return sum_complete 

    def step_function_benting(self, final_sum):
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

class cactus(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.sprites = []
        for i in range(1,7):
            current_sprite = pygame.transform.scale(pygame.image.load(f"assets/cacti/cactus{i}.png"), (100,100))
            self.sprites.append(current_sprite)
        self.image = random.choice(self.sprites)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
    def update(self):
        self.x_pos -= game_speed
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

class ptero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = 650
        self.y_pos = random.choice([140,147,175])
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load("assets/Ptero1.png"), (84,62)))
        self.sprites.append(pygame.transform.scale(pygame.image.load("assets/Ptero2.png"), (84,62)))
        self.current_image = 0
        self.image = self.sprites[self.current_image]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
    
    def update(self):
        self.animate()
        self.x_pos -= game_speed
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def animate(self):
        self.current_image += 0.025
        if self.current_image >= 2:
            self.current_image = 0
        self.image = self.sprites[int(self.current_image)]

#bot generator

bots_array = []
cur_neuron_weights = []
cur_layer_weights = []
final_neurons_weights = []

for cur_id in range(500):
    for _ in range(2):
        for _ in range(5):
            for _ in range(2):
                cur_neuron_weights.append(random.randint(-1000,1000))
            cur_layer_weights.append(cur_neuron_weights)
            cur_neuron_weights = []
        final_neurons_weights.append(cur_layer_weights)
        cur_layer_weights = []            
    cur_bot = bot(final_neurons_weights,40,180, cur_id +1)
    bots_array.append({
        "id": f'{getattr(cur_bot, "id")}',
        "neurons": f'{getattr(cur_bot, "neurons")}'
        })
    ai_group.add(cur_bot)
    final_neurons_weights = []
print(bots_array[0])

#sound effects

death_sound = pygame.mixer.Sound("assets/sfx/lose.mp3")
jump_sound = pygame.mixer.Sound("assets/sfx/jump.mp3")
point_sound = pygame.mixer.Sound("assets/sfx/100points.mp3")

CLOUD_EVENT = pygame.USEREVENT
pygame.time.set_timer(CLOUD_EVENT,300)

# functions

def last_ai_killed():
    if len(bots_array) <= 10:
        global best_ai_score, game_speed
        game_over_text = game_font.render("That was the last one!", True, "black")
        game_over_rect = game_over_text.get_rect(center=(320,150))
        score_text = game_font.render(f"Score: {int(best_ai_score)}")
        score_rect = score_text.get_rect(center=(320, 170))
        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)
        game_speed = 5
        cloud_group.empty()
        obstacle_group.empty()
# insert here code to make the best ai weights save in maybe a json
        




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
        if event.type == CLOUD_EVENT:
            current_cloud_y = randint(25,150)
            current_cloud = cloud(cloud,690, current_cloud_y)
            cloud_group.add(current_cloud)
    screen.fill("white")
    # i still don't know surely how i'll kill an ai 
    # if pygame.spritecollide(ai_group.sprite,obstacle_group, False):        
    if len(bots_array) <= 1:
        game_over = True
    if game_over:
        last_ai_killed()
    if not game_over:
        game_speed += 0.0025
        if round(best_ai_score,1) % 100 == 0 and int(best_ai_score) > 0:
            point_sfx.play()

        if pygame.time.get_ticks() - obstacle_timer >= obstacle_cooldown:
            obstacle_spawn = True
        
        if obstacle_spawn:
            obstacle_random = random.randint(1,50)
            if obstacle_random in range(1,7):
                new_obstacle = cactus(640,170)
                obstacle_group.add(new_obstacle)
                obstacle_timer = pygame.time.get_ticks()
                obstacle_spawn = False
            elif obstacle_random in range(7,10):
                new_obstacle = ptero()
                obstacle_group.add(new_obstacle)
                obstacle_timer = pygame.time.get_ticks()
                obstacle_spawn = False

                

    dt = clock.tick(60) / 1000
pygame.quit()
sys.exit()



