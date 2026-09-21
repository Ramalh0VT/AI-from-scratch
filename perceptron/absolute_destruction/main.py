import random
weights = []
inputs = [10, 50]

for i in range(7):
    weights.append(random.randint(-1000,1000))

def jump():
    print("jumped")

def sum_function():
    global the_sum = 0
    for weight in weights:
            the_sum += (weight * inputs[0])
            the_sum += (weight * inputs[1])
    
def step_function():
    if the_sum > 0:
        jump()

while True:
    inputs[0] += 1
    inputs[1] += 1
    sum_function()
    step_function()
    time.sleep(0.1)

    

    
