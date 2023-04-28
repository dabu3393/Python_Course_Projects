import os
import art

print(art.logo)
print('Welcome to the secret auction program.')

more_bidders = True
dict_of_bids = {}

def find_highest_bidder(bidding_record):
    highest_bidder = ""
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder
        elif bid_amount == highest_bid:
            highest_bidder += f' and {bidder}'
    print(f'The winner is {highest_bidder} with a bid of ${highest_bid}')

def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

while more_bidders:
    bidders_name = input('What is your name?: ')
    bid = int(input('What\'s your bid?: $'))
    dict_of_bids[bidders_name] = bid
    other_bidders = input('Are there any other bidders? Type \'yes\' or \'no\'.\n')

    if other_bidders == 'no':
        clear()
        find_highest_bidder(dict_of_bids)
        more_bidders = False
    elif other_bidders == 'yes':
        clear()
    else:
        print('Not an option. Goodbye.')
        more_bidders = False

