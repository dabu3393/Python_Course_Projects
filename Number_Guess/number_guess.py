import art
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, answer, turns):
    '''This function will check the users guess with the answer and compare the two. It returns the number of turn remaining.'''
    if answer > user_guess:
        print('Too low.')
        return turns - 1
    elif answer < user_guess:
        print('Too high.')
        return turns - 1
    elif answer == user_guess:
        print(f'You got it! The answer was {answer}.')
    
def set_difficulty():
    '''This prompts the user for what difficulty they want, and gives them the proper amount of attempts'''
    difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    elif difficulty == 'hard':
        return HARD_LEVEL_TURNS
    else:
        return 1

def game():
    print(art.logo)
    print('Welcome to the Number Guessing Game!')
    print('I\'m thinnking of a number between 1 and 100.')
    number = random.randint(1, 100)
    # print(f'Pssst, the correct number is {number}')

    turns = set_difficulty()

    guess = 0
    while guess != number:
        print(f'You have {turns} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))
        turns = check_answer(guess, number, turns)
        if turns == 0:
            print(f'You\'ve run out of guesses, you lose. The answer was {number}.')
            return
        elif guess != number:
            print('Guess again.')

game()