# Scope

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

# Global Scope

potion_strength = 2

def drink_potion():
    print(potion_strength)

drink_potion()

# There is no block scope in Pyhon

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
  new_enemy = enemies[0]

print(new_enemy)

def create_enemy():
  enemies = ["Skeleton", "Zombie", "Alien"]

  if game_level < 5:
    new_enemy = enemies[0]

create_enemy()
print(new_enemy)

# Modifying global scope variable

enemies = 1

def increase_enemies():
  global enemies
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")