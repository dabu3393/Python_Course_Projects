import hangman_art
import requests

api_url = 'https://random-word-api.herokuapp.com/word'
word_api = requests.get(api_url).json()

print(hangman_art.logo)
chosen_letters = []
chosen_word = word_api[0]
word_length = len(chosen_word)
lives = 6

display = []

for _ in range(word_length):
    display += '_'

print(f"{' '.join(display)}")

end_of_game = False

while not end_of_game:

    guessed_letter = input('Guess a letter: ').lower()

    chosen_letters += guessed_letter

    if guessed_letter in display:
        print(f'You\'ve already guessed {guessed_letter}\n')

    print(f"\nGuessed letters: {', '.join(chosen_letters)}\n")
    
    if guessed_letter not in chosen_word:
        lives -= 1
        print(f'You guessed {guessed_letter}. That\'s not in the word.')
        if lives == 0:
            end_of_game = True
            print(f'You lose. The word was {chosen_word}.')

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f'Current position: {position}\nCurrent letter: {letter}\nGuessed letter: {guessed_letter}')
        if letter == guessed_letter:
            display[position] = letter

    print(f"{' '.join(display)}\n")

    print(hangman_art.stages[lives])

    if '_' not in display:
        end_of_game = True
        print('You win!')
