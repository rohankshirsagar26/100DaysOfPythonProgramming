# Randomisation

import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(round(random_float, 2))

# List

fruits = [ 'mango', 'apple', 'banana', 'kiwi', 'dragonfruit']

print(fruits[0], fruits[-1])

fruits[1] = 'jackfruit'

print(fruits)

fruits.append('strawberry')

print(fruits)

fruits.extend(['pineapple', 'orange'])

print(fruits)