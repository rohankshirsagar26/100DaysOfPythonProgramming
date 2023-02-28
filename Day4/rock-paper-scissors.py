import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


your_choice = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n')

if your_choice=='0':
    print(f'{rock}')
elif your_choice=='1':
    print(f'{paper}')
elif your_choice=='2':
    print(f'{scissors}')

computer_choice = str(random.randint(0,2))

print('Computor chose:')

if computer_choice=='0':
    print(f'{rock}')
elif computer_choice=='1':
    print(f'{paper}')
elif computer_choice=='2':
    print(f'{scissors}')

if(your_choice == '0' and computer_choice == '1'):
    print('\nYou lose')
elif(your_choice == '0' and computer_choice == '2'):
    print('\nYou win')
elif(your_choice == '1' and computer_choice == '2'):
    print('\nYou lose')
elif(your_choice == '1' and computer_choice == '0'):
    print('\nYou win')
elif(your_choice == '2' and computer_choice == '0'):
    print('\nYou lose')
elif(your_choice == '2' and computer_choice == '1'):
    print('\nYou win')
elif(your_choice == computer_choice):
    print('\nDraw')