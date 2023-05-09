import art
from game_data import data
import random
import os

# Pull specific information from the dictionary
def format_data(account):
    '''returns the information on the account chosen at random'''
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f'{account_name}, a {account_description}, from {account_country}'

# Compare the two accounts with your answer
def check_answer(guess, a_followers, b_followers):
    '''Checking the answer and returning True or False, depending on whether the user guessed right or wrong.'''
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

# Print logo art
print(art.logo)
score = 0
game_continue = True
account_b = random.choice(data)

while game_continue:
    # Chooses a random dictionary from the data list
    account_a = account_b
    account_b = random.choice(data)
    # Change account_b if the account random choice is the same
    if account_a == account_b:
        account_b = random.choice(data)

    print(f'Compare A: {format_data(account_a)}')
    print(art.vs)
    print(f'Against B: {format_data(account_b)}')

    user_guess = input('Who has more followers? Type \'A\' or \'B\': ').lower()

    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']

    is_correct = check_answer(user_guess, a_followers, b_followers)

    clear()

    print(art.logo)

    # Keep score and add a point when the correct answer is guessed
    if is_correct:
        score += 1
        print(f'You\'re right! Current score: {score}')
    else:
        game_continue = False
        print(f'You\'re wrong. Final score: {score}')