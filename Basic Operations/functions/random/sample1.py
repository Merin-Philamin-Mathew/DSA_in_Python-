import random

print(random.random())

print(random.randint(1,2))   # Random integer between 1 and 10 (inclusive)

print(random.uniform(1,2))   # Random float between 1.5 and 5.5

list = [23,67,783,45]
random.shuffle(list)
print(list)  # The list 'numbers' is shuffled randomly

colors = ['red', 'blue', 'green', 'yellow']
print(random.choice(colors))  # Randomly selects one color from the list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.sample(numbers, 3))  # Randomly selects 3 unique elements from the list

random.seed(3)
print(random.random())  # Random number based on seed 42

print(random.randrange(0, 10, 2))  # Randomly selects from the range [0, 2, 4, 6, 8]



