import pandas


nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}


def create_nato_list():
    user_word = input('Enter a word: ').upper()
    try:
        word_list = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        create_nato_list()
    else:
        print(word_list)


create_nato_list()
