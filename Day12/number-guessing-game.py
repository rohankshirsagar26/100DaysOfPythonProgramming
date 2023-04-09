import random
print("Welcome to The Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
NUMBER = random.randint(1, 100)
difficulty_level = input("Choose a difficutlty. Type 'easy' or 'hard': ")
isGameOver = False

if difficulty_level == "easy":
  attempts = 10
  print(f"You have {attempts} attempts remaining to guess the number.\n")
if difficulty_level == "hard":
  attempts = 5
  print(f"You have {attempts} attempts remaining to guess the number.\n")

while attempts != 0:
  guess = int(input("Make a Guess: "))
  if guess == NUMBER:
    attempts = 0
    print(f"You got it! The answer was {NUMBER}")
    
  if guess < NUMBER:
    attempts -= 1
    print("Too low.\nGuess again")
    print(f"You have {attempts} attempts remaining to guess the number.\n")

  if guess > NUMBER:
    attempts -= 1
    print("Too high.\nGuess again")
    print(f"You have {attempts} attempts remaining to guess the number.\n")