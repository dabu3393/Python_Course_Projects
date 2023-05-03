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

middle_finger = '''

         / \\
        |\_/|
        |---|
        |   |
        |   |
      _ |=-=| _
  _  / \|   |/ \\
 / \|   |   |   ||\\
|   |   |   |   | \\\\
|   |   |   |   |   \\
| -   -   -   - |)   )
|                   /
 \                 /
  \               /
   \             /
    \           /
'''

game_images = [rock, paper, scissors, middle_finger]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n'))

if 2 >= user_choice >= 0:
    print(game_images[user_choice])
else:
    print(game_images[3])

print('Computer chose:')

computer_choice = random.randint(0, 2)

print(game_images[computer_choice])

if user_choice == computer_choice:
    print('You tied')
elif user_choice == 0 and computer_choice == 2:
    print('You win!')
elif user_choice == 2 and computer_choice == 0:
    print('You lose')
elif user_choice != 0 and user_choice != 1 and user_choice != 2:
    print('You lose for putting in a wrong value')
elif user_choice < computer_choice:
    print('You lose')
elif user_choice > computer_choice:
    print('You win!')

