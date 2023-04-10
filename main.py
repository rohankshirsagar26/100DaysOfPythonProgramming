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