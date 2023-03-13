#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random
word_list = ["camel", "camel", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
#Testing code
print(f'Pssst, the solution is {chosen_word}.\n')

display = []

for _ in range(word_length):
    display.append('_')

while '_' in display and lives > -1:
  blanks = display.count('_')
  guess = input("Guess a letter: ").lower()
  for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter

  print(display, '\n')
  if blanks == display.count('_'):
    print(stages[lives])
    lives -= 1
 
if lives == -1:
  print('You lose.')
else:
  print('You win.')