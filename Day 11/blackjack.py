import art
import os
import random
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
    
def calculate_score(list_of_cards):
    '''Take a list of cards and return the score calculated from the cards'''

    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0
        
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)

    return sum(list_of_cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'It\'s a draw 🙃'
    elif computer_score == 0:
        return 'Lose, opponent has a Blackjack 🤯'
    elif user_score == 0:
        return 'Win with a Blackjack 🤑'
    elif user_score > 21:
        return 'You went over 21. You lose 🙃'
    elif computer_score > 21:
        return 'Opponent went over. You win! 🤑'
    elif user_score > computer_score:
        return 'You win 🤑'
    else:
        return 'You lose 🙃'
    
def play_game():
    print(art.logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Your cards: {user_cards}, current score: {user_score}')
        print(f'Computer\'s first card: {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input('Type \'y\' to get another card, type \'n\' to pass: ')
            if another_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f'Your final hand is {user_cards}, final score: {user_score}')
    print(f'Computer\'s final hand is {computer_cards}, final score: {computer_score}')
    print(compare(user_score, computer_score))

while input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ') == 'y':
    clear()
    play_game()
