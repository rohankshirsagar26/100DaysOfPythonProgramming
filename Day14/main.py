import random
from art import logo, vs
from game_data import data
from replit import clear

print(logo)

score = 0
game_is_over = False


player_one = random.choice(data)
player_two = random.choice(data)

while not game_is_over:
  
  print(f"\nCompare A: {player_one['name']}, {player_one['description']} from {player_one['country']}. {player_one['follower_count']} {vs}\nCompare B: {player_two['name']}, {player_two['description']} from {player_two['country']}. {player_two['follower_count']}")
  
  followers = input("\nWho has more followers? Type 'A' or 'B': ")
  
  if followers == 'A':
    if player_one["follower_count"] > player_two["follower_count"]:
      score += 1
      player_two = random.choice(data)
      clear()
      print(f"\n✅ You're right! Current score: {score} ✅")
    else:
      game_is_over = True
      print(f"\n❌ Sorry, that's wrong. Final score: {score} ❌")
  
  if followers == 'B':
    if player_two["follower_count"] > player_one["follower_count"]:
      score += 1
      player_one = player_two   
      player_two = random.choice(data)
      clear()
      print(f"\n✅ You're right! Current score: {score} ✅")
    else:
      game_is_over = True
      print(f"\n❌ Sorry, that's wrong. Final score: {score} ❌")