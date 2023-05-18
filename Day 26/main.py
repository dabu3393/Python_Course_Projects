import pandas


nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

user_word = input('Enter a word: ').upper()
word_list = [nato_dict[letter] for letter in user_word]
print(word_list)

