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

# Nested List

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)