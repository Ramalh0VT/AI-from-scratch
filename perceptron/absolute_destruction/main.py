import random
import time
weights = []
inputs = [10, 50]

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
    
    
def step_function():
        jump()

print(weights)
print(inputs)

while True:
    inputs[0] += 1
    inputs[1] += 1
    print(inputs)
    sum_function()
    step_function()
    time.sleep(1)

    

    
