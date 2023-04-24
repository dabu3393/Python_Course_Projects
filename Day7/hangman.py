import random

word_list = ['pencil', 'avalanche', 'aluminum', 'fencing']

chosen_word = random.choice(word_list)

display = []

for blank in chosen_word:
    display.append('_')

print(display)

end_of_game = False

while not end_of_game:

    guessed_letter = input('What letter do you guess?\n').lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        print(f'Current position: {position}\nCurrent letter: {letter}\nGuessed letter: {guessed_letter}')
        if letter == guessed_letter:
            display[position] = letter
        

    print(display)

    if '_' not in display:
        end_of_game = True
        print('You win!')